from base_module import BaseModule
from module_config import load_module_config, load_config_from_yaml
from module_factory import ModuleFactory

class ModuleManager:
    def __init__(self, config_path: str):
        self.configs = load_module_config(load_config_from_yaml(config_path))
        self.modules: list[BaseModule] = []
        self._auto_register_modules()

    def _auto_register_modules(self):
        """Automatically register modules using the factory pattern."""
        for config in self.configs:
            module = ModuleFactory.create_module(config)
            self.modules.append(module)

    def register_module(self, module: BaseModule):
        self.modules.append(module)

    def execute_module(self, module_name: str, **kwargs):
        for module in self.modules:
            if module.name() == module_name:
                return module.execute(**kwargs)

    def get_module(self, module_name: str) -> BaseModule:
        for module in self.modules:
            if module.name() == module_name:
                return module
        raise ValueError(f"Module {module_name} not found")
    
    def get_modules(self) -> list[BaseModule]:
        return self.modules