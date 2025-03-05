from typing import Generator, Tuple


class calculator:
    """
    A calculator that can perform operations on vectors.
    """

    @staticmethod
    def custom_zip(
        list1: list[float], list2: list[float]
    ) -> Generator[Tuple[float, float], None, None]:
        """
        Custom zip function to iterate over two lists simultaneously.

        Args:
            list1 (list of float): The first list.
            list2 (list of float): The second list.

        Yields:
            Tuple[float, float]: A tuple containing elements from both lists.
        """
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length.")

        for i in range(len(list1)):
            yield (list1[i], list2[i])

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        """
        result = 0
        for x, y in calculator.custom_zip(V1, V2):
            result += float(x) * float(y)
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        """
        result = (
            [float(x) + float(y) for x, y in calculator.custom_zip(V1, V2)])
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract the second vector from the first vector element-wise.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        """
        result = (
            [float(x) - float(y) for x, y in calculator.custom_zip(V1, V2)])
        print(f"Sous Vector is: {result}")
