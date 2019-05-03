from project import settings
from project.tenant_provisioning.models import Tenant
import boto3


class TenantAlreadyExistError(Exception):
    pass


class CreateIamUser:

    def __init__(self,
                 tenantId):
        self._tenantId = tenantId

    def execute(self):
        self.valid_data()
        tenant = Tenant(tenantId=self._tenantId)



        tenant.save()
        return tenant

    def valid_data(self):
        try:
            tenant = Tenant.objects.get(tenantId=self._tenantId)
        except Tenant.DoesNotExist:
            print('Not found')
            tenant = None

        if tenant is not None:
            # Raise a meaningful error to be catched by the client
            error_msg = (
                'There is an user account with {} tenant id. '
                'Please, try another tenant id'
            ).format(self._tenantId)

            raise TenantAlreadyExistError(_(error_msg))

        return True

    def create_iam_user(self):
        iamClient = boto3.client(
            'iam',
            endpoint_url=settings.AWS_IAM_ENDPOINT_URL,
            region_name=settings.AWS_DEFAULT_REGION,
            aws_access_key_id='accesskey',
            aws_secret_access_key='secretkey',
        )
        print('this is a test')
        response = iamClient.create_user(
            UserName=self._tenantId,
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

