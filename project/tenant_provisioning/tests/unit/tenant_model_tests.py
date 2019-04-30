from unittest import TestCase

from project.tenant_provisioning.models import Tenant


class TenantModelTest(TestCase):

    def test_saving_and_retrieving_tenant(self):
        tenant = Tenant()
