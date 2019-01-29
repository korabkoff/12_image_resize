# Image Resizer
Script for image resize.
If width provided height calculated to maintain image proportion and vise versa.
If width and height provided - make exact that image. Do notify if proportions changed.
If scale provided, width and height can't - script breaks and notify about wrong behaviour.
If no path for output provided, image saving in the same directory as original.
If original file name is 'pic.jpg'(100x200), then after run:
```#!bash
 python image_resize.py --scale 2 pic.jpg
```
must be created 'pic__200x400.jpg'

# Parametrs
path_to_original: first and mandatory argument for path to image

--scale, -s : scale

--width, -w : width

--height, -hi : height

--output_path, -out : output path for processed image.

# How to run

script require python3.5
Example of script launch on Linux, Python 3.5:
```#!bash
python3 image_resize.py pics/test.jpg -s 0.5
# reduce image twice and save in the same directory.

python3 image_resize.py pics/test.jpg -out final -w 200
# resize image to width 200 pixels and save to 'final' directory.
# directory must exist

python3 image_resize.py pics/test.jpg -hi 100
# resize image to heigth 100 pixels.

python3 image_resize.py pics/test.jpg -hi 100 -w 200
# resize image to heigth 100 pixels and width 200 pixels.

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
