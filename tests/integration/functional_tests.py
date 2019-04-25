from selenium import webdriver
from django.test import LiveServerTestCase
import os
import unittest


class NewTenantTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
        super(NewTenantTest, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(NewTenantTest, self).tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):
        browser = self.browser;
        # The DevOps has started a ticket to create a new tenant
        # The team goes to the tenant provisioning app to start.
        browser.get('http://localhost:8000')

        # The team notices tenant provisioning in the page title
        self.assertIn('Tenant Provisioning', browser.title)
        header_text = browser.find_element_by_tag_name('h1').text
        self.assertIn('Tenant Provisioning', header_text)

        # DevOps navigates to new tenant page

        # DevOps IAM User

        # DevOps KMS

        # DevOps S3 PArt 1

        # DevOps IAM Policies

        # DevOps DynamoDB Part 1

        # DevOps API Gateway

        # DevOps Cognito

        # DevOps DynamoDB Part 2

        # DevOps CloudWatch

        # DevOps S3 PArt 2


if __name__ == '__main__':
    unittest.main(warnings='ignore')
