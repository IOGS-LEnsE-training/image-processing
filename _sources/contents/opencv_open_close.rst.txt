Opening and closing
###################

Opening and closing **morphological operations** are fundamental techniques used in
image processing, primarily for manipulating binary or grayscale images. These operations involve applying a structuring element (or kernel) to an image, and they are typically used for noise removal, shape extraction, and image enhancement.

Opening Operation
*****************

Definition: Opening is the process of eroding an image first and then dilating the eroded image. It's denoted as A ∘ B, where A is the image and B is the structuring element (kernel).

Purpose
=======

Removes small objects or noise from the foreground (white regions in a binary image).
Helps in separating connected objects in an image.

How it Works
============

Erosion: Shrinks the foreground objects by eroding the boundaries.
Dilation: Expands the eroded objects, restoring the size of the remaining objects after erosion.
Result: Small white regions (noise) are removed, and the shape of the larger objects is preserved.

Use Case: Cleaning up noise in binary images.

Closing Operation
*****************
Definition: Closing is the reverse of opening. It first dilates the image and then erodes it. It's denoted as A • B, where A is the image and B is the structuring element (kernel).

Purpose
=======

Closes small holes or gaps in the foreground (white regions in a binary image).
Connects or "fills" small breaks in the objects.

How it Works
============

Dilation: Expands the foreground objects by enlarging the boundaries.
Erosion: Shrinks the dilated objects back to their original size, but with small holes or gaps filled.
Result: Small black regions (holes) within the objects are removed, and small gaps between objects are closed.

Use Case: Filling small holes and connecting close objects.

