import unittest
from unittest.mock import call

from django.urls import resolve
from django.test import TestCase
from project.tenant_provisioning.views import new_tenant_page


class NewTenantTest(TestCase):

    def test_new_tenant_url_resolves_to_new_tenant_view(self):
        found = resolve('/newTenant/')
        self.assertEqual(found.func, new_tenant_page)

    def test_can_save_a_POST_request(self):
        response = self.client.post('/postTenant/', data={'tenant_id': 'ACME1234'})
        self.assertIn('ACME1234', response.content.decode())


if __name__ == '__main__':
    unittest.main()
