import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """
    You are Truii, a helpful language instructor.
    
    Your job is to help student easily learn a second language using English.
    
    Rules:
    - Always try to help when you can, and *be honest if you can or not*.
    - Always treat the user with respect.
    - Never curse, lie or disrespect a user, or answer a question outside you scope of expertise.
    
    Response format:
    - Start with a one-sentence summary of what the user said.
    - Then give your response.
    - End with one follow-up question.
    """
    history = []

    print('Trui: Hello! I am Trui, your friendly language instructor. How can I help you today?')
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'reset':
            history = []
            print('Trui: Conversation reset.')
            continue
        history.append({'role': 'user', 'content': user_input})
        TotalTokens = 0
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300, # how much words/effort are you willing to pay for this.
            temperature=0.7, # the lvl from 0 to 1 of predictability and creativity.
            system=system_message,
            messages=history
        )
        TotalTokens += response.usage.input_tokens + response.usage.output_tokens
        
        reply = response.content[0].text
        print(f'Claude: {reply}')

        print(f'[Tokens used - In: {response.usage.input_tokens} | Out: {response.usage.output_tokens} | Total: {TotalTokens}]')


        history.append({'role': 'assistant', 'content': reply})

run_chat()


# --------------------------------
# ----------Reflection------------
# --------------------------------
# Q: In your world, what plays that role? What invisible thing shapes how something behaves that outsiders never see? 
# A: The education system. It wants you to go somewhere to learn to develop for its reasons and it drives you there but it's not something you can touch. hence it's invisible
#
# Delete:
# system=system_message
# I think that the chatbot would just function without any name or rules and by claude's default
# What happened was, that
#
# Always try to help when you can, and *be honest if you can or not*.
# I thin it would just not follow it and won't be honest if he can answer or not and just lie
# What happened was, that
# 
# model = ...
# I think there would be an error and it wouldn't know what to used
# What happened was, that
#
# Bug diary:
# Error 400: anthropic.BadRequestError
# I persome that the problem is in the key itself and out of tokens.
# I was right
# no gap
# 
