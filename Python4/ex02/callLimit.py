from typing import Any


# class CallLimitExceededError(Exception):
#    """Exception raised when the call limit is exceeded."""
#    pass


def callLimit(limit: int):
    """
    Function that sets a limit to the number
    of times a function can be called through
    a wrapper function.

    Args:
        limit (int): the limit of times the function can
        be called.
    Returns:
        None.
    """
    count = 0

    def callLimiter(function):
        """
        Wrapper function that sets the limit
        for callLimit.

        Args:
            function: function that is called.
        Returns:
            its wrapper function (limit_function).
        """
        nonlocal count

        def limit_function(*args: Any, **kwds: Any):
            """
            Checks the amount of times a function and its arguments
            are called.

            Args:
                *args (Any): the args of the function called.
                **kwds (Any): the keywords from the function called.
            Returns:
                Result of function that is called.
            """
            nonlocal count
            if not callable(function):
                raise TypeError("Error: {function} is not callable.")
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {repr(function)} call too many times")
                # raise CallLimitExceededError((
                #    f"Error: {repr(function)} call too many times"))
        return limit_function
    return callLimiter
