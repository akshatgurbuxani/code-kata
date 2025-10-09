from operations import Operations
import logging
from calculator_config import CalculatorConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Divide(Operations):
    def __init__(self, config: CalculatorConfig):
        super().__init__(config)

    def name(self) -> str:
        """
        Returns the name of the operation.
        """
        return self.config.operations["divide"].description
    
    def execute(self, a: float, b: float) -> float:
        """
        Executes the operation.
        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The formatted result of the operation.
        """
        if b == 0:
            raise ValueError(self.config.errors.division_by_zero)
        return self.format_result(a / b)