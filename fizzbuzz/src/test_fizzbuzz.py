import pytest
from src.fizzbuzz import FizzBuzz

@pytest.fixture
def fb():
    """Returns a FizzBuzz object."""
    return FizzBuzz()

def test_fizzbuzz(fb):
    """Test basic FizzBuzz functionality."""
    result = fb.fizzbuzz(1, 100)
    # Check first 15 elements
    expected_first_15 = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert result[:15] == expected_first_15
    assert len(result) == 100

def test_invalid_range(fb):
    """Test error handling."""
    with pytest.raises(ValueError, match="Start and end must be integers 1 and 100 respectively"):
        fb.fizzbuzz(2, 100)