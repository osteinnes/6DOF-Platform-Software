from tkinter import *
from PIL import Image, ImageTk

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

    # Video source
    vid = None

    # Setup gui
    def __init__(self):
        self.root = Tk()
        self.create_dividers()
        self.pack_dividers()
        self.create_btns()
        self.pack_btns()
        self.set_image('640x360.png')
        self.restrict_size()

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
        img = ImageTk.PhotoImage(Image.open(img_path))
        label = Label(self.frame_left, image = img)
        label.image = img
        label.pack(fill = "both", expand = "yes")


if __name__ == "__main__":
    gui = gui()
    gui.start()
