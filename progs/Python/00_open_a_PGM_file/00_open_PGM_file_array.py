"""01_image_class_array file.

File containing :class::ImagePGM
Class to represent a PGM image. Using an array to store the data.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import numpy as np


def read_image_PGM(filename: str) -> list:
    """
    Read a PGM image from a file and return its information.

    :param filename: Name of the PGM file.
    :type filename: str

    :return: A list of the pixels.
    :rtype: list

    """
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
            
            # Lire les valeurs de pixels
            pixels = []
            for line in f:
                pixels.extend(line.split())
            
            # Convert the image data to a NumPy array
            image = np.array(pixels, dtype=int).reshape((height, width))
            return image
    except FileNotFoundError:
        print(f"Error: Unable to open file {filename}")


# Main function
if __name__ == "__main__":
    # Read the input PGM image
    image = read_image_PGM("../../_data/robot.pgm")
    print(type(image))
    print(image.shape)

    print(image[58])
    print(image[50, 96])
