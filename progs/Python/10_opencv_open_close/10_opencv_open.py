"""10_opencv_open file.

File containing a set of instructions to process opening and closing operations on an image.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

.. see:: https://geekosophers.com/algorithms

"""

import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt


# Main function
if __name__ == "__main__":
    ## Open an image
    image = cv2.imread("../../_data/robot.jpg")
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Optionally, apply a threshold to create a binary image
    _, binary_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)

    # Define a kernel (a 3x3 square kernel in this case)
    kernel = np.ones((9, 9), np.uint8)

    # Apply the opening operation
    opening = cv2.morphologyEx(grayscale_image, cv2.MORPH_OPEN, kernel)
    # Apply the closing operation
    closing = cv2.morphologyEx(grayscale_image, cv2.MORPH_CLOSE, kernel)

    # Display the result
    cv2.imshow('Original Image', grayscale_image)
    cv2.imshow('Opening Result', opening)
    cv2.imshow('Closing Result', closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ############################
    ## Effect of opening and closing
    image2 = cv2.imread("../../_data/forms_opening_closing.png")
    grayscale_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    _, binary_image2 = cv2.threshold(grayscale_image2, 127, 255, cv2.THRESH_BINARY)
    binary_image_normalized = binary_image2 // 255


    kernel = np.ones((9,9), np.uint8)
    # Closing / Opening
    opening = cv2.morphologyEx(binary_image_normalized, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary_image_normalized, cv2.MORPH_CLOSE, kernel)

    # Display the result
    cv2.imshow('Original Image', binary_image_normalized*255)
    cv2.imshow('Opening Result', opening*255)
    cv2.imshow('Closing Result', closing*255)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


