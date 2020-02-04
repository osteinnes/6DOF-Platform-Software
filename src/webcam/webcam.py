import cv2

# Class for taking and storing picuters
class webcam(object):
    cam = None          # Camera object
    
    # Initialize with a camera index
    def __init__(self, camera_index = 0):
        self.set_cam(camera_index)

    # Set camera to the objects camera variable
    def set_cam(self, index):
        self.cam = cv2.VideoCapture(0)

    # Release camera and 
    def shut_down(self):
        self.cam.release()
        cv2.destroyAllWindows()

    # Returns an image, if an exception is 
    # raised return None
    def get_img(self):
        try:
            check, img = self.webcam.read()
            return img
        except Exception as exc:
            print(exc)            
            return None

if __name__ == "__main__":
    cam = webcam()
    img = cam.get_img()
    cam.shut_down()
    print(img)
    #cv2.imwrite(filename='img.jpg', img=img)