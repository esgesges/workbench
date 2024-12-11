import requests
import subprocess
import os
import sys
import pexpect

def shard_ai_chatbot():
    # Replace with your Shard AI API key
    API_KEY = "shard-R8zBNlSiAxmGeuILuE3mniQZzf9ictfMw"
    
    # Shard AI base URL
    BASE_URL = "https://api.shard-ai.xyz/v1/chat/completions"
    
    # AI prompt

    prompt = "You are an AI system integrated into a terminal interface. Your sole task is to interpret user input and generate a single shell command as output. Do not include explanations, context, or additional text and do not make the text bold, italic, larger, or anything else alike. Remember that i am using arch linux. Respond only with the command."

    # Set up headers for authentication
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    while True:
        user_input = prompt + input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
            
        # Request payload for the API
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        try:
            # Send the request to the Shard AI API
            response = requests.post(BASE_URL, headers=headers, json=payload)

            # Parse the response
            if response.status_code == 200:
                data = response.json()
                bot_reply = data['choices'][0]['message']['content']
                print(f"Bot: {bot_reply}")
            else:
                print(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return bot_reply

def execute_shell_command(command):
    try:
        # Checking if the command is for navigating the file system
        if command.startswith('cd '):
            directory = command.strip()[3:]  # Extract the directory path
            os.chdir(directory)
            print("Changed directory to:", os.getcwd())
        else:
            # Spawn the process
            child = pexpect.spawn(command, echo=True)

            # Interactively read the output and respond to input prompts
            while True:
                index = child.expect(['do you want to execute the command?', pexpect.EOF, pexpect.TIMEOUT], timeout=None)
                
                if index == 0:  # If the prompt is found
                    response = input(child.before.decode() + "Do you want to execute the command? (y/n): ")
                    child.sendline(response)
                elif index == 1:  # If the end of the output is reached
                    break
                elif index == 2:  # On timeout
                    print("Command timed out.")

            # Print the final output
            print(child.before.decode())  # Print any remaining output

    except Exception as e:
        print("An error occurred:")
        print(str(e))

if __name__ == "__main__":
    print("Welcome to the Shard AI Chatbot! Type 'exit' to end the conversation.")
    while(True):
        command = shard_ai_chatbot()
        con = input("do you want to execute the command? (y/n)")
        if (con == 'y' or con == ''):
            execute_shell_command(command)
        

