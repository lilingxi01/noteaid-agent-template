import json

from handler import MyAgent


def handler(event, context):
    agent = MyAgent()

    print("Received event:", json.dumps(event, indent=2))

    return {"statusCode": 200, "body": "hello world"}
