#!/usr/bin/env python3
import aws_cdk as cdk

from cdk_test.cdk_test_stack import CdkTestStack


app = cdk.App()
CdkTestStack(app, "CdkTestStack", env=cdk.Environment(region="eu-north-1"))

app.synth()
