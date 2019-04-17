import unittest

from django.urls import resolve
from django.test import TestCase
from tenant_provisioning.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


if __name__ == '__main__':
    unittest.main()
