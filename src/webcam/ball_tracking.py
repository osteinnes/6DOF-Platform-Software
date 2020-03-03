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


def getContourCircle(img, mask_type):

    mask = generateMask(img, mask_type)

    # Find contours
    contours, hierarchy = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        sorted_contours = doSortContours(contours)
        
        # Retrieve relevant contours
        biggest_contour = sorted_contours[0][1]

        if mask_type == "white":
            # Draw contours on image
            cv2.drawContours(img, biggest_contour, -1, (255, 0, 0), 3)

            # Find and draw centre of contours
            img = drawContourCenter(biggest_contour, img, (255, 0, 0))

            # Retrieve coordinates of center and print them
            x,y = getContourCenter(biggest_contour)
            print("Center of ball>> x:", x, " y: ", y)
        elif mask_type == "red":
            # Draw contours on image
            cv2.drawContours(img, biggest_contour, -1, (0, 255, 0), 3)

            # Find and draw centre of contours
            img = drawContourCenter(biggest_contour, img, (0, 255, 0))
        elif mask_type == "blue":
            # Draw contours on image
            cv2.drawContours(img, biggest_contour, -1, (0, 0, 255), 3)

            # Find and draw centre of contours
            img = drawContourCenter(biggest_contour, img, (0, 0, 255))

    # Return image with contours and centers drawn (if any)
    return img

# Draws center of a contour
def drawContourCenter(contour, img, color):

    # Weighted average of image pixel intesities to find centroid of contour (blob)
    M = cv2.moments(contour)

    # Check if segmentation were successful
    if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.circle(img, (cX, cY), 7, color, -1)
    return img

# Returns center coordinates of a contour
def getContourCenter(contour):

    # Weighted average of image pixel intesities to find centroid of contour (blob)
    M = cv2.moments(contour)

    # Initialize coordinates
    cX = None
    cY = None

    # Check if segmentation were successful
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    # Return coordinates
    return cX, cY

def generateMask(img, mask_type):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Red color spectrum
    if mask_type == "red":        
        lower = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
        upper = cv2.inRange(hsv, (170, 50, 50), (180, 255, 255))
        mask = lower + upper
    elif mask_type == "blue":
        # Blue color
        mask = cv2.inRange(hsv, (100, 150, 50), (135, 255, 255))
    elif mask_type == "white":
        mask = cv2.inRange(hsv, (0,0,0), (0,0,255))
    return mask



def doSortContours(contours):
    # Sort contours by area (decending)
    contour_sizes = [(cv2.contourArea(contour), contour)
                    for contour in contours]
    contours_array = sorted(contour_sizes, key=lambda x: x[0], reverse=True)

    return contours_array



if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = getContourCircle(cv2.imread(args["image"], cv2.IMREAD_COLOR), "blue")

    cv2.imshow('',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
