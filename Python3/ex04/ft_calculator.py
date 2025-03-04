class calculator:
    """
    A calculator that can perform operations on vectors.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        """
        result = 0
        for x, y in zip(V1, V2):
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
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract the second vector from the first vector element-wise.

        Args:
            V1 (list of float): The first vector.
            V2 (list of float): The second vector.
        """
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
