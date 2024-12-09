import sys

MAX_INPUT_SIZE = 10**6


def check_conditions(args):
    """
    Parses arguments sent to the program.

    Args:
        args(list): A list of arguments from the main function.
    Return:
        bool: true if the args do not pass the checks.
    Raises:
        AssertionError: if two many args(more than 1).
    """
    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return True
    return False


def main(args):
    """
    Takes a string and counts various amounts of different character
    within it and prints them out in the terminal.

    Args:
        Only takes one string argument.
    Returns:
        None.
    """
    if len(args) == 0:
        print("What is the text to count?")
        text = sys.stdin.readline()
    elif check_conditions(args):
        return
    else:
        text = args[0]
    total_characters = len(text)
    if total_characters > MAX_INPUT_SIZE:
        print("Input too large!")
        return
    upper_letters = sum(1 for char in text if char.isupper())
    lower_letters = sum(1 for char in text if char.islower())
    punctuation_chars = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""

    marks = sum(1 for char in text if char in punctuation_chars)
    spaces = text.count(" ") + text.count('\n')
    digits = sum(1 for char in text if char.isdigit())
    print(f"The text contains {total_characters} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main(sys.argv[1:])
