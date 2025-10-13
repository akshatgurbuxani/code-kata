# Module Manager Kata

A programming kata that implements a flexible module management system with YAML configuration, factory pattern, and builder pattern for dynamic module loading and execution.

## Rules

Create a module management system with the following components:

- **YAML Configuration**: Define modules and their arguments in a configuration file
- **Builder Pattern**: Use `ModuleConfigBuilder` for creating module configurations
- **Factory Pattern**: Use `ModuleFactory` for creating module instances
- **Dynamic Loading**: Automatically register and load modules from configuration
- **Type Safety**: Full type hints and proper inheritance with `BaseModule`
- **Extensible**: Easy to add new modules by registering them in the factory

## Features

- **Multiple Module Types**: Greet, Echo, and Date modules
- **Configuration Management**: YAML-based configuration with validation
- **Builder Pattern**: `ModuleConfigBuilder` for creating module configurations
- **Factory Pattern**: `ModuleFactory` for creating module instances
- **Auto-Registration**: Modules are automatically registered from configuration
- **Type Safety**: Full type hints and proper inheritance
- **Extensible**: Easy to add new modules without changing core code

## Example Output

```python
from module_manager import ModuleManager

# Create module manager (automatically loads and registers modules)
manager = ModuleManager('config.yaml')

# Get available modules
print(manager.get_modules())  # [<Greet>, <Echo>, <Date>]

# Execute modules
result = manager.execute_module('greet', greeting='Hello World!')
print(result)  # Hello World!

result = manager.execute_module('echo', message='Test message')
print(result)  # Test message

result = manager.execute_module('date')
print(result)  # 2024-01-15
```

## Configuration

The system uses a YAML configuration file with the following structure:

```yaml
module-manager:
  modules:
    - name: greet
      description: "Greet the user"
      args:
        name: "Akshat"
        greeting: "Hello {name} how are you!?"
    - name: echo
      description: "Echo the user's message"
      args:
        message: "{message}"
    - name: date
      description: "Get the current date"
      args: {}
```

## Architecture

### Core Components

- **`BaseModule`**: Abstract base class for all modules
- **`ModuleConfig`**: Data class for module configuration
- **`ModuleConfigBuilder`**: Builder pattern for creating module configurations
- **`ModuleFactory`**: Factory pattern for creating module instances
- **`ModuleManager`**: Main class that manages and executes modules

### Module Structure

```
src/
├── base_module.py          # Abstract base class
├── module_config.py        # Configuration and builder
├── module_factory.py       # Factory for module creation
├── module_manager.py       # Main manager class
├── config.yaml            # Module configuration
├── services/              # Module implementations
│   ├── greet.py
│   ├── echo.py
│   └── date.py
└── test_module_manager_e2e.py  # End-to-end tests
```

## Run

```bash
python src/module_manager.py
```

## Test

```bash
pytest src/test_module_manager_e2e.py -v
```

## Adding New Modules

1. Create a new module class in `services/` directory
2. Inherit from `BaseModule`
3. Implement `name()` and `execute()` methods
4. Register the module in `ModuleFactory._module_registry`
5. Add module configuration to `config.yaml`
