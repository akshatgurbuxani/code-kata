from calculator_config import load_config_from_yaml, load_calculator_config
from operation_factory import OperationFactory
from add import Add
from substract import Substract
from mul import Multiply
from divide import Divide
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self, config_path: str):
        self.config = load_calculator_config(load_config_from_yaml(config_path))
        self.factory = OperationFactory(self.config)
        self._register_operations()
    
    def _register_operations(self):
        """Register all available operations with the factory."""
        # Register each operation with the full CalculatorConfig
        for op_name in self.config.operations.keys():
            if op_name == "add":
                operation = Add(self.config)
            elif op_name == "subtract":
                operation = Substract(self.config)
            elif op_name == "multiply":
                operation = Multiply(self.config)
            elif op_name == "divide":
                operation = Divide(self.config)
            else:
                continue
            
            # Use the proper register function
            self.factory.register(op_name, operation)
    
    def calculate(self, operation: str, a: float, b: float) -> float:
        """Calculate the result of an operation."""
        try:
            operation_obj = self.factory.create_operation(operation)
            return operation_obj.execute(a, b)
        except Exception as e:
            logger.error(f"Error in calculation: {e}")
            raise
    
    def get_supported_operations(self) -> list[str]:
        """Get list of supported operations."""
        return self.factory.get_supported_operations()
