from tkinter import *
from PIL import Image, ImageTk

from webcam import webcam

import tkinter.ttk as ttk


class gui(object):
    # Root gui window
    root = None

    # Variables for the dividers
    frame_left = None
    frame_right = None
    frame_right_top = None
    frame_right_bot = None

    # Variables for the buttons
    btn_center = None
    btn_circle = None
    btn_fig8 = None
    btn_normal = None
    btn_masked = None

    # Camera
    cam = None

    # Image holder
    label = None

    # Holds current get image method
    get_img = None

    # Setup gui
    def __init__(self):
        self.cam = webcam.webcam()
        self.get_img = self.cam.get_img

        self.root = Tk()
        self.root.title("6DOF-Platform")
        self.create_dividers()
        self.pack_dividers()
        self.create_btns()
        self.pack_btns()
        self.set_image('640x360.png')
        self.restrict_size()
        self.update()

    # Start gui
    def start(self):
        self.root.mainloop()

    # Main dividers divide the gui in several parts
    def create_dividers(self):
        self.frame_left = Frame(self.root, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        self.frame_right = Frame(self.root)
        self.frame_right_top = Frame(self.frame_right, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        self.frame_right_bot = Frame(self.frame_right, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        
    # Pack dividers
    def pack_dividers(self):
        self.frame_right.pack(side=RIGHT, pady=5, padx=5)
        self.frame_left.pack(side=LEFT, pady=5, padx=5)
        self.frame_right_top.pack(side=TOP, pady=5, padx=5, fill=X)
        self.frame_right_bot.pack(side=BOTTOM, pady=5, padx=5, fill=X)

    # Create buttons
    def create_btns(self):
        self.btn_center = Button(self.frame_right_bot, text="Center")
        self.btn_circle = Button(self.frame_right_bot, text="Circle")
        self.btn_fig8 = Button(self.frame_right_bot, text="Figure 8")

        self.btn_normal = Button(self.frame_right_top, text="Normal", command=self.set_img_mode)
        self.btn_masked = Button(self.frame_right_top, text="Masked", command=self.set_img_mode)

    # Pack buttons
    def pack_btns(self):
        self.btn_center.grid(row=0, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_circle.grid(row=1, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_fig8.grid(row=2, column=0, pady=5, padx=5, sticky='nsew')

        self.btn_masked.grid(row=1, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_normal.grid(row=0, column=0, pady=5, padx=5, sticky='nsew')

    # Restrict minimum size
    def restrict_size(self):
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.maxsize(self.root.winfo_width(), self.root.winfo_height())

    # Set placeholder image
    def set_image(self, img_path):
        img = self.cam.get_masked_img()
        img = ImageTk.PhotoImage(image = Image.fromarray(img))
        self.label = Label(self.frame_left, image = img)
        self.label.image = img
        self.label.pack(fill = "both", expand = "yes")

    # Callback function to get and update image
    def update(self):
        img = self.get_img()
        img = ImageTk.PhotoImage(image = Image.fromarray(img))
        self.label.configure(image=img)
        self.label.image = img
        self.root.after(1, self.update)

    # Switches the image mode between masked and normal
    def set_img_mode(self):
        if self.get_img == self.cam.get_img:
            self.get_img = self.cam.get_masked_img
        else:
            self.get_img = self.cam.get_img




if __name__ == "__main__":
    import os
    path = 'C:/Users/eirik/OneDrive/school/Simulation and Visualization/2.semester/simulation_of_closed_loop_systems/platform/6DOF-Platform-Software/src/webcam'
    os.chdir(path)
    gui = gui()
    gui.start()
