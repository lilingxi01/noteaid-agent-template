import json

from handler import MyAgent
from notebridge import make_executor


def handler(event, context):
    print("Received event:", json.dumps(event, indent=2))

    agent = MyAgent()
    executor = make_executor(agent=agent)
    return executor(event, context)
