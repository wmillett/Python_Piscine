import sys
import ast


def ft_filter(function, iterable):
    """
    Custom implementation of the filter function using list comprehensions.

    Args:
        function: A function (or None) to apply to each item in the iterable.
        iterable: An iterable (e.g., list, tuple) to filter.

    Returns:
        An iterator that yields items from the iterable and returns True.
        If function is None, it filters out items that evaluate to False.
    """
    if function is None:
        return (item for item in iterable if item)
    else:
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
        function = eval(args[0]) if args[0] != "None" else None
        iterable = ast.literal_eval(args[1])
        filtered = ft_filter(function, iterable)
        print(list(filtered))  # Ensure the output is a valid list
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])