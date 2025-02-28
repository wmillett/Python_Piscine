from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey

from matplotlib import pyplot as pl


array = ft_load("landscape.jpg")
inverted = ft_invert(array)
red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
grey = ft_grey(array)
print(ft_invert.__doc__)


images = [array, inverted, red, green, blue, grey]
image_titles = ["Original Image", "Inverted Image", "Red Image",
                "Green Image", "Blue Image", "Grey Image"]
pl.figure(figsize=(10, 5))

nb_imgs = len(images)
nb_rows = (nb_imgs + 1) // 2

for i, Image in enumerate(images):
    if Image is not None:
        pl.subplot(nb_rows, 2, i + 1)
        pl.title(image_titles[i])
        pl.imshow(Image, cmap="gray")
        pl.axis('off')
    else:
        print("An error occurred.")
        exit(1)


pl.show()
