import subprocess


def test_with_input(text_input):
    """
    Tests the program by passing the input through standard input.

    Args:
        text_input (str): The input string to be tested.
    """
    # Simulate input being passed via stdin
    process = subprocess.Popen(
        ['python3', 'building.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Send input text to the program and capture the output
    output, error = process.communicate(input=text_input.encode())

    # Print the results from the program
    if process.returncode == 0:
        print("Output:")
        print(output.decode())  # Decode the bytes to string
    else:
        print("Error:")
        print(error.decode())  # Decode error bytes to string


def test_with_arguments(args):
    """
    Tests the program by passing arguments through the command line.

    Args:
        args (list): List of command-line arguments to be tested.
    """
    process = subprocess.Popen(
        ['python3', 'building.py'] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Capture the output
    output, error = process.communicate()

    # Print the results from the program
    if process.returncode == 0:
        print("Output:")
        print(output.decode())  # Decode the bytes to string
    else:
        print("Error:")
        print(error.decode())  # Decode error bytes to string


if __name__ == "__main__":
    # Test cases:

    # Test the program with various inputs via stdin
    print("Testing via stdin (interactive input):")
    test_with_input("Hello World! This is a test.123\n")

    # Test the program with arguments
    print("\nTesting via command-line arguments:")
    test_with_arguments(["Hello World! This is a test.123"])

    # Test with an empty string
    print("\nTesting with an empty string via arguments:")
    test_with_arguments([""])

    # Test with a string that contains non-printable characters
    print("\nTesting with non-printable characters via arguments:")
    test_with_arguments(["Hello\x01World\x02"])

    # Test with an invalid argument count (more than 1 argument)
    print("\nTesting with too many arguments (should raise AssertionError):")
    test_with_arguments(["Too", "Many", "Arguments"])
