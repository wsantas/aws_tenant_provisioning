import boto3
import pytest
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from botocore.exceptions import ClientError
from moto import mock_s3
from mock import patch, call
import time
import unittest
import os, sys


def s3_object_created_event(bucket_name, key):
    # NOTE: truncated event object shown here
    return {
        "Records": [
            {
                "s3": {
                    "object": {
                        "key": key,
                    },
                    "bucket": {
                        "name": bucket_name,
                    },
                },
            }
        ]
    }


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
        print(self.live_server_url+'/newTenant/')
        browser.get(self.live_server_url+'/newTenant/')
        self.assertIn('New', browser.title)

        # DevOps enters a new tenant id
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a client id'
        )
        inputbox.send_keys('ACME1234')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'ACME1234' for row in rows),
            f"New tenant item did not appear in table. Contents were:\n{table.text}"
        )

    def test_handler_moves_incoming_object_to_processed(self):
        with mock_s3():
            # Create the bucket
            conn = boto3.resource('s3', region_name='us-east-1')
            conn.create_bucket(Bucket="some-bucket")
            # Add a file
            boto3.client('s3', region_name='us-east-1').put_object(Bucket="some-bucket", Key="incoming/transaction-0001.txt", Body="Hello World!")

            # Run call with an event describing the file:
            call(s3_object_created_event("some-bucket", "incoming/transaction-0001.txt"), None)

            # Assert the original file doesn't exist
            with pytest.raises(ClientError) as e_info:
                conn.Object("some-bucket", "incoming/transaction-0001.txt").get()
                assert e_info.response['Error']['Code'] == 'NoSuchKey'

            # Check that it exists in `processed/`
            obj = conn.Object("some-bucket", "processed/transaction-0001.txt").get()
            assert obj['Body'].read() == b'Hello World!'




if __name__ == '__main__':
    unittest.main(warnings='ignore')
