Image transformations
#####################

What is a binarization ?
************************



What is a convolution ?
***********************


No, filtering operations such as mean filtering are not considered morphological operations. They are part of a different category of image processing techniques known as spatial filtering or convolutional filtering.

Filtering Operations
********************

Purpose
=======
Filtering operations like mean filtering (or averaging) are used to smooth images, reduce noise, and sometimes enhance specific features such as edges.

How It Works
============

Mean filtering involves convolving an image with a filter kernel (e.g., a 3x3 matrix where each value is
1/9). This operation computes the average of the pixel values within the kernel's neighborhood and assigns this average to the central pixel.

Common Types of Filters
=======================

- **Mean Filter**: Reduces noise by averaging the pixel values in the neighborhood.
- **Gaussian Filter**: Applies a Gaussian function for weighted averaging, often used for blurring.
- **Median Filter**: Replaces the central pixel with the median of the neighborhood values, effective at reducing salt-and-pepper noise.

Morphological Operations
************************

Purpose
=======

Morphological operations are used to process the shape or structure of objects within an image, such as
removing noise, separating objects, filling gaps, and enhancing object boundaries.

How It Works
============

These operations rely on the interaction between an image and a structuring element (kernel). The
operations focus on modifying the geometry of objects based on the shape and size of the structuring element.

Common Morphological Operations
===============================

- **Erosion**: Removes pixels on object boundaries, shrinking the objects.
- **Dilation**: Adds pixels to object boundaries, expanding the objects.
- **Opening**: Erosion followed by dilation, used to remove small objects/noise.
- **Closing**: Dilation followed by erosion, used to close small holes/gaps.


Effect
======

Alters the shape of objects in the image without averaging pixel values; instead, it manipulates the binary or
grayscale structure of the image.


Other ressource
***************

You can find demonstration of different image filters using convolution on the website `geekosophers.com <https://geekosophers.com/algorithms/>`_.