from project.tenant_provisioning.models import Tenant


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
