

def square(x: int | float) -> int | float:
    """
    Applies a number to its square.

    Args:
        x (int | float): number to apply square.
    Returns:
        int | float: result of calculation.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument x must be an int or float.")
    if x == 0:
        raise ValueError("Argument cannot be '0'.")
    return x * x


def pow(x: int | float) -> int | float:
    """
    Applies a number to its power.

    Args:
        x (int | float): number to apply power.
    Returns:
        int | float: result of calculation.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument x must be an int or float.")
    if x == 0:
        raise ValueError("Argument cannot be '0'.")
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Takes a number and a function and returns an object that
    is the result of the arguments calculations.

    Args:
        x (int | float): number to be made the calculations.
        function: the function to apply to calculate the number x.
    Returns:
        object: the result object of the applied function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument x must be an int or float.")
    if not callable(function):
        raise TypeError("Argument function must be a callable function.")
    count = 0
    result = x

    def inner() -> float:
        """
        Inner function part of the outer function.

        Args:
            None.
        Return:
            float: result of function from outer.
        """
        nonlocal result
        nonlocal count
        count += 1
        try:
            result = function(result)
        except Exception as e:
            raise RuntimeError(f"Error in function call: {e}")
        return result
    return inner
