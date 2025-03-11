import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random id for a 42 student.

    Args:
        None.
    Returns:
        str: the id of the student.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Student class.

    Parameters:
        name (str): name of the student.
        surname (str): surname of the student.
        active (bool): true when class is instanciated.
        login (str): created in __post_init__ based on the
        student's name and surname.
        id (str): randomly generated when instanciated.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id)

    def __post_init__(self):
        """
        After initialization of the Student class,
        creates a login based on the name and surname
        of the student.

        Args:
            self: instance of the Student class.
        Returns:
            None.
        """
        self.login = self.name[0].upper() + self.surname
