#!/usr/bin/env python3
from time import sleep
from tkinter import *
import customtkinter
import tkinter as tk
import requests
import subprocess
import os
# Keep track of widgets created in display_output
output_widgets = {}
def userinput(root):

    textbox = customtkinter.CTkEntry(
        master=root,
        placeholder_text="\t\tInserisci comando",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#ffffff",
        height=100,
        width=495,
        border_width=2,
        corner_radius=40,
        border_color="#ffffff",
        bg_color="#042a27",
        fg_color="#ff2e2e",
        )
    textbox.place(x=70, y=50)

    Button_id1 = customtkinter.CTkButton(
        master=root,
        text="SEND",
        font=("undefined", 18),
        text_color="#000000",
        hover=True,
        hover_color="#fe0101",
        height=30,
        width=95,
        border_width=2,
        corner_radius=16,
        border_color="#ffffff",
        bg_color="#042a27",
        fg_color="#ff00dd",
        command=lambda: IO_AI(root, textbox.get()),
        )
    Button_id1.place(x=600, y=80)

def IO_AI(root, user_input):
    command = shard_ai_chatbot(user_input)
    display_output(root, command)

def shard_ai_chatbot(user_input):
    # For testing purposes, return a dummy command
    # return "touch ex.txt && ls && rm ex.txt && ls"

    # Uncomment the following lines for actual API integration
    API_KEY = "shard-R8zBNlSiAxmGeuILuE3mniQZzf9ictfMw"
    BASE_URL = "https://api.shard-ai.xyz/v1/chat/completions"
    prompt = ("You are an AI system integrated into a terminal interface. "
              "Your sole task is to interpret user input and generate a single "
              "shell command as output. Do not include explanations, context, "
              "or additional text. Remember that I am using Arch Linux. "
              "if i need multiple commands, always separate them with &&"
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
    label = customtkinter.CTkLabel(
    master=root,
    text=f"{command}",
    font=("Arial", 18),
    text_color="#ffffff",
    height=130,
    width=495,
    corner_radius=13,
    bg_color="#042a27",
    fg_color="#ff2e2e",
    )
    label.place(x=60, y=190)


    # Create a new RUN button to execute the command
    button = customtkinter.CTkButton(
        master=root,
        text="RUN",
        font=("undefined", 18),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=30,
        width=95,
        border_width=2,
        corner_radius=16,
        border_color="#ffffff",
        bg_color="#042a27",
        fg_color="#ff00dd",
        command=lambda: execute_shell_command(command),
        )
    button.place(x=600, y=230)


    # Save references to the new widgets
    output_widgets["label"] = label
    output_widgets["button"] = button

def execute_shell_command(command):
    try:
        # Split the string by '&&' and strip whitespace from each part
        commands = [cmd.strip() for cmd in command.split(' && ')]


        # Print each command individually
        for i, command in enumerate(commands, start=1):
            print(f"Command {i}: {command}")
            if command.startswith('cd '):
                directory = command.strip()[3:]
                os.chdir(directory)
                # Display the output in the GUI
                out_label = customtkinter.CTkLabel(
                    master=root,
                    text=f"changed directory to {directory}",
                    font=("Arial", 18),
                    text_color="#ffffff",
                    height=430,
                    width=495,
                    corner_radius=13,
                    bg_color="#042a27",
                    fg_color="#ff2e2e",
                    )
                out_label.place(x=60, y=350)
            else:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                output = result.stdout if result.stdout else result.stderr
                if output=="":
                    output = "Working on it..."
                out_label = customtkinter.CTkLabel(
                    master=root,
                    text=f"{output}",
                    font=("Arial", 18),
                    text_color="#ffffff",
                    height=430,
                    width=495,
                    corner_radius=13,
                    bg_color="#042a27",
                    fg_color="#ff2e2e",
                    )
                out_label.place(x=60, y=350)
            root.update()
            sleep(5)
            out_label.destroy()
        out_label = customtkinter.CTkLabel(
            master=root,
            text=f"{output}",
            font=("Arial", 18),
            text_color="#ffffff",
            height=430,
            width=495,
            corner_radius=13,
            bg_color="#042a27",
            fg_color="#ff2e2e",
            )
        out_label.place(x=60, y=350)


    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("ask-ai")
    root.geometry("800x850")
    root.configure(bg="#042a27")

    # Set up the input UI
    userinput(root)

    # Start the GUI event loop
    root.mainloop()
