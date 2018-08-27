# Bricks

## Summary

This program requires an input image to work. The reason is
that no matter how much I fine-tuned the algorithm for gen-
erating realistic variations in brick color, it was always a
little off. The solution turned out to be both simpler and
more versatile: take a sample of colors from an input image
and use that to generate colors. I also had a version of this
that generate floorboards, and another that generated
"herringbone" patterns, but I can't seem to find them anymore.

## Dependencies

This program requires Python 3 and the libraries PIL and NP to be
installed. Apologies for the dependencies, but this was really
just something I made so that I would have any repeating textures
in a game I was prototyping.

## Use

### Command Line Arguments

All of the following have a default value if not passed as
arguments:

-x, --brick\_x   the width of each brick
-y, --brick\_y   the height of each brick
-r, --rows       how many rows of bricks to make
-c, --cols       how many bricks per row
-m, --mortar     the size of the mortar between bricks
-l, --max\_lumin set the max luminosity of colors to be used to generate bricks: for filtering out white colors (like mortar)
-f  --fname      the name of the file to sample colors from; in.jpg by default. You should probably specify this.
