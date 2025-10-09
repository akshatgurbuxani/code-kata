from abc import ABC, abstractmethod
from calculator_config import CalculatorConfig
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Operations(ABC):
    def __init__(self, config: CalculatorConfig):
        self.config = config

    @abstractmethod
    def name(self) -> str:
        """
        Returns the name of the operation.
        """
        pass
    
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        """
        Executes an operation.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the operation.
        """
        pass
    
    def format_result(self, result: float) -> float:
        """
        Formats the result of the operation.

        Args:
            result (float): The result of the operation.

        Returns:
            float: The formatted result.
        """
        if self.config.output_format.format_output:
            return round(result, self.config.output_format.decimal_places)
        else:
            return result