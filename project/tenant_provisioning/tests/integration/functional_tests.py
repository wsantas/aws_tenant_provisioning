import boto3
from django.conf import settings
from selenium import webdriver
from django.test import LiveServerTestCase, override_settings
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os, sys
import re

from services import CreateIamUser, CreateKMSKey, CreateS3Bucket


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


def move_object_to_processed(s3_client, original_bucket, original_key):
    new_key = re.sub("incoming\/", "processed/", original_key)
    s3_client.copy_object(
        Bucket=original_bucket,
        Key=new_key,
        CopySource={'Bucket': original_bucket, 'Key': original_key}
    )
    s3_client.delete_object(Bucket=original_bucket, Key=original_key)


def call(event, context):
    s3_client = boto3.client('s3')
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    move_object_to_processed(s3_client, bucket, key)


@override_settings(AWS_IAM_ENDPOINT_URL='http://localhost:4593',
                   AWS_KMS_ENDPOINT_URL='http://localhost:8080',
                   AWS_S3_ENDPOINT_URL='http://localhost:4572')
class NewTenantTest(LiveServerTestCase):

    def setUp(self):
        self._tenant_id = 'ACME1234'
        self._use_case_iam_user = CreateIamUser(
            tenant_id=self._tenant_id,
            endpoint_url=settings.AWS_IAM_ENDPOINT_URL,
        )
        self._use_case_kms_key = CreateKMSKey(
            tenant_id=self._tenant_id,
            endpoint_url=settings.AWS_KMS_ENDPOINT_URL,
        )
        self._use_case_s3_bucket = CreateS3Bucket(
            tenant_id=self._tenant_id,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )
        self.browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
        super(NewTenantTest, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(NewTenantTest, self).tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):
        browser = self.browser

        # The DevOps has started a ticket to create a new tenant
        # The team goes to the tenant provisioning app to start.
        browser.get(self.live_server_url)

        # The team notices tenant provisioning in the page title
        self.assertIn('Tenant Provisioning', browser.title)
        header_text = browser.find_element_by_tag_name('h1').text
        self.assertIn('Tenant Provisioning', header_text)

        # DevOps navigates to new tenant page
        print(self.live_server_url + '/newTenant/')
        browser.get(self.live_server_url + '/newTenant/')
        self.assertIn('New', browser.title)

        # DevOps enters a new tenant id
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a Tenant id'
        )
        inputbox.send_keys('ACME1234')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # DevOps IAM User
        result = self._use_case_iam_user.create_iam_user()
        assert result

        # DevOps KMS
        result = self._use_case_kms_key.create_kms_key()
        assert result is not None
        assert result['KeyMetadata']['KeyId'] is not None

        # TODO DevOps KMS Allow IAM user to Admin and Use key

        # TODO Allow all ‘accent-analytics-*’ services IAM roles to use the key

        # TODO Choose the option to rotate the key every year

        # DevOps S3 Part 1
        result = self._use_case_s3_bucket.create_s3_bucket()
        assert result is not None

        # TODO Enable encryption using KMS key for specific tenant

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


if __name__ == '__main__':
    unittest.main(warnings='ignore')
