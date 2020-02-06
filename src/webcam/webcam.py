import cv2
import numpy as np

# Class for taking and storing picuters
class webcam(object):
    cam = None          # Camera object
    
    # Initialize with a camera index
    def __init__(self):
        self.set_cam()

    # Set camera to the objects camera variable
    def set_cam(self, source=0):
        self.cam = cv2.VideoCapture(source)

    # Release camera and 
    def shut_down(self):
        self.cam.release()
        cv2.destroyAllWindows()

    # Returns an image, if an exception is 
    # raised return None
    def get_img(self):
        try:
            check, img = self.cam.read()
            return img
        except Exception as exc:
            print(exc)            
            return None

    # Returns a binary image 
    def get_masked_img(self):
        img = self.get_img()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Lower range
        l = np.array([0, 120, 70])
        u = np.array([10, 255, 255])
        mask_l = cv2.inRange(img, l, u)

        # Upper range
        l = np.array([170, 120, 70])
        u = np.array([180, 255, 255])
        mask_u = cv2.inRange(img, l, u)

        mask = mask_l + mask_u

        return cv2.bitwise_and(img, img, mask=mask)

if __name__ == "__main__":
    cam = webcam()

    for i in range(2):
        img = cam.get_masked_img()
        cv2.imwrite(filename='img' + str(i) + '.jpg', img=img)

    cam.shut_down()