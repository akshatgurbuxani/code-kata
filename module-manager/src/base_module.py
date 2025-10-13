from abc import ABC, abstractmethod
from module_config import ModuleConfig

class BaseModule(ABC):
    """
    Base class for all modules.
    """
    def __init__(self, config: ModuleConfig):
        self.config = config
    
    @abstractmethod
    def name(self) -> str:
        """
        Returns the name of the module.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> str:
        """
        Execute the module.
        """
        pass
