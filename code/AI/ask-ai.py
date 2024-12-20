#!/usr/bin/env python3

import requests
import subprocess
import os

def shard_ai_chatbot():
    API_KEY = "shard-R8zBNlSiAxmGeuILuE3mniQZzf9ictfMw"
    BASE_URL = "https://api.shard-ai.xyz/v1/chat/completions"
    prompt = "You are an AI system integrated into a terminal interface. Your sole task is to interpret user input and generate a single shell command as output. Do not include explanations, context, or additional text and do not make the text bold, italic, larger, or anything else alike. Remember that I am using Arch Linux. Respond only with the command."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": f"{prompt}\n{user_input}"}
            ]
        }

        try:
            response = requests.post(BASE_URL, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                bot_reply = data['choices'][0]['message']['content'].strip()
                print(f"Bot: {bot_reply}")
                return bot_reply
            else:
                print(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")

def execute_shell_command(command):
    try:
        if command.startswith('cd '):
            directory = command.strip()[3:]
            os.chdir(directory)
            print("Changed directory to:", os.getcwd())
        else:
            # Use subprocess.run with input/output attached to the terminal
            process = subprocess.run(command, shell=True)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    print("Welcome to the Shard AI Chatbot! Type 'exit' to end the conversation.")
    while True:
        command = shard_ai_chatbot()
        if not command:
            continue
        confirm = input("Do you want to execute the command? (y/n): ").strip().lower()
        if confirm in ['y', 'yes', '']:
            execute_shell_command(command)
