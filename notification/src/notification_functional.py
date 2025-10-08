"""
Functional Programming approach to notification system.
Focuses on pure functions, immutability, and function composition.
"""

import logging
from typing import Callable
from dataclasses import dataclass
from functools import partial

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass(frozen=True)  # Immutable
class NotificationConfig:
    """Immutable configuration data."""
    subject: str
    body: str
    recipients: list[str]
    sender: str

# Functions
def create_email_message(config: NotificationConfig) -> str:
    """Create email message."""
    return f"Sending email to {config.recipients} with subject '{config.subject}' and body '{config.body}' from {config.sender}"


def create_sms_message(config: NotificationConfig) -> str:
    """Create SMS message."""
    return f"Sending SMS to {config.recipients} with message '{config.body}' from {config.sender}"


def create_push_message(config: NotificationConfig) -> str:
    """Create push notification message."""
    return f"Sending push notification to {config.recipients} with title '{config.subject}' and message '{config.body}'"


# Higher-order function - takes function as parameter
def send_notification(notification_type: str, config: NotificationConfig) -> str:
    """Dispatches to appropriate message creator."""
    message_creators = {
        "email": create_email_message,
        "sms": create_sms_message,
        "push": create_push_message
    }
    
    if notification_type not in message_creators:
        raise ValueError(f"Unknown notification type: {notification_type}")
    
    return message_creators[notification_type](config)


# Function composition - combining functions
def log_and_send(logger_func: Callable, send_func: Callable, config: NotificationConfig) -> str:
    """Compose logging with sending."""
    message = send_func(config)
    logger_func(message)
    return message


# Partial application - creating specialized functions
def create_email_sender(config: NotificationConfig) -> Callable:
    """Create a specialized email sender function."""
    return partial(send_notification, "email", config)


def create_sms_sender(config: NotificationConfig) -> Callable:
    """Create a specialized SMS sender function."""
    return partial(send_notification, "sms", config)


# Functional approach to processing multiple notifications
def process_notifications(config: NotificationConfig, types: list[str]) -> list[str]:
    """Process multiple notification types functionally."""
    return [send_notification(notif_type, config) for notif_type in types]


# Immutable data transformation
def update_recipients(config: NotificationConfig, new_recipients: list[str]) -> NotificationConfig:
    """Create new config with updated recipients (immutable update)."""
    return NotificationConfig(
        subject=config.subject,
        body=config.body,
        recipients=new_recipients,
        sender=config.sender
    )


# Example usage
if __name__ == "__main__":
    config = NotificationConfig(
        subject="Test Alert",
        body="This is a test notification",
        recipients=["user@test.com"],
        sender="system@test.com"
    )
    
    # Pure function calls
    email_msg = create_email_message(config)
    sms_msg = create_sms_message(config)
    
    # Higher-order function
    push_msg = send_notification("push", config)
    
    # Function composition
    logged_email = log_and_send(logger.info, partial(send_notification, "email"), config)
    
    # Process multiple types functionally
    all_messages = process_notifications(config, ["email", "sms", "push"])
