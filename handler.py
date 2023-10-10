from typing import List, Union

from notebridge import Bridge, ChatMessage, ChatContext
import openai


class MyAgent(Bridge):
    def on_receive(self, message_stack: List[ChatMessage], context: ChatContext) -> Union[str, List[str]]:
        # TODO: Implement your agent here.
        # You can access environment variables by using something like `os.environ['OPENAI_API_KEY']`.

        gpt_messages = [{
            "role": "system",
            "content": f'You are role-playing as a physician called NoteAid, who can answer patients\' questions about their health. Here is patient\'s clinical note: {context.note}',
        }]

        for prev_message in message_stack:
            if prev_message.is_agent:
                gpt_messages.append({
                    "role": "assistant",
                    "content": prev_message.content,
                })
            else:
                gpt_messages.append({
                    "role": "user",
                    "content": prev_message.content,
                })

        chat_completion = openai.ChatCompletion.create(model='gpt-4', messages=gpt_messages)
        answer = chat_completion.choices[0].message.content

        return answer
