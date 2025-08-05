# system imports
from abc import ABC, abstractmethod
import logging

# internal imports


# external imports


# logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Animal(ABC):
    def __init__(self, name: str, age: int):
        """
        Initializes the Animal object.
        """
        self.name = name
        self.age = age
        self.year = "year" if age == 1 else "years"

    @abstractmethod
    def speak(self) -> str:
        """
        Returns a string with the animal's name and age.
        """
        pass

class Dog(Animal):
    """
    A Dog is an Animal.
    """
    def speak(self) -> str:
        """
        Returns a string with the animal's name and age.
        """
        return f"Ruff. My name is {self.name}, and I am {self.age} {self.year} old."
    
class Cat(Animal):
    """
    A Cat is an Animal.
    """
    def speak(self) -> str:
        """
        Returns a string with the animal's name and age.
        """
        return f"Meow. My name is {self.name}, and I am {self.age} {self.year} old."