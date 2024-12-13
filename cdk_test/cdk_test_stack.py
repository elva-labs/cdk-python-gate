from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    CfnOutput,
)
from constructs import Construct
import os


class CdkTestStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, stage: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Use stage variable to make resource names unique
        lambda_name = f"TestLambdaFunction-{stage}"

        # Create Lambda function with environment variable
        self.lambda_function = lambda_.Function(
            self,
            lambda_name,
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="handler.lambda_handler",
            code=lambda_.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "..", "src")
            ),
            environment={
                "SUCCESS_MESSAGE": f"Hello from Lambda in {stage} stage!",
                "STAGE": stage,
            },
        )

        # Add Function URL with authentication type set to NONE (publicly accessible)
        self.lambda_function_url = self.lambda_function.add_function_url(
            auth_type=lambda_.FunctionUrlAuthType.NONE,
            cors=lambda_.FunctionUrlCorsOptions(
                allowed_origins=[
                    "*"
                ],  # Be cautious with allowing all origins in production
                allowed_methods=[lambda_.HttpMethod.GET],
                allowed_headers=["Content-Type"],
            ),
        )

        # Output the Function URL for easy access
        CfnOutput(
            self,
            f"LambdaFunctionUrl-{stage}",
            value=self.lambda_function_url.url,
            description=f"The URL of the Lambda function in the {stage} stage",
        )
