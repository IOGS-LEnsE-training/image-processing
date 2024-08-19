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
    

'''
int main(int argc, char** argv) {
	
	std::cout << "Test OpenCV" << std::endl;
	
	// Time measurement
	std::chrono::duration<double, std::milli> duration;
	std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	
	
	// Open an image
	start = std::chrono::high_resolution_clock::now();	// time starts
	cv::Mat image = cv::imread("../../../_data/robot.pgm"); 
	end = std::chrono::high_resolution_clock::now();	// time stops
	duration = end - start;
    std::cout << "Execution time of read image: " << duration.count() << " milliseconds" << std::endl;
	
	// Display in a window
	std::string windowName = "Robot from LEnsE"; //Name of the window
	cv::namedWindow(windowName); // Create a window
	cv::imshow(windowName, image); // Show our image inside the created window.
	cv::waitKey(0); // Wait for any keystroke in the window
	cv::destroyWindow(windowName); //destroy the created window
	
	// Access to informations about the image
	cv::Size size = image.size();	
	std::cout << "W,H = " << size.height << "," << size.width << std::endl;
	std::cout << "Channels = " << image.channels() << std::endl;
	std::cout << "Depth = " << image.depth() << std::endl;
	std::cout << "Type = " << image.type() << std::endl;
	
	// Write an image in PGM
	cv::Mat grayImage;
	cv::cvtColor(image, grayImage, cv::COLOR_BGR2GRAY);
	cv::imwrite("robot2.pgm", grayImage);

	return 0;
}
'''

