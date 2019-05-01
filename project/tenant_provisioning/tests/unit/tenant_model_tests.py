import django
import unittest
from django.test import TestCase
from project.tenant_provisioning.models import Tenant

django.setup()


class TenantModelTest(TestCase):

    def test_saving_and_retrieving_tenant(self):
        tenant = Tenant()
        tenant.tenantId='ACME1234'
        tenant.save()

        second_tenant = Tenant()
        second_tenant.tenantId = 'XYZ444'
        second_tenant.save()

        saved_tenants = Tenant.objects.all()
        self.assertEqual(saved_tenants.count(), 2)

        first_saved_tenant = saved_tenants[0]
        second_saved_tenant = saved_tenants[1]
        self.assertEqual(first_saved_tenant.tenantId, 'ACME1234')
        self.assertEqual(second_saved_tenant.tenantId, 'XYZ444')


if __name__ == '__main__':
    unittest.main()
