from operations import Operations
from calculator_config import CalculatorConfig
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Add(Operations):
    def __init__(self, config: CalculatorConfig):
        super().__init__(config)

    def name(self) -> str:
        """
        Returns the name of the operation.
        """
        return self.config.operations["add"].description
    
    def execute(self, a: float, b: float) -> float:
        """
        Executes the operation.
        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The formatted result of the operation.
        """
        return self.format_result(a + b)