Python and images
#################

There are lots of libraries or modules to open and process images with Python. We can mention: **PIL** (Python Imaging Library or Pillow), **OpenCV** (Open Source Computer Vision Library), scikit-image...

Before using one of the most popular, *OpenCV*, we will go back to the **basics** of most principles used by these modules to process images.

To understand the fundamentals, we will use :abbr:`PGM (Portable Gray Map)` and :abbr:`PPM (Portable Pixmap)` images.

PGM and PPM files formats
*************************

:abbr:`PGM (Portable Gray Map)` and :abbr:`PPM (Portable Pixmap)` files formats are types of files used to store grayscale or RGB images. Their particularity is that they store data in a **plain text format**, making them easy to read and write.

*A binary format also exists for more efficient storage.*

PGM files can represent images with various levels of gray, from black to white.

PPM files support both grayscale and color images, with color images typically represented using RGB (Red, Green, Blue) color channels.

.. note::

    Some file formats are much more commonly used (:abbr:`JPG (Joint Photographic Experts Group)` or :abbr:`PNG (Portable Network Graphics)`), especially for data compression, making files lighter to store.

    Structures of that kind of files are more complex and data need to be decompressed. But the basics are the same as PGM or PPM files.

Structure of a PGM file
=======================

The structure of a PGM file consists of a **header section** followed by the **image data section**. Here is a breakdown of the structure:

* **Header Section**: The header section contains metadata about the image, including:

    * Magic Number: Indicates the file type. For PGM files, this is typically "P2" for ASCII-encoded files or "P5" for binary-encoded files.
    * Width and Height: Specifies the dimensions of the image in pixels.
    * Maximum Gray Value: Indicates the maximum intensity value for grayscale pixels (usually 255).

* **Image Data Section**: The image data section contains the pixel values that represent the grayscale intensities of the image.

Here's an example of the structure of an ASCII-encoded PGM file:

.. code-block:: bash

    P2
    # This is a comment
    3 2
    255
    0 0 0   # Pixel values for the first row
    255 255 255   # Pixel values for the second row

In this example, the first line is the **magic number**, followed by comments (which start with the "#" character) and **metadata** (width, height, and maximum gray value).

The image data section contains the pixel values that represent the grayscale intensities of the image.

Structure of a PPM file
=======================

The structure of a PPM file is the same as a PGM file. It consists of a **header section** followed by the **image data section**. Here is a breakdown of the structure:

* **Header Section**: The header section contains metadata about the image, including:

    * Magic Number: Indicates the file type. For PGM files, this is typically "P3" for ASCII-encoded files or "P6" for binary-encoded files.
    * Width and Height: Specifies the dimensions of the image in pixels.
    * Maximum Gray Value: Indicates the maximum intensity value for grayscale pixels (usually 255).

* **Image Data Section**: The image data section contains a set of three values that represent respectively the red, the gree, and the blue intensities of the image.

Here's an example of the structure of an ASCII-encoded PPM file:

.. code-block:: bash

    P3
    # This is a comment
    3 2
    255
    0 0 0 0 1 0 1 1 0   # Pixel values for the first row
    255 0 0 0 255 0 0 0 255   # Pixel values for the second row

Read a PGM file - list
**********************

.. note::

    The codes of this example is in the :file:`\\progs\\Python\\00_open_a_PGM_file\\` directory of the repository.

    Examples of images are stored in :file:`\\_data\\` directory of the repository.
	
	The main file of the Python script is :file:`00_open_PGM_file_list.py`

Function to read a PGM file
===========================

As described previously, a PGM file in **plain text format** can be opened like a classical ASCII text file. The path to the file must be given to the function.

.. code-block:: python
    :linenos:

    def read_image_PGM(filename: str) -> list:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                magic_number = lines[0].strip()
                width, height = map(int, lines[1].split())
                max_gray_value = int(lines[2])
                print(f'PGM File\nMagic Number={magic_number}')
                print(f'W={width} / H={height} / Maximum Gray Value={max_gray_value}')
                pixels = [[int(value) for value in line.split()] for line in lines[3:]]
                return pixels
        except FileNotFoundError:
            print(f"Error: Unable to open file {filename}")

