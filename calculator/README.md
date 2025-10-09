# Calculator Kata

A programming kata that implements a simple two-input calculator with proper configuration management and operation factory pattern.

## Rules

Create a calculator system with the following components:

- **Two-input operations** only (simple arithmetic)
- **YAML configuration** for operations, errors, and output formatting
- **Factory pattern** for operation creation and registration
- **Proper type safety** with dataclasses instead of dictionaries
- Support for addition, subtraction, multiplication, and division
- Configurable decimal precision and error handling

## Example Output

```
# Basic operations
calculator.calculate("add", 5.0, 3.0)      # 8.0
calculator.calculate("subtract", 10.0, 4.0) # 6.0
calculator.calculate("multiply", 3.0, 4.0)  # 12.0
calculator.calculate("divide", 15.0, 3.0)   # 5.0

# Decimal precision (configured in YAML)
calculator.calculate("divide", 10.0, 3.0)   # 3.33 (rounded to 2 decimal places)

# Get supported operations
calculator.get_supported_operations()       # ['add', 'subtract', 'multiply', 'divide']
```

## Run

```bash
python src/test_calculator_e2e.py
```

## Test

```bash
python src/test_calculator_e2e.py
```