import requests
from telegram.ext import Updater, MessageHandler, filters
import json

def getMessage(botToken):
    method = "getUpdates"
    url = f"https://api.telegram.org/bot{botToken}/{method}"
    response = requests.get(url)
    print(response.text)
    data = response.json()
    if data["ok"]:
        updates = data["result"]
        if updates:
            latest_update= updates[-1]
            return latest_update
    print("mcdcdcmd cmd cdmc dmc")
    return None

def req(url, content, model):
    apikey = "shard-RlY0kvMvQvpdYKprWDMsVX1zDKKkuo3ff"
    data = {
        "messages": [{"role": "user", "content": content}],
        "model": model
    }
    headers = {
        "Authorization": f"Bearer {apikey}",
        "Content-Type": "application/json"
    }
    response = requests.post(url=url, headers=headers, json=data)
    return response

def getResult(response):
    try:
        result = response.json().get('choices')[0].get('message').get('content')
        return result
    except (json.decoder.JSONDecodeError, IndexError, KeyError) as e:
        print("Error:", e)
        return ""

def sendMessage(botKey, chat_id, message):
    url = f"https://api.telegram.org/bot{botKey}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print("Error sending message to Telegram")

def main():
    botKey = "7090375373:AAHNBHKUGn4Odg5FYJb30nQoK63TJW4dw0E"
    module = "gpt-4"
    chat_id = 716727488
    AIurl = "https://api.shard-ai.xyz/v1/chat/completions"

    updates = getMessage(botKey)
    print(updates)
    res = updates.get("result", [])
    print(res)
    for update in updates.get("result", []):
        message = update.get("message")
        print(message)
        if message:
            text = message.get("text")
            print(text)
            AIresponse = req(AIurl, text, module)
            result = getResult(AIresponse)
            print(result)
            if result:
                sendMessage(botKey, chat_id, result)
            else:
                print("No response from AI API")

if __name__ == "__main__":
    main()
