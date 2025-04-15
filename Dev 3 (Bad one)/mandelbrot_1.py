from mandelbrot import MandelbrotSet
from PIL import Image

mandelbrot_set = MandelbrotSet(max_iterations=20, escape_radius=1000)

width, height = 1024, 1024
scale = 0.004
GRAYSCALE = "L"

image = Image.new(mode=GRAYSCALE, size=(width, height))
for y in range(height):
    for x in range(width):
        c = scale * complex(x - width / 2, height / 2 - y)
        instability = 1 - mandelbrot_set.stability(c, smooth=True)
        image.putpixel((x, y), int(instability * 255))

image.show()