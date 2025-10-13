import pytest
import os
import sys
from datetime import datetime
from unittest.mock import patch

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from module_manager import ModuleManager
from module_config import load_config_from_yaml
from services.greet import Greet
from services.echo import Echo
from services.date import Date


class TestModuleManagerE2E:
    """End-to-end tests for the module manager system."""
    
    @pytest.fixture
    def config_path(self):
        """Path to the test configuration file."""
        return os.path.join(os.path.dirname(__file__), "config.yaml")
    
    @pytest.fixture
    def module_manager(self, config_path):
        """Create a module manager with all modules automatically registered."""
        return ModuleManager(config_path)
    
    def test_greet_module_e2e(self, module_manager):
        """Test the greet module end-to-end."""
        # Test with the configured greeting
        result = module_manager.execute_module("greet", greeting="Hello Akshat how are you!?")
        assert result == "Hello Akshat how are you!?"
        
        # Test with a custom greeting
        result = module_manager.execute_module("greet", greeting="Hi there!")
        assert result == "Hi there!"
    
    def test_echo_module_e2e(self, module_manager):
        """Test the echo module end-to-end."""
        # Test with a simple message
        result = module_manager.execute_module("echo", message="Hello World!")
        assert result == "Hello World!"
        
        # Test with a longer message
        result = module_manager.execute_module("echo", message="This is a test message for the echo module.")
        assert result == "This is a test message for the echo module."
    
    def test_date_module_e2e(self, module_manager):
        """Test the date module end-to-end."""
        # Test that the date module returns a valid date string
        result = module_manager.execute_module("date")
        
        # Verify it's a valid date string in YYYY-MM-DD format
        assert isinstance(result, str)
        assert len(result) == 10  # YYYY-MM-DD format
        assert result.count('-') == 2
        
        # Verify it's a valid date
        parsed_date = datetime.strptime(result, "%Y-%m-%d")
        assert parsed_date is not None
        
        # Verify it's today's date (within reasonable bounds)
        today = datetime.now().date()
        result_date = parsed_date.date()
        assert result_date == today
    
    def test_module_registration(self, module_manager):
        """Test that all modules are properly registered."""
        modules = module_manager.get_modules()
        module_names = [module.name() for module in modules]
        
        assert "greet" in module_names
        assert "echo" in module_names
        assert "date" in module_names
        assert len(modules) == 3
    
    def test_get_module(self, module_manager):
        """Test getting individual modules."""
        greet_module = module_manager.get_module("greet")
        assert greet_module.name() == "greet"
        assert isinstance(greet_module, Greet)
        
        echo_module = module_manager.get_module("echo")
        assert echo_module.name() == "echo"
        assert isinstance(echo_module, Echo)
        
        date_module = module_manager.get_module("date")
        assert date_module.name() == "date"
        assert isinstance(date_module, Date)
    
    def test_module_not_found(self, module_manager):
        """Test that getting a non-existent module raises an error."""
        with pytest.raises(ValueError, match="Module nonexistent not found"):
            module_manager.get_module("nonexistent")
    
    def test_execute_nonexistent_module(self, module_manager):
        """Test that executing a non-existent module returns None."""
        result = module_manager.execute_module("nonexistent")
        assert result is None
    
    def test_config_loading(self, config_path):
        """Test that the configuration file loads correctly."""
        config = load_config_from_yaml(config_path)
        
        assert "module-manager" in config
        assert "modules" in config["module-manager"]
        assert len(config["module-manager"]["modules"]) == 3
        
        # Verify all expected modules are in the config
        module_names = [module["name"] for module in config["module-manager"]["modules"]]
        assert "greet" in module_names
        assert "echo" in module_names
        assert "date" in module_names
    
    def test_greet_module_with_template_substitution(self, module_manager):
        """Test that the greet module can handle template substitution."""
        # Test with the configured template
        result = module_manager.execute_module("greet", greeting="Hello {name} how are you!?")
        assert result == "Hello {name} how are you!?"
        
        # Test with actual substitution (if the module supported it)
        result = module_manager.execute_module("greet", greeting="Hello Akshat how are you!?")
        assert result == "Hello Akshat how are you!?"
    
    def test_echo_module_with_special_characters(self, module_manager):
        """Test that the echo module handles special characters correctly."""
        special_messages = [
            "Hello, World!",
            "Test with numbers: 12345",
            "Special chars: !@#$%^&*()",
            "Unicode: 你好世界",
            "Newlines:\nTest",
            "Tabs:\tTest"
        ]
        
        for message in special_messages:
            result = module_manager.execute_module("echo", message=message)
            assert result == message
    
    @patch('services.date.datetime')
    def test_date_module_with_mocked_date(self, mock_datetime, module_manager):
        """Test the date module with a mocked date."""
        # Mock the datetime to return a specific date
        mock_datetime.now.return_value.strftime.return_value = "2024-01-15"
        
        result = module_manager.execute_module("date")
        assert result == "2024-01-15"
        mock_datetime.now.return_value.strftime.assert_called_once_with("%Y-%m-%d")


if __name__ == "__main__":
    pytest.main([__file__])
