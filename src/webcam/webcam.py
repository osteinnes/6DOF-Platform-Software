import cv2
import numpy as np
import os

# Class for taking and storing picuters
class webcam(object):
    cam = None          # Camera object
    
    # Initialize with a camera index
    def __init__(self):
        self.set_cam()

    # Set camera to the objects camera variable
    def set_cam(self, source=2):
        self.cam = cv2.VideoCapture(source)

    # Release camera and 
    def shut_down(self):
        self.cam.release()
        cv2.destroyAllWindows()

    # Returns an image, if an exception is 
    # raised return None
    def get_img(self, rgb=True):
        img = None
        try:
            check, img = self.cam.read()
            if rgb:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except Exception as exc:
            print(exc)
        
        return img

    # Returns a binary image 
    def get_masked_img(self):
        img = self.get_img(rgb=False)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Red color spectrum
        lower = cv2.inRange(hsv, (0, 75, 50), (15, 255, 255))
        upper = cv2.inRange(hsv, (165, 75, 50), (180, 255, 255))
        red = lower + upper

        # Blue color
        blue = cv2.inRange(hsv, (100, 150, 50), (135, 255, 255))

        mask = red + blue

        img = cv2.bitwise_and(img, img, mask=mask)

        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def snapshot(self, name = "Snapshot"):
        img = self.get_img(rgb=False)
        cv2.imwrite(filename=name + ".jpg", img=img)
        


if __name__ == "__main__":
    cam = webcam()

    for i in range(2):
        img = cam.get_masked_img()
        cv2.imwrite(filename='img' + str(i) + '.jpg', img=img)

    cam.shut_down()