import sys


def count_in_list(lst: list, item: str):
    """
    Count the number of occurrences of an item in a list.

    Args:
        lst (list): The list to search.
        item (str): The item to search for.

    Returns:
        int: The number of occurrences of the item in the list.
    """
    return lst.count(item)

if __name__ == "__main__":
    count_in_list(sys.argv[1:])
