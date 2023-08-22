from typing import List, Union

from notebridge import Bridge, ChatMessage, ChatContext


class MyAgent(Bridge):
    def on_receive(self, message_stack: List[ChatMessage], context: ChatContext) -> Union[str, List[str]]:
        # TODO: Implement your agent here.
        pass
