#!/usr/bin/env python3

from PIL import Image
import numpy as np
import random
import sys
import argparse

white = (255, 255, 255)

def rnd_color(max_luminosity, fname):
    lumins = 256
    img = Image.open(fname)
    pxl = img.load()
    x, y = img.size
    rnd_sample = None
    while lumins > max_luminosity:
        rnd_x = random.randint(0, x - 1)
        rnd_y = random.randint(0, y - 1)
        rnd_sample = pxl[rnd_x, rnd_y]
        lumins = rnd_sample[0] + rnd_sample[1] + rnd_sample[2]
        lumins /= 3
    return rnd_sample


def add_brick(color_row, brick_x, mortar_width, max_luminosity, fname):
    red = rnd_color(max_luminosity, fname)

    for i in range(mortar_width//2):
        color_row.append(white)

    for i in range(brick_x):
        color_row.append(red)

    for i in range(mortar_width//2):
        color_row.append(white)


def draw(brick_x, brick_y, bricks_per_row, rows, mortar_width, max_luminosity, fname):
    dim_x = (mortar_width + brick_x) * bricks_per_row
    dim_y = (mortar_width + brick_y) * rows
    img = Image.new('RGB', (dim_x, dim_y))
    pxl = img.load()
    pixels_wide = (mortar_width + brick_x) * bricks_per_row
    full_image = []
    offset = True 
    for row_n in range(rows):
        offset = not offset

        # Add upper mortar to image.
        for _ in range(mortar_width//2):
           full_image.append([white for _ in range(dim_x)])

        # Make line of bricks
        image_row = []
        for bricks in range(bricks_per_row):
            add_brick(image_row, brick_x, mortar_width, max_luminosity, fname)

        # Offset row of bricks so they're staggered
        if offset:
            for _ in range((brick_x + mortar_width)//2):
                image_row.append(image_row.pop(0))

        # Add line of bricks to image
        for _ in range(brick_y):
            full_image.append(image_row)

        # Add lower mortar
        for _ in range(mortar_width//2):
            full_image.append([white for _ in range(dim_x)])

    # Assign pixels to image
    for i, row in enumerate(full_image):
        if row == None:
            continue
        for j, col in enumerate(row):
            if not i or not j:
                continue
            try:
                pxl[j, i] = col
            except:
                import pdb; pdb.set_trace()

    img.save("out.png")
    img.show()

def main():
    parser = argparse.ArgumentParser("Procedural Birck Generation")
    parser.add_argument("-x", "--brick_x"  , default=40      , type=int)
    parser.add_argument("-y", "--brick_y"  , default=20      , type=int)
    parser.add_argument("-r", "--rows"     , default=10      , type=int)
    parser.add_argument("-c", "--cols"     , default=10      , type=int)
    parser.add_argument("-m", "--mortar"   , default=2       , type=int)
    parser.add_argument("-l", "--max_lumin", default=200     , type=int)
    parser.add_argument("-f", "--fname"    , default="in.jpg", type=str)
    args = parser.parse_args(sys.argv[1:])
    draw(args.brick_x, args.brick_y, args.rows, args.cols, args.mortar, args.max_lumin, args.fname)

if __name__ == "__main__":
    main()
