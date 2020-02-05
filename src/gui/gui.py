from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.minsize(600, 400)

root.title("6DOF-Platform")

# Create main deviders
frame_top = Frame(root, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
frame_bot = Frame(root, pady=5, padx=5, highlightbackground="black", highlightthickness=1)

# Pack main deviders
frame_top.pack(side=TOP, pady=5, padx=5)
frame_bot.pack(side=BOTTOM, pady=5, padx=5)

# Create buttons
btn_center = Button(frame_top, text="Center")
btn_circle = Button(frame_top, text="Circle")
btn_fig8 = Button(frame_top, text="Figure 8")

# Pack buttons
btn_center.grid(row=0, column=0, pady=5, padx=5)
btn_circle.grid(row=0, column=1, pady=5, padx=5)
btn_fig8.grid(row=0, column=2, pady=5, padx=5)

print(os.getcwd())

# Add image
img = Image.open('h.jpg')
img = ImageTk.PhotoImage(img)
can = Label(root, image = img)
can.pack(side = "bottom", fill = "both", expand = "yes")


root.mainloop()

