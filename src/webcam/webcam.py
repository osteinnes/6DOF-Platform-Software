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
    def get_img(self):
        try:
            check, img = self.cam.read()
            return img
        except Exception as exc:
            print(exc)            
            return None

    # Returns a binary image 
    def get_masked_img(self):
        image = self.get_img()
        result = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array([155,25,0])
        upper = np.array([179,255,255])
        mask = cv2.inRange(image, lower, upper)
        return cv2.bitwise_and(result, result, mask=mask)
        


if __name__ == "__main__":
    cam = webcam()

    for i in range(2):
        img = cam.get_masked_img()
        cv2.imwrite(filename='img' + str(i) + '.jpg', img=img)

    cam.shut_down()