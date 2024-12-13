import os
import json


def lambda_handler(event, context):
    """
    Lambda function handler for processing events.

    :param event: AWS Lambda uses this parameter to pass in event data to the handler
    :param context: Runtime information provided by AWS Lambda
    :return: A dictionary response
    """
    try:
        # Retrieve the environment variable
        success_message = os.environ.get(
            "SUCCESS_MESSAGE", "Default success message, NICE!"
        )

        # Process the incoming event
        print(f"Received event: {event}")

        # Return response using the environment variable with consistent headers
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(success_message),
        }
    except Exception as e:
        print(f"Error processing event: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(str(e)),
        }
