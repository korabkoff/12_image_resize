from PIL import Image
import argparse
import os
import sys
from fractions import Fraction


def parse_args(args):

    def readable_dir(prospective_dir):
        if not os.path.isdir(prospective_dir):
            raise Exception("readable_dir:{0} is not a valid path".format(prospective_dir))
        if os.access(prospective_dir, os.R_OK):
            return prospective_dir
        else:
            raise Exception("readable_dir:{0} is not a readable dir".format(prospective_dir))

    parser = argparse.ArgumentParser(description='Image resize')
    parser.add_argument('path_to_original', default=None, help='File path to image file', type=open)
    parser.add_argument('--output_path', '-out', default=None, help='File path to store result file', type=readable_dir)
    parser.add_argument('--height', '-hi', default=None, help='new image height ', type=int)
    parser.add_argument('--width', '-w', default=None, help='new image width ', type=int)
    parser.add_argument('--scale', '-s', default=None, help='image scale', type=float)

    return parser.parse_args(args)


def open_image(path_to_original):
    if not path_to_original:
        return None

    return Image.open(path_to_original)


def resize_image(im, width, height, scale):

    img_width, img_height = im.size

    if scale and (height or width):
        print('Scale can\'t be used with height or width')
        return None

    elif scale and not width and not height:
        return im.resize(
            (round(img_width * (Fraction(scale))),
             round(img_height * (Fraction(scale)))),
            resample=0
        )

    elif not height and not scale:
        scale = width / img_width
        return im.resize((width, round(img_height * (Fraction(scale)))), resample=0)

    elif not width and not scale:
        scale = height / img_height
        return im.resize(((round(img_width * (Fraction(scale)))), height), resample=0)

    else:
        if img_width / img_height != width / height:
            print('Image proportions not identical')
        return im.resize((width, height), resample=0)


def save_image(im, path_to_original, path_to_result):

    img_width, img_height = im.size
    basename = os.path.basename(path_to_original)
    path_to_img = '{}'.format(os.path.dirname(path_to_original))
    img_name = (basename.split('.'))[0]
    img_ext = (basename.split('.'))[1]

    if not path_to_result:
        path_to_result = '{}{}__{}x{}.{}'.format(
            path_to_img,
            img_name,
            img_width,
            img_height,
            img_ext
        )
    else:
        path_to_result = '{}/{}__{}x{}.{}'.format(
            path_to_result,
            img_name,
            img_width,
            img_height,
            img_ext
        )
    im.save(path_to_result, format=None)


if __name__ == '__main__':

    parser = parse_args(sys.argv[1:])

    path_to_original = parser.path_to_original.name

    path_to_result = parser.output_path

    height = parser.height

    width = parser.width

    scale = parser.scale

    the_image = open_image(path_to_original)

    the_image = resize_image(the_image, width, height, scale)

    save_image(the_image, path_to_original, path_to_result)

