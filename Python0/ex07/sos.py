import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def text_to_morse(text):
    """
    Converts a text string to Morse code.

    Args:
        text (str): The text to convert to Morse code.

    Returns:
        str: The Morse code representation of the text.
    """
    morse_code = []
    for char in text.upper():
        if char in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char])
            morse_code.append(" ")
    if morse_code:
        morse_code.pop()
    return "".join(morse_code).strip()


def main(args):
    """
    Main function for the sos program.

    Args:
        args (list): Command-line arguments passed to the program.

    Raises:
        AssertionError: If the number of arguments is not 1 or if the
        type is invalid.

    Returns:
        None
    """
    try:
        if len(args) != 1:
            raise AssertionError("Usage: sos.py <text>")
        text = args[0]
        for char in text.upper():
            if char not in NESTED_MORSE:
                raise AssertionError("Invalid input")
        morse_code = text_to_morse(text)
        print(morse_code)
    except AssertionError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
