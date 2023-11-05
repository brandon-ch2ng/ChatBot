import os
import openai

openai.api_key = "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"

def chat (messages):
	response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
	return response.choices[0].message['content']

conversation=[
  {"role": "system", "content": "A helpful assistant."},
  {"role": "user", "content": "Answer the question"}
]

print("Chatbot: Hi there! I'm a chatbot. You can start our conversation, or type 'exit' to end it.")

while (True):
    userInput = input('\nYou: ')
    conversation.append({"role": "user", "content": userInput})
    
    response = chat(conversation)
    print('\nChatbot: ', response)
    
    if (userInput.lower() == 'exit'):
        break
 