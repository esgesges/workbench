import requests
from telegram.ext import Updater, MessageHandler, filters
import json
import time


def getMessage(botToken):
    url = f"https://api.telegram.org/bot{botToken}/getUpdates"
    response = requests.get(url)
    jResponse = response.json()

    # Check if 'result' is empty
    if not jResponse.get('result'):
        print("No updates found. Send a message to the bot first.")
        return None

    print(jResponse['result'][-1])  # Debug: print the latest update
    text = jResponse['result'][-1]['message']['text']
    if text == "/get":
        text = jResponse['result'][-2]['message']['text']
    else:
        text = "aaa"

    return text



def sendToAi(text):
    apikey = "shard-RlY0kvMvQvpdYKprWDMsVX1zDKKkuo3ff"
    model = "gpt-4"
    url = "https://api.shard-ai.xyz/v1/chat/completions"

    data = {
        "messages": [{"role": "user", "content": text}],
        "model": model
    }
    headers = {
        "Authorization": f"Bearer {apikey}",
        "Content-Type": "application/json"
    }
    response = requests.post(url=url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

def sendToTelegram(botToken, text):
    url = f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id=716727488&text={text}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error sending message to Telegram")
    return response



def main():
    botToken = "7090375373:AAHNBHKUGn4Odg5FYJb30nQoK63TJW4dw0E"
#    message = getMessage(botToken)
#    AIresponse = sendToAi(message)
    sendToTelegram(botToken, "AIresponse")
    time.sleep(5)
print("-----------------")
while True:
    main()
#    break
#    time.sleep(5)