In the third line of this example, the file is opened with native Python function :code:`open`, in reading mode (*'r'*).

At the line 4, each line of the file is read and stored in the :code:`lines` list. As mentioned in the *Structure of a PGM file* section, first lines contain metadata of the image.

Then, the last lines contain pixels information. They are stored in a new list (called :code:`pixels`).

Opening an image
----------------

You can try this function with the next command, in a *command shell*:

>>> image = read_image_PGM("../../_data/robot.pgm")
PGM File
Magic Number=P2
W=600 / H=382 / Maximum Gray Value=255

The :file:`robot.pgm` file contains an image of 600 x 382 pixels.

The type of the returned object is a Python :code:`list`.

>>> print(type(image))
<class 'list'>

Accessing to a pixel value
==========================

The function we defined returns a list of integers. In this example, the length of the list :code:`image` is 600 by 382 pixels.

To access to the value of the 58th pixel, you can use the following command:

>>> print(image[58])
[211]

But if you want to access to the 96th pixel of the 50th row (each row has 600 pixels), you need to use the following command:

>>> print(image[50 * 600 + 96])
[190]

Read a PGM file - array
***********************

.. note::

    The codes of this example is in the :file:`\\progs\\Python\\00_open_a_PGM_file\\` directory of the repository.

    Examples of images are stored in :file:`\\_data\\` directory of the repository.
	
	The main file of the Python script is :file:`00_open_PGM_file_array.py`

Function to read a PGM file
===========================

As described previously, a PGM file in **plain text format** can be opened like a classical ASCII text file. The path to the file must be given to the function. This function is nearly the same as previously.

.. code-block:: python
    :linenos:

	def read_image_PGM(filename: str) -> list:

		try:
			with open(filename, 'r') as f:
				# Read the magic number of the file
				magic_number = f.readline().strip()
				if magic_number != 'P2':
					raise ValueError("Invalid PGM file format")
							
				# Read the width, height, and maximum gray value
				width, height = map(int, f.readline().split())
				max_gray_value = int(f.readline())
				print(f'PGM File\nMagic Number={magic_number}')
				print(f'W={width} / H={height} / Maximum Gray Value={max_gray_value}')
				
				# Read each pixel value
				pixels = []
				for line in f:
					pixels.extend(line.split())
				
				# Convert the image data to a NumPy array
				image = np.array(pixels, dtype=int).reshape((height, width))
				return image
		except FileNotFoundError:
			print(f"Error: Unable to open file {filename}")


Then, the last lines contain pixels information. They are stored in a new list (called :code:`image`). In this case, the final object is an array from the Numpy package.

Opening an image
----------------

You can try this function with the next command, in a *command shell*:

>>> image = read_image_PGM("../../_data/robot.pgm")
PGM File
Magic Number=P2
W=600 / H=382 / Maximum Gray Value=255

The :file:`robot.pgm` file contains an image of 600 x 382 pixels.

The type of the returned object is a Python :code:`numpy.ndarray`.

>>> print(type(image))
<class 'numpy.ndarray'>

And you can access to the shape of the image by the following instruction : 

>>> print(image.shape)
(382, 600)

Accessing to a pixel value
==========================

The function we defined returns a list of integers. In this example, the length of the list :code:`image` is 600 by 382 pixels.

If you want to access to the 96th pixel of the 50th row (each row has 600 pixels), you need to use the following command:

>>> print(image[50, 96])
[190]


Create a class: ImagePGM
************************

To **facilitate the access to metadata** of an image, it is recommended to use a data structure or a **class** that gathers the main characteristics of an image.

.. note::

    If you are not familiar with **object-oriented programming**, you can practice with this tutorial: *Soon...*


|

Start by discovering PGM images (without compression - grayscale)

* :file:`01_imagePGM_class` : a class that describes a PGM image and its content, with:
	* :code:`readImagePGM` method to read an image from its file name
	* overloading of the << operator
	* Python with list !!
* :file:`02_imagePGM_modular` : the same as previously but with:
	* separated files for class declaration, definition and main program
	* :code:`writeImagePGM` method to write an image
