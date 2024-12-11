import requests
import subprocess
import os

def shard_ai_chatbot():
    # Replace with your Shard AI API key
    API_KEY = "shard-R8zBNlSiAxmGeuILuE3mniQZzf9ictfMw"
    
    # Shard AI base URL
    BASE_URL = "https://api.shard-ai.xyz/v1/chat/completions"
    
    # Set up headers for authentication
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    print("Welcome to the Shard AI Chatbot! Type 'exit' to end the conversation.")

    while True:
        user_input = "give me the exact terminal command for the action that follows, please don't write anything beside the actual terminal command (i am using arch linux). also dont add punctuation"
        user_input += input("You: ")
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
            # Extract the directory path from the command
            directory = command.strip()[3:]
            
            # Change the current working directory
            os.chdir(directory)
            print("Changed directory to:", os.getcwd())
        else:
            # Execute the command
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

            # Print the standard output and standard error
            print("Standard Output:\n", result.stdout)
            print("Standard Error:\n", result.stderr)  # Will be empty if no error occurred
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command:")
        print("Return Code:", e.returncode)
        print("Output:", e.output)
        print("Error Output:", e.stderr)

if __name__ == "__main__":
    while(True):
        command = shard_ai_chatbot()
        execute_shell_command(command)

