#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_test.cdk_test_stack import CdkTestStack

# Get the stage from an environment variable, default to 'dev'
stage = os.getenv("STAGE", "dev")

# Initialize the CDK app
app = cdk.App()

# Pass the stage variable to the stack
CdkTestStack(
    app, f"CdkTestStack-{stage}", stage=stage, env=cdk.Environment(region="eu-north-1")
)

# Synthesize the app
app.synth()
