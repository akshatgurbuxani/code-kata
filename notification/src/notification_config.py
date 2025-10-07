from dataclasses import dataclass
from typing import Optional
import yaml
import os


@dataclass
class NotificationDataConfig:
    """
    Notification config.
    """
    subject: str
    body: str
    recipients: list[str]
    sender: str


class NotificationDataConfigBuilder:
    """
    Builder for the notification config.
    """
    def __init__(self):
        self.notification_config: Optional[NotificationDataConfig] = None

    def build_config(self, config: dict) -> 'NotificationDataConfigBuilder':
        """
        Builds the notification config from the given config.
        """
        notification_data_config = config.get("notification_data_config")
        if notification_data_config:
            self.notification_config = NotificationDataConfig(
                subject=notification_data_config["subject"],
                body=notification_data_config["body"],
                recipients=notification_data_config["recipients"],
                sender=notification_data_config["sender"]
            )
        return self
    
    def get_config(self) -> NotificationDataConfig:
        """
        Returns the built notification config.
        """
        if self.notification_config is None:
            raise ValueError("Configuration not built yet. Call build_config() first.")
        return self.notification_config


def load_notification_config(config: dict) -> NotificationDataConfig:
    """
    Loads the notification config from the given config.
    """
    builder = NotificationDataConfigBuilder()
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