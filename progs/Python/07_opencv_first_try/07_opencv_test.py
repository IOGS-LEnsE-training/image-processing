"""07_opencv_test file.

File containing a set of instructions to open and display an image in PNG or JPG format.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np


# Main function
if __name__ == "__main__":

    ## Open an image
    image = cv2.imread("../../_data/robot.pgm")
    print(type(image))
    print(image.shape)

    image_jpg = cv2.imread("../../_data/robot.jpg")
    print(type(image_jpg))
    print(image_jpg.shape)
    
    # Display the image
    cv2.imshow('Image Window', image)
    # Wait for a key press
    cv2.waitKey(0)  # 0 means wait indefinitely

    
    ## Generate a random image
    height, width, channels = 256, 512, 3
    # Generate random pixel values in the range [0, 255] for an RGB image
    random_image = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
    # Display the image
    cv2.imshow('Random Image Window', random_image)
    # Wait for a key press
    cv2.waitKey(0)  # 0 means wait indefinitely

    # Save the image using OpenCV
    output_filename = 'random_image.png'
    cv2.imwrite(output_filename, random_image)

    ## Access to a part of an image
    image_crop = image[200:350,300:500,:]
    print(image_crop.shape)
    # Display the image
    cv2.imshow('Crop Image Window', image_crop)
    # Wait for a key press
    cv2.waitKey(0)  # 0 means wait indefinitely   
    
    ## Convert to grayscale
    grayscale_image = cv2.cvtColor(image_jpg, cv2.COLOR_BGR2GRAY)
    print(grayscale_image.shape)
    # Display the image
    cv2.imshow('Crop Image Window', grayscale_image)
    # Wait for a key press
    cv2.waitKey(0)  # 0 means wait indefinitely   

    ## Binarize an image
    retval, binary_image = cv2.threshold(grayscale_image, 63,
                                         255, cv2.THRESH_BINARY)
    # Display the image
    cv2.imshow('Binary Image Window', binary_image)
    # Wait for a key press
    cv2.waitKey(0)  # 0 means wait indefinitely

    # Close the window
    cv2.destroyAllWindows()
    
