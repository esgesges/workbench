import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x400")

# Open your image
image = Image.open("/home/emrys/Documents/workbench/code/desktopUI/0above-the-mountains.png")
photo = ImageTk.PhotoImage(image)

# Create a Label with the image
background_label = tk.Label(root, image=photo)
background_label.place(relx=0.5, rely=0.5, anchor="center")

# Add text over the image (transparency effect)
userLabel = tk.Label(root, text="Username:", font=("Arial", 16), fg="white", bg="black")
userLabel.place(relx=0.5, rely=0.4, anchor="center")

root.mainloop()
