# aws_tenant_provisioning
Small application to automate/orchastrate some AWS configurations

Please set you environment variable for your environment or the code with throw an ImportError.
It is advisable to set the environment default to 'test' for your default test config

Environment variable options:

    environment=test (test, prod, local)
    
    
###### LocalStack:

Used for local development to prevent unnecessary charges against AWS

    https://github.com/localstack/localstack

LocalStack does not yet support the kms end point, so we will leverage another tool:

    https://github.com/nsmithuk/local-kms
    

Currently, you must restart local stack to complete the functional tests if they were already ran once.


