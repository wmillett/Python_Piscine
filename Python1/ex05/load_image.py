from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a file.

    Args:
        path: The path to the image.
    Returns:
        The image as a numpy array.
    """
    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            img_array = np.array(img)
            print(f"The shape of image is: {img_array.shape}")
            print(img_array)
            return img_array
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return None
