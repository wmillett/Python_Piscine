import numpy as np


def ft_invert(array) -> np.array:
    """
    Invert the colors of an image.
    Args:
        array: The image to invert.
    Returns:
        The inverted image.
    """
    try:
        max_value = np.iinfo(array.dtype).max
        inverted = max_value - array
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return inverted


def ft_red(array) -> np.array:
    """
    Applies a red filter to an image.
    Args:
        array: The image to apply the filter to.
    Returns:
        The image with the red filter applied.
    """
    red_array = np.copy(array)
    red_array[:, :, 1] = 0  # Green channel
    red_array[:, :, 2] = 0  # Blue channel
    return red_array


def ft_green(array) -> np.array:
    """
    Applies a green filter to an image.
    Args:
        array: The image to apply the filter to.
    Returns:
        The image with the green filter applied.
    """
    green_array = np.copy(array)
    green_array[:, :, 0] = 0  # Red channel
    green_array[:, :, 2] = 0  # Blue channel
    return green_array


def ft_blue(array) -> np.array:
    """
    Applies a blue filter to an image.
    Args:
        array: The image to apply the filter to.
    Returns:
        The image with the blue filter applied.
    """
    blue_array = np.copy(array)
    blue_array[:, :, 0] = 0  # Red channel
    blue_array[:, :, 1] = 0  # Green channel
    return blue_array


def ft_grey(array) -> np.array:
    """
    Convert an image to grayscale.
    Args:
        array: The image to convert.
    Returns:
        The grayscale image.
    """
    grayscale = np.copy(array)
    # red = array[:, :, 0]
    # green = array[:, :, 1]
    # blue = array[:, :, 2]
    # grayscale = (red + green + blue) // 3

    weights = np.array([0.2989, 0.5870, 0.1140])

    # Compute the weighted sum to get the grayscale values
    grayscale = np.dot(array, weights)

    # grayscale = grayscale.astype(np.uint8)
    return grayscale
    #  grey = np.mean(grey, axis=2)
    #  return grey
