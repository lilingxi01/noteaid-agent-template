import json
import logging

from pydantic import ValidationError
from handler import MyAgent
from notebridge import ChatMessage, ChatContext


def handler(event, context):
    agent = MyAgent()

    print("Received event:", json.dumps(event, indent=2))

    if 'message_stack' not in event or type(event['message_stack']) != list:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Message stack (message_stack) is invalid from the request."
            })
        }

    if 'context' not in event or type(event['context']) != dict:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Context (context) is invalid from the request."
            })
        }

    try:
        message_stack = [ChatMessage(**m) for m in event['message_stack']]
        context = ChatContext(**event['context'])
    except ValidationError as e:
        logging.error(f"Error occurred while parsing the request: {str(e)}")
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": f"Invalid message_stack or context structure: {str(e)}"
            })
        }

    response = agent.on_receive(message_stack=message_stack, context=context)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "response": response
        })
    }
