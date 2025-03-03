from abc import ABC, abstractmethod


class Character(ABC):
    """
    Class for a character.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a character with a first name and a health state.
        Args:
            first_name (str)
            is_alive (bool)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Change the health state of the character.
        """
        pass


class Stark(Character):
    """
    Stark class that inherits from the
    Character class.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Stark character.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Change the health state of Stark character.
        """
        self.is_alive = False
