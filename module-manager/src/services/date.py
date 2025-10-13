from base_module import BaseModule
from module_config import ModuleConfig
from datetime import datetime

class Date(BaseModule):
    def __init__(self, config: ModuleConfig):
        super().__init__(config)

    def name(self) -> str:
        return self.config.name

    def execute(self, **kwargs) -> str:
        return datetime.now().strftime("%Y-%m-%d")