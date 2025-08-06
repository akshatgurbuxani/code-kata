from stringsum import StringSum

def test_valid_numbers():
    """Test sum with valid natural numbers."""
    result = StringSum("123", "456").sum()
    assert result == 579

def test_invalid_string():
    """Test sum with one invalid string."""
    result = StringSum("123", "abc").sum()
    assert result == 123

def test_empty_string():
    """Test sum with empty string."""
    result = StringSum("", "456").sum()
    assert result == 456

def test_negative_number():
    """Test sum with negative number."""
    result = StringSum("-5", "10").sum()
    assert result == 10

def test_both_invalid():
    """Test sum with both invalid inputs."""
    result = StringSum("abc", "def").sum()
    assert result == 0
