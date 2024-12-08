import sys


def check_conditions(args):
    try:
        if len(args) == 0:
            print("Please provide a string")
            return True
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return True
    return False


def main(args):
    if check_conditions(args):
        return
    text = args[0]
    total_characters = len(text)
    upper_letters = sum(1 for char in text if char.isupper())
    lower_letters = sum(1 for char in text if char.islower())
    punctuation_chars = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""

    marks = sum(1 for char in text if char in punctuation_chars)
    spaces = text.count(" ")
    digits = sum(1 for char in text if char.isdigit())
    print(f"The text contains {total_characters} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main(sys.argv[1:])
