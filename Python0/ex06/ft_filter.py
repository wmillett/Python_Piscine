import sys
import ast


def ft_filter(function, iterable):
    """
    Custom implementation of the filter function using list comprehensions.

    Args:
        function: A function (or None) to apply to each item in the iterable.
        iterable: An iterable (e.g., list, tuple) to filter.

    Returns:
        An iterator that yields items from the iterable for which the function returns True.
        If function is None, it filters out items that evaluate to False.
    """
    if function is None:
        # If function is None, filter out falsy values
        return (item for item in iterable if item)
    else:
        # Otherwise, apply the function to filter items
        return (item for item in iterable if function(item))


def main(args):
    """
    Main for ft_filter, parses invalid input.

    Args:
        Argument list for ft_filter.

    Return:
        Filtered list.
    """
    try:
        if len(args) != 2:
            raise Exception("Usage: ft_filter(function, iterable)")

        # Parse args safely using ast
        function = ast.literal_eval(args[0]) if args[0] != "None" else None
        iterable = ast.literal_eval(args[1])  # TODO change to make Lambda ok

        # Execute and print
        filtered = ft_filter(function, iterable)
        print(list(filtered))
        filtered = filter(function, iterable)
        print(list(filtered))
    except Exception as e:
        print("Error: ", e)
        return 1


if __name__ == "__main__":
    main(sys.argv[1:])
