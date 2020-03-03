from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2

from webcam import webcam, ball_tracking


class gui(object):
    # Root gui window
    root = None

    # Variables for the dividers
    frame_left = None
    frame_right = None
    frame_right_top = None
    frame_right_center = None
    frame_right_bot = None

    # Variables for the buttons
    select_cam = None
    variable = None

    btn_center = None
    btn_circle = None
    btn_fig8 = None

    btn_normal = None
    btn_masked = None
    btn_snapshot = None

    # Camera
    cam = None
    cams = None

    # Image holder
    label = None

    # Holds current get image method
    get_img = None

    # Setup gui
    def __init__(self):
        self.cam = webcam.webcam()
        self.get_img = self.cam.get_img

        self.root = Tk()
        self.root.title("6DOF-Platform 3000")
        self.create_dividers()
        self.pack_dividers()
        self.create_btns()
        self.pack_btns()
        self.set_image()
        self.restrict_size()
        self.update()

    # Start gui
    def start(self):
        self.root.mainloop()

    # Main dividers divide the gui in several parts
    def create_dividers(self):
        self.frame_left = Frame(self.root, pady=5, padx=5,
                                highlightbackground="black", highlightthickness=1)
        self.frame_right = Frame(self.root)
        self.frame_right_top = Frame(
            self.frame_right, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        self.frame_right_top.columnconfigure(0, weight=1)
        self.frame_right_center = Frame(
            self.frame_right, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        self.frame_right_center.columnconfigure(0, weight=1)
        self.frame_right_bot = Frame(
            self.frame_right, pady=5, padx=5, highlightbackground="black", highlightthickness=1)
        self.frame_right_bot.columnconfigure(0, weight=1)

    # Pack dividers
    def pack_dividers(self):
        self.frame_right.pack(side=RIGHT, pady=5, padx=5)
        self.frame_left.pack(side=LEFT, pady=5, padx=5)
        self.frame_right_top.pack(side=TOP, pady=5, padx=5, fill=X)
        self.frame_right_center.pack(pady=5, padx=5, fill=X)
        self.frame_right_bot.pack(side=BOTTOM, pady=5, padx=5, fill=X)

    # Create buttons
    def create_btns(self):
        self.btn_center = Button(self.frame_right_bot,
                                 text="Center", command=self.set_mode_center)
        self.btn_circle = Button(self.frame_right_bot,
                                 text="Circle", command=self.set_mode_circle)
        self.btn_fig8 = Button(self.frame_right_bot,
                               text="Figure 8", command=self.set_mode_figure8)

        self.btn_normal = Button(
            self.frame_right_center, text="Normal", command=self.set_img_mode_normal)
        self.btn_masked = Button(
            self.frame_right_center, text="Masked", command=self.set_img_mode_masked)
        self.btn_snapshot = Button(
            self.frame_right_center, text="Snapshot", command=self.cam.snapshot)

        self.set_cam("initial cam: 0")      # This string will never appear in gui, must end with " 0"(space + zero)
        self.select_cam = OptionMenu(
            self.frame_right_top, self.variable, *self.cams, command=self.set_cam)
        self.select_cam.config(indicatoron=0)

    # Pack buttons
    def pack_btns(self):
        self.btn_center.grid(row=0, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_circle.grid(row=1, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_fig8.grid(row=2, column=0, pady=5, padx=5, sticky='nsew')

        self.btn_snapshot.grid(row=0, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_masked.grid(row=1, column=0, pady=5, padx=5, sticky='nsew')
        self.btn_normal.grid(row=2, column=0, pady=5, padx=5, sticky='nsew')

        self.select_cam.grid(row=0, column=0, pady=5, padx=5, sticky=(N,S,E,W))

    def set_cam(self, n):        
        self.cams = self.cam.get_cams()
        self.cams = ["Camera " + str(cam) for cam in self.cams]
        if not self.variable:
            self.variable = StringVar(self.root)
        self.variable.set(self.cams[0])
        cam_index = int(n.split()[-1])
        self.cam.set_cam(cam_index)

    # Restrict minimum size
    def restrict_size(self):
        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.maxsize(self.root.winfo_width(), self.root.winfo_height())

    # Set placeholder image
    def set_image(self):
        img = self.cam.get_masked_img()
        img = ImageTk.PhotoImage(image=Image.fromarray(img))
        self.label = Label(self.frame_left, image=img)
        self.label.image = img
        self.label.pack(fill="both", expand="yes")

    # Callback function to get and update image
    def update(self):
        frame = self.get_img()
        #img = frame.copy()

        img = None

        img = ball_tracking.getContourCircle(frame)

        img = ImageTk.PhotoImage(image=Image.fromarray(img))
        self.label.configure(image=img)
        self.label.image = img
        self.root.after(1, self.update)

    # Switches the image mode between masked and normal
    def set_img_mode_normal(self):
        self.get_img = self.cam.get_img

    def set_img_mode_masked(self):
        self.get_img = self.cam.get_masked_img

    # Set different modes
    def set_mode_center(self):
        print("mode: center")

    def set_mode_circle(self):
        print("mode: circle")

    def set_mode_figure8(self):
        print("mode: figure 8")


if __name__ == "__main__":
    gui = gui()
    gui.start()
