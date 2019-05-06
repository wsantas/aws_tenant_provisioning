from project import settings
from project.tenant_provisioning.models import Tenant
import boto3


class TenantAlreadyExistError(Exception):
    pass


class CreateIamUser:

    def __init__(self,
                 tenant_id, endpoint_url):
        self._tenant_id = tenant_id
        self._endpoint_url = endpoint_url

    def execute(self):
        self.valid_data()
        tenant = Tenant(tenant_id=self._tenant_id)



        tenant.save()
        return tenant

    def valid_data(self):
        try:
            tenant = Tenant.objects.get(tenant_id=self._tenant_id)
        except Tenant.DoesNotExist:
            print('Not found')
            tenant = None

        if tenant is not None:
            # Raise a meaningful error to be catched by the client
            error_msg = (
                'There is an user account with {} tenant id. '
                'Please, try another tenant id'
            ).format(self._tenant_id)

            raise TenantAlreadyExistError(_(error_msg))

        return True

    def create_iam_user(self):
        iamClient = boto3.client(
            'iam',
            endpoint_url=self._endpoint_url,
            region_name=settings.AWS_DEFAULT_REGION,
            aws_access_key_id='accesskey',
            aws_secret_access_key='secretkey',
        )
        print('this is a test')
        response = iamClient.create_user(
            UserName=self._tenant_id,
            PermissionsBoundary='12345678901234567890',
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        )
        print('this is a test2')
        return True

