from oop import Dog, Cat

def test_animal_speak():
    """Test basic animal speak functionality."""
    dog1 = Dog("Rex", 1)
    cat1 = Cat("Kitty", 0)
    dog2 = Dog("Fido", 6)
    cat2 = Cat("Sylvester", 2)

    assert dog1.speak() == f"Ruff. My name is Rex, and I am {1} year old."
    assert cat1.speak() == f"Meow. My name is Kitty, and I am {0} years old."
    assert dog2.speak() == f"Ruff. My name is Fido, and I am {6} years old."
    assert cat2.speak() == f"Meow. My name is Sylvester, and I am {2} years old."