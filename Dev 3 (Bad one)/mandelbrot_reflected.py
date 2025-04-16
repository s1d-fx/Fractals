from PIL import Image
from mandelbrot import MandelbrotSet
from viewport import Viewport
import matplotlib.cm

### Changing RGB scale from (0 to 255) to (0 to 1)
def denormalise(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]

### Choosing the colour theme
colormap = matplotlib.cm.get_cmap("turbo").colors
palette = denormalise(colormap)
len(colormap)
colormap[0]
palette[0]

### Creating mandelbrot set
mandelbrot_set = MandelbrotSet(max_iterations=1024, escape_radius=1000)
indices = []

### Function to create a bitmap image of the mandelbrot set
def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]
        indices.append(pixel.color)

### Zooming in on the desired region of the mandelbrot set
image = Image.new(mode="RGB", size=(256, 256))
viewport = Viewport(image, center=-0.7430 + 0.1302j, width=0.01)
paint(mandelbrot_set, viewport, palette, smooth=True)

### Enhancing the image
from PIL import ImageEnhance
enhancer = ImageEnhance.Brightness(image)
enhancer.enhance(1.25)

### Mirroring the image vertically
mirrored_image_1 = image.transpose(Image.FLIP_LEFT_RIGHT)
half_image = Image.new(mode="RGB", size=(2048, 1024))
half_image.paste(image, (0, 0))
half_image.paste(mirrored_image_1, (1024, 0))

### Mirroring the image horizontally
mirrored_image_2 = half_image.transpose(Image.FLIP_TOP_BOTTOM)
full_image = Image.new(mode="RGB", size=(2048, 2048))
full_image.paste(half_image, (0, 0))
full_image.paste(mirrored_image_2, (0, 1024))

### Showing the image
full_image.show()

### Saving the image as a png
image_path = "Mandelbrot_reflected_2048.png" 
full_image.save(image_path)
print(f"Final comnposition saved to {image_path}")
