# Fractal Generator: Mandelbrot Sets
# December 13, 2015
# Draw mandelbrot function references: http://0pointer.net/blog/projects/mandelbrot.html

import Image, ImageDraw, random
# ImageDraw module provides simple 2D graphics for Image objects. 
# Create new images, generate graphics

# Constants
DIMENSIONS = (50000, 50000)
# scale image dimension down to dimension of Mandelbrot Set ~(3,3) in loop
SCALE = 1.0/(DIMENSIONS[0]/3)  
# centers the image in the given dimensions 
CENTER = (2.2, 1.5)                  # Use this for Mandelbrot set
MAX_ITERATIONS = 100
NUM_COLORS = 255

def get_color_palette(colors_num):
    """ 
    Creates a list of 'colors_num' triples as an RGB color palette.
    Uses a pseudo-random number generator.
    Takes as input number of colors in RGB palette.
    """
    palette = []
    for i in xrange(colors_num):
        (r, g, b) = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        palette.append((r, g, b))
    return palette


def iterate_mandelbrot(c, iterate_max, z=0):
    """
    Calculates the mandelbrot sequence for the point c withs tart value z
    """
    for n in xrange(iterate_max + 1):
        z = z*z +c
        if abs(z) > 2:
            return n
    return None


def draw_mandelbrot(max_iterations, dimensions, scale, center, color_palette):
    """
    Draws mandelbrot using color palette and iterate mandelbrot functions.
    returns Image object
    """
    # Create image and object d which can be used to draw in given image
    img = Image.new("RGB", dimensions) 
    d = ImageDraw.Draw(img)
    for y in xrange(dimensions[1]):
        for x in xrange(dimensions[0]):
            c = complex(x * scale - center[0], y * scale - center[1])   
            n = iterate_mandelbrot(c, max_iterations)          
            if n is None:
                v = 1
            else:
                # describes length of time until c is bounded
                v = n
            # Fill point with palette color based on length of time until bounded
            d.point((x, y), fill = color_palette[v])
    return img


if __name__ == '__main__':
    pal = get_color_palette(NUM_COLORS)
    img = draw_mandelbrot(MAX_ITERATIONS, DIMENSIONS, SCALE, CENTER, pal)
    img.save("result.png")
