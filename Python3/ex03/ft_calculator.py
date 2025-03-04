class calculator:
    """
    A calculator that can perform 4 operations on vectors with a scalar.
    """

    def __init__(self, vector):
        """
        Initialize the calculator with a vector.

        Args:
            vector (list of float): The vector to perform operations on.
        """
        self.vector = vector

    def __add__(self, scalar):
        """
        Adds a scalar to each element of the vector and prints the result.

        Args:
            scalar (float): The scalar to add.
        """
        result = calculator([x + scalar for x in self.vector])
        print(result)
        return result

    def __mul__(self, scalar):
        """
        Multiplies each element of the vector by a scalar
        and prints the result.

        Args:
            scalar (float): The scalar to multiply.
        """
        result = calculator([x * scalar for x in self.vector])
        print(result)
        return result

    def __sub__(self, scalar):
        """
        Subtracts a scalar from each element of the vector
        and prints the result.

        Args:
            scalar (float): The scalar to subtract.
        """
        result = calculator([x - scalar for x in self.vector])
        print(result)
        return result

    def __truediv__(self, scalar):
        """
        Divides each element of the vector by a scalar and prints the result.

        Args:
            scalar (float): The scalar to divide by.
        """
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        result = calculator([x / scalar for x in self.vector])
        print(result)
        return result

    def __repr__(self):
        """
        Returns a string representation of the vector.
        """
        return f"Vector: {self.vector}"
