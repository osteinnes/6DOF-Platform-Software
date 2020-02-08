import cv2
import numpy as np

# Class for taking and storing picuters
class webcam(object):
    cam = None          # Camera object
    
    # Initialize with a camera index
    def __init__(self):
        self.set_cam()

    # Set camera to the objects camera variable
    def set_cam(self, source=1):
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

        # H = (0 - 10), s = (20 - 255), v = (50 - 255)
        mask1 = cv2.inRange(hsv, (0, 150, 50), (10, 255, 255))

        # H = (170 - 180), s = (200 - 255), v = (50 - 255)
        mask2 = cv2.inRange(hsv, (170, 150, 50), (180, 255, 255))

        mask = mask1 + mask2

        img = cv2.bitwise_and(img, img, mask=mask)

        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        


if __name__ == "__main__":
    cam = webcam()

    for i in range(2):
        img = cam.get_masked_img()
        cv2.imwrite(filename='img' + str(i) + '.jpg', img=img)

    cam.shut_down()