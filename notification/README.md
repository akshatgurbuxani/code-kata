# Notification System

A flexible notification system supporting multiple notification types (Email, SMS, Push) with configuration management and proper error handling.

## Features

- **Multiple Notification Types**: Email, SMS, and Push notifications
- **Configuration Management**: YAML-based configuration with validation
- **Factory Pattern**: Easy creation of notification instances
- **Type Safety**: Full type hints and proper inheritance
- **Extensible**: Easy to add new notification types

## Usage

```python
from notification import NotificationFactory
from notification_config import load_config_from_yaml

# Load configuration from YAML file
config = load_config_from_yaml("notification_config.yaml")

# Create factory
factory = NotificationFactory(config)

# Create and send notifications
email_notification = factory.create_notification("email")
email_notification.send("Your custom message here")

sms_notification = factory.create_notification("sms")
sms_notification.send("SMS message")

push_notification = factory.create_notification("push")
push_notification.send("Push notification message")
```

### Configuration

The system uses a YAML configuration file with the following structure:

```yaml
notification_data_config:
  email:
    subject: "Email Subject"
    body: "Default email body"
    recipients: ["user@example.com"]
    sender: "sender@example.com"
  sms:
    subject: "SMS Subject"
    body: "Default SMS message"
    recipients: ["1234567890"]
    sender: "1234567890"
  push:
    subject: "Push Title"
    body: "Default push message"
    recipients: ["device_id"]
    sender: "app_name"
```

## Running the Demo

```bash
python notification.py
```

## Running Tests

```bash
pytest test_notification.py -v
```