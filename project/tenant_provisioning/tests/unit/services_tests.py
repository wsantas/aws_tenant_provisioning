import unittest

from django.test import TestCase

from project.tenant_provisioning.models import Tenant
from services import CreateIamUser


class CreateIamUserTest(TestCase):

    def setUp(self):
        # setup method will be executed on each test
        self._use_case = CreateIamUser(
            tenantId="ACME1234"
        )

    def test_create_iam_user(self):
        result = self._use_case.execute()
        assert isinstance(result, Tenant)

    # def test_create_iam_user_tenant_exists_exception(self):
    #     result = self._use_case.execute()
    #     assert isinstance(result, Tenant)


if __name__ == '__main__':
    unittest.main()
