"""07_opencv_histo file.

File containing a set of instructions to display a histogram.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_histo(image):
    # Calculate the histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    print(type(histogram))
    print(histogram.shape)

    # Plot the histogram
    plt.figure()
    
    plt.subplot(2, 1, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Image / Histogram")
    
    plt.subplot(2, 1, 2)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    # Create a range of values (0 to 255) for the x-axis
    x = np.arange(256)

    # Plot the histogram as bars
    plt.bar(x, histogram[:,0], width=1, color='black')  # width=1 to make bars narrow and represent each intensity

    plt.xlim([0, 256])  # Limits for the x-axis


# Main function
if __name__ == "__main__":

    # Open an image
    image = cv2.imread("../../_data/robot.jpg", cv2.IMREAD_GRAYSCALE)
    
    display_histo(image)
    
    
    ## Low contrast
    alpha = 0.6
    beta = 0
    image_low = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    display_histo(image_low)

    
    ## High contrast
    alpha = 1.4
    beta = 0
    image_high = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    display_histo(image_high)
    
    ## Other representation of an histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    plt.figure()
    plt.title("Grayscale Image Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.plot(histogram)
    plt.xlim([0, 256])  # Limits for the x-axis
    plt.show()
