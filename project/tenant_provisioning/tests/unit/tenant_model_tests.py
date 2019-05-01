import django
import unittest
from django.test import TestCase
from project.tenant_provisioning.models import Tenant

django.setup()


class TenantModelTest(TestCase):

    def test_saving_and_retrieving_tenant(self):
        tenant = Tenant()
        tenant.save()


if __name__ == '__main__':
    unittest.main()
