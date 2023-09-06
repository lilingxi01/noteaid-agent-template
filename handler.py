from typing import List, Union

from notebridge import Bridge, ChatMessage, ChatContext


class MyAgent(Bridge):
    def on_receive(self, message_stack: List[ChatMessage], context: ChatContext) -> Union[str, List[str]]:
        # TODO: Implement your agent here.
        # You can access environment variables by using something like `os.environ['OPENAI_API_KEY']`.
        return 'Hello, world!'
