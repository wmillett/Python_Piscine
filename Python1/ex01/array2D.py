# import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and print some information about the shape.

    Args:
        family: A 2D array.
        start: The starting index.
        end: The ending index.

    Returns:
        A sliced 2D array.
    """
    shape = (len(family), len(family[0])) if family else (0, 0)
    print(f"My shape is : {shape}")

    sliced_family = family[start:end]
    new_shape = (len(sliced_family),
                 len(sliced_family[0])) if sliced_family else (0, 0)
    print(f"My new shape is : {new_shape}")

    return sliced_family
