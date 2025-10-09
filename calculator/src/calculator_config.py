from dataclasses import dataclass
from typing import Optional
import yaml
import os

@dataclass
class OperationConfig:
    """Configuration for a single operation."""
    symbol: str
    description: str

@dataclass
class ErrorMessages:
    """Error messages configuration."""
    division_by_zero: str
    invalid_expression: str
    unmatched_parentheses: str
    unknown_operation: str

@dataclass
class OutputFormat:
    """Output formatting configuration."""
    decimal_places: int
    format_output: bool

@dataclass
class CalculatorConfig:
    """
    Calculator config.
    """
    name: str
    operations: dict[str, OperationConfig]
    errors: ErrorMessages
    output_format: OutputFormat

class CalculatorConfigBuilder:
    """
    Builder for the calculator config.
    """
    def __init__(self):
        self.calculator_config: Optional[CalculatorConfig] = None

    def build_config(self, config: dict) -> 'CalculatorConfigBuilder':
        """
        Builds the calculator config from the given config.
        """
        calculator_config = config.get("calculator")
        if calculator_config:
            # Build operations config
            operations = {}
            for op_name, op_data in calculator_config["operations"].items():
                operations[op_name] = OperationConfig(
                    symbol=op_data["symbol"],
                    description=op_data["description"]
                )
            
            # Build errors config
            errors = ErrorMessages(
                division_by_zero=calculator_config["errors"]["division_by_zero"],
                invalid_expression=calculator_config["errors"]["invalid_expression"],
                unmatched_parentheses=calculator_config["errors"]["unmatched_parentheses"],
                unknown_operation=calculator_config["errors"]["unknown_operation"]
            )
            
            # Build output format config
            output_format = OutputFormat(
                decimal_places=calculator_config["output_format"]["decimal_places"],
                format_output=calculator_config["output_format"]["format_output"]
            )
            
            self.calculator_config = CalculatorConfig(
                name=calculator_config["name"],
                operations=operations,
                errors=errors,
                output_format=output_format
            )
        return self
    
    def get_config(self) -> CalculatorConfig:
        """
        Returns the built calculator config.
        """
        if self.calculator_config is None:
            raise ValueError("Configuration not built yet. Call build_config() first.")
        return self.calculator_config
    
def load_calculator_config(config: dict) -> CalculatorConfig:
    """
    Loads the calculator config from the given config.
    """
    builder = CalculatorConfigBuilder()
    return builder.build_config(config).get_config()

def load_config_from_yaml(yaml_file_path: str) -> dict:
    """
    Loads configuration from a YAML file.
    """
    if not os.path.exists(yaml_file_path):
        raise FileNotFoundError(f"Configuration file not found: {yaml_file_path}")
    
    try:
        with open(yaml_file_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
    except Exception as e:
        raise ValueError(f"Error reading configuration file: {e}")