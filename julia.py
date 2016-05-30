# Fractal Generator: Mandelbrot Sets
# December 13, 2015
# Source for base code and other references:
# Pid Eins: http://0pointer.net/blog/projects/mandelbrot.html
# EESITE: http://eesite.bitbucket.org/html/software/fractal/fractal.html

import Image, ImageDraw, math, colorsys

# Constant variables
dimensions = (800, 800)
# scale image dimension down to dimension of Mandelbrot Set ~(3,3) in loop
scale = 1.0/(dimensions[0]/3)
# centers the image in the given dimensions 
#(otherwise only real-real quadrantwould be visible)
center = (1.5, 1.5)                # Use this for Julia set
iterate_max = 100
colors_max = 50

# Create image and object d which can be used to draw in given image
img = Image.new("RGB", dimensions) 
d = ImageDraw.Draw(img)

# Calculate a tolerable palette. 
# HSV easier to sample from (different hues with same sat and value) 
# use colorsys to convert HSV to RGB
# alternatively, download available palettes
palette = [0] * colors_max
for i in xrange(colors_max):
    f = 1-abs((float(i)/colors_max-1)**15)
    r, g, b = colorsys.hsv_to_rgb(.66+f/3, 1-f/2, f)
    palette[i] = (int(r*255), int(g*255), int(b*255))

# Calculate the mandelbrot sequence for the point c with start value z
def iterate_mandelbrot(c, z=0):
    for n in xrange(iterate_max + 1):
        z = z*z +c
        if abs(z) > 2:
            return n
    return None

# Draw Mandelbrot set
for y in xrange(dimensions[1]):
    for x in xrange(dimensions[0]):
        c = complex(x * scale - center[0], y * scale - center[1])

        n = iterate_mandelbrot(complex(0.3, 0.6), c)  # Use this for Julia set

        if n is None:
            v = 1
        else:
            # describes length of time until c is bounded
            v = n/100.0
        
        # Fill point with palette color based on length of time until bounded
        d.point((x, y), fill = palette[int(v * (colors_max-1))])

del d
img.save("julia.png")