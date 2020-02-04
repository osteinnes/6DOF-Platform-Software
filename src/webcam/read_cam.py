import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
print(webcam)
try:
    check, img = webcam.read()
except:
    print("Cant read webcam")

try:
    cv2.imwrite(filename='saved_img.jpg', img=img)
except:
    print("Cant save")

h, w, d = len(img), len(img[0]), len(img[0][0])
print("Height:", h, "Width:", w, "Dim:", d)

webcam.release()            # Realese webcamera
cv2.destroyAllWindows()