import django
import unittest
from django.test import TestCase

from project.tenant_provisioning.serializer import TenantSerializer

django.setup()


class TenantSerializerTest(TestCase):

    def test_serializer(self):
        serializer = TenantSerializer()
        serializer.createIamUser(self)


if __name__ == '__main__':
    unittest.main()
