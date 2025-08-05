class FizzBuzz:
    def __init__(self):
        pass

    def _valid(self, start: int, end: int) -> bool:
        """
        Validates that the start and end are 1 and 100 respectively.

        Args:
            start (int): The start of the range.
            end (int): The end of the range.

        Returns:
            bool: True if the start and end are 1 and 100 respectively, False otherwise.
        """
        return start == 1 and end == 100

    def _fizzbuzz(self, number: int) -> str:
        """
        Returns the FizzBuzz value for a given number.

        Args:
            number (int): The number to get the FizzBuzz value for.

        Returns:
            str: The FizzBuzz value for the given number.
        """
        if number % 3 == 0:
            if number % 5 == 0:
                return "FizzBuzz"
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return str(number)
    
    def fizzbuzz(self, start: int, end: int) -> list[str]:
        """
        Returns the FizzBuzz list for a given range.

        Args:
            start (int): The start of the range.
            end (int): The end of the range.

        Returns:
            list[str]: The FizzBuzz list for the given range.
        """
        if not self._valid(start, end):
            raise ValueError("Start and end must be integers 1 and 100 respectively")
        return [self._fizzbuzz(i) for i in range(start, end + 1)]
    
if __name__ == "__main__":
    fizzbuzz = FizzBuzz()
    print(fizzbuzz.fizzbuzz(1, 100))