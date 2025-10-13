from base_module import BaseModule
from module_config import ModuleConfig
from services.greet import Greet
from services.echo import Echo
from services.date import Date


class ModuleFactory:
    """
    Factory for creating modules based on their configuration.
    """
    
    _module_registry = {
        "greet": Greet,
        "echo": Echo,
        "date": Date,
    }
    
    @classmethod
    def create_module(cls, config: ModuleConfig) -> BaseModule:
        """
        Create a module instance based on the configuration.
        """
        module_class = cls._module_registry.get(config.name)
        if not module_class:
            raise ValueError(f"Unknown module type: {config.name}")
        
        return module_class(config)
    
    @classmethod
    def register_module(cls, name: str, module_class: type):
        """
        Register a new module type.
        """
        cls._module_registry[name] = module_class
