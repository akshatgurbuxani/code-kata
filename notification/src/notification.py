from abc import ABC, abstractmethod
from typing import Optional
import logging

from notification_config import load_notification_config, NotificationDataConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Notification(ABC):
    def __init__(self, config: NotificationDataConfig):
        self.config = config
    
    @abstractmethod
    def send(self) -> str:
        pass


class EmailNotification(Notification):
    def send(self) -> str:
        message = f"Sending email to {self.config.recipients} with subject '{self.config.subject}' and body '{self.config.body}' from {self.config.sender}"
        logger.info(message)
        return message


class SMSNotification(Notification):
    def send(self) -> str:
        message = f"Sending SMS to {self.config.recipients} with message '{self.config.body}' from {self.config.sender}"
        logger.info(message)
        return message


class PushNotification(Notification):
    def send(self) -> str:
        message = f"Sending push notification to {self.config.recipients} with title '{self.config.subject}' and message '{self.config.body}'"
        logger.info(message)
        return message


class NotificationFactory:
    def __init__(self, config: dict):
        self.config = load_notification_config(config)

    def create_notification(self, notification_type: str) -> Optional[Notification]:
        if notification_type == "email":
            return EmailNotification(self.config)
        elif notification_type == "sms":
            return SMSNotification(self.config)
        elif notification_type == "push":
            return PushNotification(self.config)
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
    
    def get_supported_types(self) -> list[str]:
        return ["email", "sms", "push"]