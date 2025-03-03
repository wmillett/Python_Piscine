from S1E9 import Character


class Baratheon(Character):
    """
    A stag.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initiate Baratheon Character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Custom return for str from __str__.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Custom return for str from __repr__.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        """
        Create Baratheon Character.
        """
        return cls(first_name, is_alive)

    def die(self):
        """
        Simulate the death of the character.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Stupid lion.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initiate a Lannister Character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Custom return for str from __str__.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Custom return for str from __repr__.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Simulate the death of the character.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Create a Lannister Character.
        """
        return cls(first_name, is_alive)
