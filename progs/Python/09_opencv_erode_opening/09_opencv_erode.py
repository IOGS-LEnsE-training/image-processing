"""09_opencv_erode file.

File containing a set of instructions to process erosion and dilation operations on an image.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

.. see:: https://geekosophers.com/algorithms

"""

import cv2
import numpy as np

# Main function
if __name__ == "__main__":
    ## Open an image
    image = cv2.imread("../../_data/robot.jpg")
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Display the image
    cv2.imshow('Original Grayscale Image', grayscale_image)
    cv2.waitKey(0)

    ## Kernels
    cross_kernel_9 = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
    cross_kernel_5 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    square_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

    ## Erosion
    eroded_image_cross_9 = cv2.erode(grayscale_image, cross_kernel_9, iterations=1)
    eroded_image_cross_5 = cv2.erode(grayscale_image, cross_kernel_5, iterations=1)
    eroded_image_square = cv2.erode(grayscale_image, square_kernel, iterations=1)

    cv2.imshow("Original Image", grayscale_image)
    cv2.imshow("Cross Kernel Erosion - 9x9", eroded_image_cross_9)
    cv2.imshow("Cross Kernel Erosion - 5x5", eroded_image_cross_5)
    cv2.imshow("Square Kernel Erosion - 9x9", eroded_image_square)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    print(grayscale_image.shape)
    print(eroded_image_cross_9.shape)

