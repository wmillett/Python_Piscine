from load_image import ft_load
import matplotlib.pyplot as plt
import sys
import numpy as np
import traceback


def custom_transpose(arr):
    """
    Transpose a 2D or 3D array.
    Args:
        arr: The array to transpose (2D or 3D).
    Returns:
        The transposed array.
    """
    if arr.ndim == 2:
        # Handle 2D arrays
        rows, cols = arr.shape
        transposed_arr = np.empty((cols, rows), dtype=arr.dtype)
        for i in range(rows):
            for j in range(cols):
                transposed_arr[j, i] = arr[i, j]
    elif arr.ndim == 3:
        # Handle 3D arrays (images with channels)
        rows, cols, channels = arr.shape
        transposed_arr = np.empty((cols, rows, channels), dtype=arr.dtype)
        for i in range(rows):
            for j in range(cols):
                for k in range(channels):
                    transposed_arr[j, i, k] = arr[i, j, k]
    else:
        raise ValueError("Input array must be 2D or 3D.")
    return transposed_arr


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
        new_img = custom_transpose(img)
        new_img = new_img[:: -1, :, :]
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
    args = ["./animal.jpeg", 90]
    print(args)
    if len(args) != 2:
        print("Usage: python3 rotate.py <path> <angle>")
        return
    try:
        img = ft_load(args[0])
        if img is None:
            raise Exception("Image missing.")
        img = img[:400, :400, :1]
        print(f"The shape of image is: {img.shape}")
        print(img)
        angle = int(args[1])
        if angle < 0:
            raise ValueError("Angle must be a positive integer.")
        if angle >= 360:
            raise ValueError("Angle must be less than 360.")
        new_img = rotate(img, angle)
        if img is None:
            raise Exception("Image missing.")
        print(f"The shape of the rotated image is: {img.shape}")
        print(new_img)
        plt.imshow(new_img)
        plt.show()
        return
    except ValueError:
        print("Invalid angle.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback_details = traceback.format_exc()
        print("Traceback details:")
        print(traceback_details)
        return


if __name__ == "__main__":
    main(sys.argv[1:])
