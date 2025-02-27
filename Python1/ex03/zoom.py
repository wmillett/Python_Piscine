from load_image import ft_load
import sys
import matplotlib.pyplot as plt


def main(args):
    """
    Main function of the zoom program. The zoom program
    takes an image, loads it and slices it to a smaller
    image. The program then displays the zoomed image.

    Args:
        args: Takes the path to an image.

    Returns:
        None
    """
    if len(args) > 7:
        print("Error: Too many arguments.")
        return
    if not args:
        args = ["./animal.jpeg", 0, 400, 0, 400, 0, 1]
    if len(args) < 7:
        print("Error: Not enough arguments.")
        return
    try:
        img = ft_load(args[0])
        if img is None:
            return
        print(img)
        for i in range(1, len(args)):
            try:
                args[i] = int(args[i])
                if args[i] < 0:
                    print("Error: Argument must be a positive integer.")
                    return
            except ValueError:
                print("Error: Argument must be an integer.")
                return
        mp = "New shape after slicing: "
        new_img = img[args[1]:args[2], args[3]:args[4], args[5]:args[6]]
        print(f"{mp}{new_img.shape} or {new_img.shape[:2]}")
        print(new_img)
        plt.imshow(new_img)
        plt.show()
    except IndexError:
        print("Please provide a path to an image.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main(sys.argv[1:])
