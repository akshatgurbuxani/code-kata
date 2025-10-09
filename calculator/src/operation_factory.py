from operations import Operations
from calculator_config import CalculatorConfig
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OperationFactory:
    """
    Factory for creating operations.
    """
    def __init__(self, config: CalculatorConfig) -> None:
        self.config = config
        self._operations: dict[str, Operations] = None

    def register(self, operation_type: str, op: Operations) -> None:
        """
        Registers an operation.
        """
        if self._operations is None:
            self._operations = {}
        self._operations[operation_type] = op

    def create_operation(self, operation_type: str) -> Operations:
        """
        Creates an operation.
        Args:
            operation_type (str): The type of operation to create.

        Returns:
            Operations: The created operation.
        """
        if self._operations is None:
            raise ValueError(f"No operations registered")
        if operation_type not in self._operations:
            raise ValueError(f"{self.config.errors.unknown_operation}: {operation_type}")
        return self._operations[operation_type] 
    
    def get_supported_operations(self) -> list[str]:
        """
        Returns the supported operations.
        """
        if self._operations is None:
            raise ValueError(f"No operations registered")
        return list(self._operations.keys())