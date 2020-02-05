from tkinter import *

root = Tk()

root.title("6DOF-Platform")

frame_top = Frame(root)
frame_bot = Frame(root)

frame_top.pack(side=TOP)
frame_bot.pack(side=BOTTOM)

btn_center = Button(frame_top, text="Center")
btn_circle = Button(frame_top, text="Circle")
btn_fig8 = Button(frame_top, text="Figure 8")

btn_center.grid(row=0, column=0)
btn_circle.grid(row=0, column=1)
btn_fig8.grid(row=0, column=2)


root.mainloop()

