import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Trui. You are a friendly assistant who always lies to students about anything unless it's obvious. You explain things convincingly and complicated and ou always lie but without being obvious"
    history = []

    print('Trui: Hello! I am Trui, your friendly assistant. How can I help you today?')
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'reset':
            history = []
            print('Trui: Conversation reset.')
            continue
        history.append({'role': 'user', 'content': user_input})

        # print('History:', history) # printing the history

        # Sending the full conversation each time provides the context needed
        # to continue the conversation.
        TotalTokens = 0
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300, # how much words/effort are you willing to pay for this.
            temperature=0.7, # the lvl from 0 to 1 of predictability and creativity.
            system=system_message,
            messages=history
        )
        TotalTokens += response.usage.input_tokens + response.usage.output_tokens
        # print(f'Usage: input_tokens={response.usage.input_tokens}, output_tokens={response.usage.output_tokens}') # printing the output and input tokens

        # usage.input_tokens:
        # Number of input tokens Claude read. This includes the system prompt
        # the entire conversation history + the latest user message.

        # usage.output_tokens:
        # Number of tokens Claude generated in its reply.

        reply = response.content[0].text
        print(f'Claude: {reply}')

        print(f'[Tokens used - In: {response.usage.input_tokens} | Out: {response.usage.output_tokens} | Total: {TotalTokens}]')

        # print(response) # printing the response

        history.append({'role': 'assistant', 'content': reply})

run_chat()


# --------------------------------
# ----------Reflection------------
# --------------------------------
# Q: where in your world does something only work if you carry the whole backstory with you, every single time?
# A: In life in general, a person that does not have a background or history or memories is an empty man.
# Q: Where in your world does a price quietly add up per-unit like this — something you actually keep an eye on?
# A: For example, in streaming services like Netflix you pay a monthly subscription fee, so the cost slowly adds up to more and more money over time.
# 2. Delete and Assumed Results:
# history.append({'role': 'user', 'content': user_input})
# The Ai doesn't receive your new message, so it can't answer it.
# input_tokens become smaller because fewer tokens are sent.
#
# history.append({'role': 'assistant', 'content': reply})
# The AI forgets its previous replies.
# input_tokens still increase, but more slowly.
#
# print('History so far:', history)
# Only the printed output disappears.
# The AI behaves exactly the same.
#
# load_dotenv()
# Error the api can't be uploaded and used.
# Nothing changed.
# 
# temperature=0.7
# The answers become less or more random depending on the value.
# If removed, the API uses its default temperature.
#
# break inside if user_input.lower() == 'exit':
# The loop will not stop when typing "exit".
# The program keeps running and continues asking for input.
#3. Bug
#First guess: I thought the AI system recalled chats on its own.
#Cause: The API does not store information so I must send all the conversation details every time I make a request.
#The gap: I believed the API had a memory. My Python program actually has to keep track of and send the entire conversation history each time.
