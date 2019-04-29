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
        browser.get(self.live_server_url)

        # The team notices tenant provisioning in the page title
        self.assertIn('Tenant Provisioning', browser.title)
        header_text = browser.find_element_by_tag_name('h1').text
        self.assertIn('Tenant Provisioning', header_text)

        # DevOps navigates to new tenant page
        print(self.live_server_url+'/newTenant')
        browser.get(self.live_server_url+'/newTenant')
        print('*** '+browser.title)
        self.assertIn('New', browser.title)

        # DevOps enters a new tenant id
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a client id'
        )


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
