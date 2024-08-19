"""08_opencv_mean file.

File containing a set of instructions to process a blur (or mean) filter on an image.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

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
    
    ## Apply Gaussian blur
    # Parameters: (source image, kernel size, standard deviation in X direction)
    kernel_size = (15, 15)  # Kernel size (must be odd numbers)
    blurred_image15 = cv2.GaussianBlur(grayscale_image, kernel_size, 0)
    kernel_size = (3, 3)  # Kernel size (must be odd numbers)
    blurred_image3 = cv2.GaussianBlur(grayscale_image, kernel_size, 0)
    # Display the blurred image
    cv2.imshow('Gaussian Blurred Image - 15', blurred_image15)
    cv2.imshow('Gaussian Blurred Image - 3', blurred_image3)
    cv2.waitKey(0)
    
    ## Execution time comparison
    import timeit
    kernel_size = (15, 15)  
    # Blur on a grayscale image
    def grayscale_process():
        blurred_image15g = cv2.GaussianBlur(grayscale_image, kernel_size, 0)
    # Blur on a RGB image
    def rgb_process():
        blurred_image15g = cv2.GaussianBlur(image, kernel_size, 0)


    # Measure execution times
    time_gray = timeit.timeit(grayscale_process, number=10)
    time_rgb = timeit.timeit(rgb_process, number=10)

    print(f"Execution time for Grayscale: {time_gray / 10:.6f} seconds")
    print(f"Execution time for RGB: {time_rgb / 10:.6f} seconds")
    
    cv2.destroyAllWindows()
    

