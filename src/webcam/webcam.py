import cv2

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

if __name__ == "__main__":
    cam = webcam()

    for i in range(2):
        img = cam.get_img()
        cv2.imwrite(filename='img' + str(i) + '.jpg', img=img)

    cam.shut_down()