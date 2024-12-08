import sys


def check_conditions(args):
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    try:
        int_arg = int(args[0]) 
    except ValueError:
        raise AssertionError("argument is not an integer")
    return int_arg


def main(args):
    try:
        if len(args) == 0:
            return
        int_arg = check_conditions(args)
        if int_arg % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
            
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main(sys.argv[1:])
