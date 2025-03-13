# libraries Import
from tkinter import *
import customtkinter

# Main root Properties

root = Tk()
root.title("ask-ai")
root.geometry("800x350")
root.configure(bg="#042a27")

def rem_label():
    print("Destroying...")
    Label_id3.destroy()


Button_id1 = customtkinter.CTkButton(
    master=root,
    text="SEND",
    font=("undefined", 18),
    text_color="#000000",
    hover_color="#fe0101",
    height=30,
    width=95,
    border_width=2,
    corner_radius=16,
    border_color="#ffffff",
    bg_color="#042a27",
    fg_color="#ff00dd",
    )
Button_id1.place(x=600, y=80)
Label_id3 = customtkinter.CTkLabel(
    master=root,
    text="                  Output...",
    font=("Arial", 18),
    text_color="#ffffff",
    height=130,
    width=495,
    corner_radius=13,
    bg_color="#042a27",
    fg_color="#ff2e2e",
    )
Label_id3.place(x=60, y=190)
Entry_id2 = customtkinter.CTkEntry(
    master=root,
    placeholder_text="                          Inserisci comando",
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
Entry_id2.place(x=70, y=50)
Button_id4 = customtkinter.CTkButton(
    master=root,
    text="RUN",
    font=("undefined", 18),
    text_color="#000000",
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=16,
    border_color="#ffffff",
    bg_color="#042a27",
    fg_color="#ff00dd",
    command=rem_label
    )
Button_id4.place(x=600, y=230)



#run the main loop
root.mainloop()