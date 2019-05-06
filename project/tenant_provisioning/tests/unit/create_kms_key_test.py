import unittest

from django.conf import settings
from django.test import TestCase, override_settings
from moto import mock_kms

from project.tenant_provisioning.models import Tenant
from services import CreateIamUser, CreateKMSKey


class CreateIamUserTest(TestCase):

    def setUp(self):
        # setup method will be executed on each test
        self._use_case = CreateKMSKey(
            tenant_id="ACME1234",
            endpoint_url=settings.AWS_IAM_ENDPOINT_URL,
        )

    def test_create_iam_user(self):
        result = self._use_case.execute()
        assert result

    def test_create_kms_key(self):
        with mock_kms():
            result = self._use_case.create_kms_key()
            assert result

    # def test_create_iam_user_tenant_exists_exception(self):
    #     result = self._use_case.execute()
    #     assert isinstance(result, Tenant)


if __name__ == '__main__':
    unittest.main()


