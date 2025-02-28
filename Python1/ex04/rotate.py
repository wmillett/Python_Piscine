from zoom import zoom
import matplotlib.pyplot as plt
import sys
import numpy as np


def rotate(img, angle):
    """
    Rotate an image by a given angle.
    Args:
        img: The image to rotate.
        angle: The angle to rotate the image by.
    Returns:
        The rotated image.
    """
    try:
        new_img = np.rot90(img, k=1)  # TODO Make your own rotation function
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return new_img


def main(args):
    """
    Load an image from a file and rotate it.
    Ars:
        args: Command line arguments.
    Returns:
        None
    """
    if not args:
        args = ["./animal.jpeg", 90]
    if len(args) != 2:
        print("Usage: python3 rotate.py <path> <angle>")
        return
    try:
        img = zoom(args[0])
        if img is None:
            raise Exception("An error occurred.")
        angle = int(args[1])
        if angle < 0:
            raise ValueError("Angle must be a positive integer.")
        if angle >= 360:
            raise ValueError("Angle must be less than 360.")
        new_img = rotate(img, angle)
        if img is None:
            raise Exception("An error occurred.")
        print(f"The shape of the rotated image is: {img.shape}")
        plt.imshow(new_img)
        plt.show()
        return    
    except ValueError:
        print("Invalid angle.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main(sys.argv[1:])
