import sys


def filter_words(S, N):
    """
    Filters words from string S that have a length greater than N.

    Args:
        S (str): The input string containing words separated by spaces.
        N (int): The minimum length of words to include in the output.

    Returns:
        list: A list of words from S with length greater than N.
    """
    # Strip surrounding quotes from the input string
    if S.startswith("'") and S.endswith("'"):
        S = S[1:-1]
    elif S.startswith('"') and S.endswith('"'):
        S = S[1:-1]

    # Split the string into words
    words = S.split()

    # Filter words with length > N
    filtered_words = [word for word in words if len(word) > N]

    return filtered_words


def main(args):
    """
    Main function to handle command-line arguments and execute the program.

    Args:
        args (list): Command-line arguments passed to the program.

    Raises:
        AssertionError: If the number of arguments is not 2 or if the
        types are invalid.
    """
    try:
        # Check if the number of arguments is exactly 2
        assert len(args) == 2, "Exactly 2 arguments are required"

        # Extract arguments
        S = args[0]
        N = args[1]

        # Validate types
        assert isinstance(S, str), "The first argument must be a string."
        assert N.isdigit(), "The second argument must be an integer."

        # Convert N to an integer
        N = int(N)

        # Filter words and print the result
        result = filter_words(S, N)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
