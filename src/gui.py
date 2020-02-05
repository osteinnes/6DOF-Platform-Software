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

    # Variables for the buttons
    btn_center = None
    btn_circle = None
    btn_fig8 = None

    # Camera
    cam = None

    # Image holder
    label = None

    # Setup gui
    def __init__(self):
        self.root = Tk()
        self.create_dividers()
        self.pack_dividers()
        self.create_btns()
        self.pack_btns()
        self.cam = webcam.webcam()
        self.set_image('640x360.png')
        #self.restrict_size()
        self.update()

    # Start gui
    def start(self):
        self.root.mainloop()

    # Set window title
    def set_title(self, title="6DOF-Platform"):
        self.root.title(title)

    # Main dividers divide the gui in several parts
    def create_dividers(self):
        self.frame_left = Frame(self.root, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        self.frame_right = Frame(self.root, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        
    # Pack dividers
    def pack_dividers(self):
        self.frame_right.pack(side=RIGHT, pady=5, padx=5)
        self.frame_left.pack(side=LEFT, pady=5, padx=5)

    # Create buttons
    def create_btns(self):
        self.btn_center = Button(self.frame_right, text="Center")
        self.btn_circle = Button(self.frame_right, text="Circle")
        self.btn_fig8 = Button(self.frame_right, text="Figure 8")

    # Pack buttons
    def pack_btns(self):
        self.btn_center.grid(row=0, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_circle.grid(row=1, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_fig8.grid(row=2, column=0, pady=5, padx=5, sticky='nsew')

    # Restrict minimum size
    def restrict_size(self):
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.maxsize(self.root.winfo_width(), self.root.winfo_height())

    # Set placeholder image
    def set_image(self, img_path):
        img = self.cam.get_img()
        img = ImageTk.PhotoImage(image = Image.fromarray(img))
        self.label = Label(self.frame_left, image = img)
        self.label.image = img
        self.label.pack(fill = "both", expand = "yes")

    def update(self):
        img = self.cam.get_img()
        img = ImageTk.PhotoImage(image = Image.fromarray(img))
        self.label.configure(image=img)
        self.label.image = img
        self.root.after(10, self.update)


if __name__ == "__main__":
    import os
    path = 'C:/Users/eirik/OneDrive/school/Simulation and Visualization/2.semester/simulation_of_closed_loop_systems/platform/6DOF-Platform-Software/src/webcam'
    os.chdir(path)
    gui = gui()
    gui.start()
