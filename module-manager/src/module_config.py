from dataclasses import dataclass
from typing import Optional
import os
import yaml


@dataclass
class ModuleConfig:
    """
    Module config.
    """
    name: str
    description: str
    args: dict

class ModuleConfigBuilder:
    """
    Builder for the module config.
    """
    def __init__(self):
        self.module_config: Optional[ModuleConfig] = None

    def build_config(self, config: dict) -> 'ModuleConfigBuilder':
        """
        Builds the module config from the given config.
        """
        module_config = config.get("module_manager")
        if module_config:
            self.module_config = ModuleConfig(
                name=module_config["name"],
                description=module_config["description"],
                args=module_config["args"]
            )
        return self
    
    def get_config(self) -> ModuleConfig:
        """
        Returns the built module config.
        """
        if self.module_config is None:
            raise ValueError("Configuration not built yet. Call build_config() first.")
        return self.module_config
    
def load_module_config(config: dict) -> list[ModuleConfig]:
    """
    Loads all module configs from the given config using the builder pattern.
    """
    module_configs = []
    
    if config.get("module-manager") and config.get("module-manager").get("modules"):
        for module_data in config["module-manager"]["modules"]:
            builder = ModuleConfigBuilder()
            # Create a config dict that matches the builder's expected format
            module_config_dict = {
                "module_manager": module_data
            }
            module_config = builder.build_config(module_config_dict).get_config()
            module_configs.append(module_config)
    
    return module_configs

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