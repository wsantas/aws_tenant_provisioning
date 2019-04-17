from selenium import webdriver
import os
import unittest


class NewTenantTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # The DevOps has started a ticket to create a new tenant
        # The team goes to the tenant provisioning app to start.
        self.browser.get('http://localhost:8000')

        # The team notices tenant provisioning in the page title
        self.assertIn('Tenant Provisioning', self.browser.title)

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

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
