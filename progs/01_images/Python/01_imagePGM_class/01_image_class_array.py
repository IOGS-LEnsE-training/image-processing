"""01_image_class_array file.

File containing :class::ImagePGM
Class to represent a PGM image. Using an array to store the data.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import numpy as np

class ImagePGM:
    """
    Class to represent a PGM image.

    :param width: Width of the image.
    :type width: int
    :param height: Height of the image.
    :type height: int
    :param channels: Number of color values for each pixel of the image.
    :type channels: int
    :param max_gray_value: Value of the white color.
    :type max_gray_value: int
    :param magic_number: Type of the file.
    :type magic_number: str
    :param pixels: Value of each pixel.
    :type pixels: list
    """
    
    def __init__(self, filename):
        """
        Initialize the ImagePGM object.

        Parameters:
            filename (str): Name of the PGM file.
        """
        self.width = 0              # Width of the image
        self.height = 0             # Height of the image
        self.channels = 0           # Number of color values for each pixel of the image
        self.max_gray_value = 0     # Value of the white color
        self.magic_number = ""      # Type of the file
        self.pixels = np.array([])  # Value of each pixel
        self.readImagePGM(filename)
    
    def readImagePGM(self, filename):
        """
        Read a PGM image from a file and store its information.

        :param filename: Name of the PGM file.
        :type filename: str
        
        :return: True if the file was successfully read, False otherwise.
        :rtype: bool

        """
        try:
            with open(filename, 'r') as f:
                self.magic_number = f.readline().strip()
                if self.magic_number != 'P2':
                    raise ValueError("Invalid PGM file format")
                # Read the width, height, and maximum gray value
                self.width, self.height = map(int, f.readline().split())
                self.max_gray_value = int(f.readline())
                # Read the image data
                image_data = []
                for _ in range(self.height):
                    row = list(map(int, f.readline().split()))
                    image_data.extend(row)

                # Convert the image data to a NumPy array
                self.pixels = np.array(image_data, dtype=np.uint8).reshape((self.height, self.width))

        except FileNotFoundError:
            print(f"Error: Unable to open file {filename}")
            return False
        return True

    def __str__(self):
        """
        Return a string representation of the ImagePGM object.

        :return: A string with PGM image informations
        :rtype: str
        """
        return f"Image PGM / Type: {self.magic_number}, (W,H) = ({self.width}, {self.height})"


# Main function
if __name__ == "__main__":
    # Read the input PGM image
    image = ImagePGM("../../_data/robot.pgm")

    print("Infos")
    print(image)
    print(type(image.pixels))
