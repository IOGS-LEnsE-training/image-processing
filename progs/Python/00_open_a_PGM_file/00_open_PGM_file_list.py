"""00_open_PGM_file_list file.

Image Processing / Tutorials
First example of opening a PGM file and store the data in a list.

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""


def read_image_PGM(filename: str) -> list:
    """
    Read a PGM image from a file and return its information.

    :param filename: Name of the PGM file.
    :type filename: str

    :return: A list of the pixels.
    :rtype: list

    """
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


# Main function
if __name__ == "__main__":
    # Read the input PGM image
    image = read_image_PGM("../../_data/robot.pgm")
    print(type(image))

    print(image[58])
    print(image[50 * 600 + 96])