class StringSum():
    """
    A class that sums two strings and returns the result if they are natural numbers.
    """
    
    def __init__(self, num1: str, num2: str):
        """
        Initializes the StringSum class.

        Args:
            num1 (str): The first number to sum.
            num2 (str): The second number to sum.
        """
        self.num1 = self._validate(num1)
        self.num2 = self._validate(num2)

    def _validate(self, stringnumber: str) -> int:
        """
        Validates the input string and returns the natural number.

        Args:
            stringnumber (str): The input string to validate.

        Returns:
            int: The natural number.
        """
        try:
            natural_number = int(stringnumber)
            if natural_number >= 0:
                return natural_number
            else:
                return 0
        except ValueError:
            return 0
        
    def sum(self) -> int:
        """
        Sums the two numbers and returns the result.

        Returns:
            int: The sum of the two numbers.
        """
        return self.num1 + self.num2