from selenium import webdriver

browser = webdriver.Firefox()

# The DevOps has started a ticket to create a new tenant
# The team goes to the tenant provisioning app to start.
browser.get('http://localhost:8000')

# The team notices tenant provisioning in the page title
assert 'Tenant Provisioning' in browser.title

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

# Satisfied, DevOps closes the ticket
browser.quit()