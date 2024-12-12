#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
import requests
import subprocess
import os

# Keep track of widgets created in display_output
output_widgets = {}

def userinput(root):
    label = tk.Label(root, text='Explain the command you want to run:')
    label.pack()

    textbox = tk.Entry(root, width=50)
    textbox.pack()

    button = tk.Button(root, text='SEND',
                       command=lambda: IO_AI(root, textbox.get()))
    button.pack()

def IO_AI(root, user_input):
    command = shard_ai_chatbot(user_input)
    display_output(root, command)

def shard_ai_chatbot(user_input):
    # For testing purposes, return a dummy command
    return "ls"

    # Uncomment the following lines for actual API integration
    API_KEY = "shard-R8zBNlSiAxmGeuILuE3mniQZzf9ictfMw"
    BASE_URL = "https://api.shard-ai.xyz/v1/chat/completions"
    prompt = ("You are an AI system integrated into a terminal interface. "
              "Your sole task is to interpret user input and generate a single "
              "shell command as output. Do not include explanations, context, "
              "or additional text. Remember that I am using Arch Linux. "
              "Respond only with the command.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

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
            return data['choices'][0]['message']['content'].strip()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return "Error: Failed to generate command"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error: Exception occurred"

def display_output(root, command):
    global output_widgets

    # Destroy previous widgets if they exist
    if "label" in output_widgets:
        output_widgets["label"].destroy()
    if "button" in output_widgets:
        output_widgets["button"].destroy()

    # Create a new label to display the command
    label = tk.Label(root, text=f'Command output: {command}')
    label.pack()

    # Create a new RUN button to execute the command
    button = tk.Button(root, text='RUN',
                       command=lambda: execute_shell_command(command))
    button.pack()

    # Save references to the new widgets
    output_widgets["label"] = label
    output_widgets["button"] = button

def execute_shell_command(command):
    try:
        if command.startswith('cd '):
            directory = command.strip()[3:]
            os.chdir(directory)
            print("Changed directory to:", os.getcwd())
        else:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout if result.stdout else result.stderr

        # Display the output in the GUI
        output_label = tk.Label(root, text=f'Command Output:\n{output}', wraplength=500, justify="left", bg="#90ee90")
        output_label.pack()
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("AI Command Executor")
    root['bg'] = '#90ee90'
    root.geometry("500x300")

    # Set up the input UI
    userinput(root)

    # Start the GUI event loop
    root.mainloop()
