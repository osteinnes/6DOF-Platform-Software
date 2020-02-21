# import the necessary packages
import numpy as np
import argparse
import cv2
from PIL import Image
import imutils


def getHoughCircle(image):
    img = np.asarray(image)

    # load the image, clone it for output, and then convert it to grayscale
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 500)

    print("Cirles: ", circles)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5),
                          (x + 5, y + 5), (0, 128, 255), -1)
        # show the output image
        img = output
        cv2.imwrite("nparray.png", np.hstack([image, output]))
        cv2.imwrite("img.png", img)

    return img


def getContourCircle(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Red color spectrum
    lower = cv2.inRange(hsv, (0, 75, 50), (15, 255, 255))
    upper = cv2.inRange(hsv, (165, 75, 50), (180, 255, 255))
    red = lower + upper

    # Blue color
    blue = cv2.inRange(hsv, (100, 150, 50), (135, 255, 255))
    mask = red + blue

    contours = []

    contours, hierarchy = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #print(contours)

    if len(contours) > 1:
        contour_sizes = [(cv2.contourArea(contour), contour)
                        for contour in contours]
        biggest_contours = sorted(contour_sizes, key=lambda x: x[0], reverse=True)
        #biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        
        biggest_contour = biggest_contours[0][1]
        smallest_contour = biggest_contours[2][1]

        cv2.drawContours(img, smallest_contour, -1, (0, 255, 0), 3)
        cv2.drawContours(img, biggest_contour, -1, (255, 0, 0), 3)

        M = cv2.moments(biggest_contour)
        M2 = cv2.moments(smallest_contour)

        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.circle(img, (cX, cY), 7, (255, 0, 0), -1)
        if M2["m00"] != 0:
            cX = int(M2["m10"] / M2["m00"])
            cY = int(M2["m01"] / M2["m00"])

            cv2.circle(img, (cX, cY), 7, (0, 255, 0), -1)

    return img


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = getContourCircle(cv2.imread(args["image"], cv2.IMREAD_COLOR))

    cv2.imshow('',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
