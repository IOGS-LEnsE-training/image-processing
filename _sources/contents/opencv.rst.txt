OpenCV: Basics
##############

A powerful set of tools for image processing



* :file:`07_opencv_first_try` : introducing OpenCV, open and display an image.
* :file:`08_opencv_mean_filters` : convolution with a specific kernel.
* :file:`09_opencv_erode_opening` : erosion, dilatation, opening and closing on image.


Install opencv
**************

Install for Python
==================

To install OpenCV for Python, you can use the package manager :code:`pip`.

.. code-block:: bash

	pip install opencv-python

Install for C++
===============

Soon...

Using Python 
************

.. note::

    The code of this example is in the :file:`\\progs\\Python\\07_opencv_first_try\\07_opencv_test.py` file of the repository.

    Examples of images are stored in :file:`\\_data\\` directory of the repository.

Import opencv
=============

To import OpenCV in your Python scripts, you can use this instruction:

.. code-block:: python

	import cv2
	
To display the version of OpenCV that is installed (and verify its good installation...), you can use this instruction: 

.. code-block:: python

	print(cv2.__version__)

Open an image
=============

The :code:`imread` function of OpenCV reads an image from a specified file path. A lot of different formats can be opened (JPG, PNG...).

.. code-block:: python

	image = cv2.imread('path/to/your/image.jpg')

Replace 'path/to/your/image.jpg' with the actual path to your image file.

>>> image = cv2.imread("../../_data/robot.pgm")

The data from the file are stored in a :code:`numpy.ndarray` object, as showed by the next instruction:

>>> print(type(image))
<class 'numpy.ndarray'>

You can also access to the size of the image (or shape) by the next instruction:

>>> print(image.shape)
(382, 600, 3)

The firt value is the height, the second one the width and the third one is the number of channels.

.. note::

	Even if the image is stored in a grayscale format, the :code:`imread` function of OpenCV create a 3 channels image (R, G, B). In the case of a grayscale format, the 3 channels are exactly the same.


Display an image
================

OpenCV uses different graphic backends to display images, depending on the operating system and how OpenCV was compiled. The most common graphic packages or libraries that OpenCV relies on to display images using the cv2.imshow() function include: GTK (GIMP Toolkit), Qt, Win32 API, Cocoa (on macOS).

To display an image, you can use the :code:`imshow` function of OpenCV as described below:

.. code-block:: python

	cv2.imshow('Image Window', image)
	
The first parameter is the name of the window that will display the image. The second parameter is the :code:`numpy.ndarray` containing the image.

.. warning::
	
	The :code:`imshow` function doesn't pause or block the execution of your script. To keep the window opened, a blocking function is required.
	
To maintain the display of the image, you can use the :code:`waitKey` function of OpenCV as mentionned below:

.. code-block:: python

	cv2.waitKey(0)  # 0 means wait indefinitely
	
To close the window, you need to click on the top-right cross of the window, or press any key of the keyboard.

At the end of your script, to be sure that each OpenCV window is closed, you can use this instruction:

.. code-block:: python
	
	cv2.destroyAllWindows()


Save an image
=============

It is also possible to save a :code:`numpy.ndarray` object (containing data of an image) in a specific file with the :code:`imwrite` function of OpenCV.

The next code, for example, permits to generate a random image (with Numpy random function) and to store it into a specific file.

.. code-block:: python

    # Generate a random image
    height, width, channels = 256, 512, 3
    # Generate random pixel values in the range [0, 255] for an RGB image
    random_image = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)

    # Save the image using OpenCV
    output_filename = 'random_image.png'
    cv2.imwrite(output_filename, random_image)

The :code:`imwrite` function needs two parameters: the path to the file to save the data and the :code:`numpy.ndarray` object containing the data.


Images as arrays
****************

As mentionned in the :ref:`digital-image` section, a digital raster image is a 2- or 3-D array, depending on the color space used and how the pixel information is stored. One of the most efficient method to store data from a digital image is to use :code:`numpy.ndarray`. OpenCV is based on this principle (as we could see in the previous part).


Access to a part of an image
============================

It is possible to access to a part of an image by using the properties of :code:`numpy.ndarray`. This process is called: **cropping an image**. This means extracting a rectangular portion from the original image.

To extract a part of an image from a first point of coordinates (x1, y1) to a second point of coordinates (x2, y2), you can follow this instruction:

.. code-block:: python

    image_crop = image[y1:y2,x1:x2,:]

To obtain the shape of the new cropped image, you can use:

.. code-block:: python

    print(image_crop.shape)
	
|

.. figure:: ../_static/images/images_crop_numpy.png
   :align: center
   :scale: 80%

   Example of image cropping: on the left the original image, on the right the cropped image around the robot wheel.
   
For this example, we used the following code:

.. code-block:: python

    image = cv2.imread("../../_data/robot.pgm")
	image_crop = image[200:350,300:500,:]


Convert an image to grayscale format
====================================

Converting an image to grayscale is a common and useful step in image processing and computer vision to **simplify computation**. Grayscale images have only one channel (intensity), instead of three (RGB) in color images. Operations such as filtering, edge detection, and thresholding can be performed more quickly on grayscale images due to the reduced amount of data.


To convert an image to grayscale using OpenCV in Python, you can use the :code:`cvtColor` function. This function is designed to convert images between different color spaces, including converting a color image to grayscale:

.. code-block:: python

	grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
If you check the shape of the resulting image, it has only one channel.

>>> print(grayscale_image.shape)
(382, 600)

Binarize an image
=================

Binarization is a fundamental image processing technique with various
applications across multiple fields: optical character recognition (OCR),
barcode and QR Code Detection, fingerprint recognition
art and Image Stylization...

Binarization simplifies image data by reducing it to its most basic form, making it easier for various algorithms to process, analyze, and extract meaningful information.

The :code:`threshold` function of OpenCV allows to perform a binarization of a grayscale image.

You can set a threshold value (e.g., 127) and a maximum value (e.g., 255).

.. code-block:: python

    retval, binary_image = cv2.threshold(grayscale_image, threshold,
                                         max_value, cv2.THRESH_BINARY)

This function returns two values:
 - *retval*: The threshold value used
 - *binary_image*: The binarized image

.. figure:: ../_static/images/images_threshold.png
   :align: center

   Example of image binarization.

Besides *THRESH_BINARY*, OpenCV offers other thresholding methods:

- *THRESH_BINARY_INV*: Inverted binary thresholding
- *THRESH_TRUNC*: Truncates pixel values above the threshold
- *THRESH_TOZERO*: Sets pixels below the threshold to zero
- *THRESH_TOZERO_INV*: Sets pixels above the threshold to zero.