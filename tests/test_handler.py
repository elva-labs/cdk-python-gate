import os
import pytest
import json
from src.handler import lambda_handler


def test_lambda_handler_success():
    """
    Test the lambda_handler function with a sample event
    """
    # Simulate an event
    test_event = {}
    test_context = {}

    # Set up environment variable for testing
    os.environ["SUCCESS_MESSAGE"] = "Test success message"

    # Call the lambda handler
    response = lambda_handler(test_event, test_context)

    # Assert the response structure and content
    assert response["statusCode"] == 200
    assert response["body"] == json.dumps("Test success message")
    assert "headers" in response
    assert response["headers"]["Content-Type"] == "application/json"
    assert response["headers"]["Access-Control-Allow-Origin"] == "*"


def test_lambda_handler_default_message():
    """
    Test the lambda_handler with no environment variable set
    """
    # Remove the environment variable
    if "SUCCESS_MESSAGE" in os.environ:
        del os.environ["SUCCESS_MESSAGE"]

    # Simulate an event
    test_event = {}
    test_context = {}

    # Call the lambda handler
    response = lambda_handler(test_event, test_context)

    # Assert the response falls back to default
    assert response["statusCode"] == 200
    assert response["body"] == json.dumps("Default success message, NICE!")
