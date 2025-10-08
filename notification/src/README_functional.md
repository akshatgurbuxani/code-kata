# Functional Notification System

This demonstrates a **Functional Programming** approach to the notification system.

## Key Functional Programming Concepts

### 1. **Pure Functions**
- `create_email_message()` - No side effects, same input always produces same output
- `create_sms_message()` - Immutable data processing
- `create_push_message()` - Predictable behavior

### 2. **Immutability**
- `NotificationConfig` is frozen (immutable)
- `update_recipients()` creates new objects instead of modifying existing ones

### 3. **Higher-Order Functions**
- `send_notification()` - Takes function as parameter
- `log_and_send()` - Function composition

### 4. **Partial Application**
- `create_email_sender()` - Creates specialized functions
- `create_sms_sender()` - Pre-configured functions

### 5. **Function Composition**
- `log_and_send()` - Combines logging with sending
- `process_notifications()` - Processes multiple types functionally

## How to Run

### 1. Run the Demo
```bash
cd /Users/akshat/_/dev/code-kata/notification/src
python run_functional_demo.py
```

### 2. Run the Tests
```bash
# Run all tests
pytest test_notification_functional.py -v

# Run specific test class
pytest test_notification_functional.py::TestMessageCreators -v

# Run with coverage
pytest test_notification_functional.py --cov=notification_functional
```

### 3. Run Individual Functions
```python
from notification_functional import *

# Create config
config = NotificationConfig(
    subject="Test",
    body="Test message",
    recipients=["user@test.com"],
    sender="system@test.com"
)

# Test individual functions
email_msg = create_email_message(config)
sms_msg = create_sms_message(config)
push_msg = create_push_message(config)

# Test higher-order function
result = send_notification("email", config)

# Test function composition
logged_result = log_and_send(print, partial(send_notification, "email"), config)

# Test functional processing
all_messages = process_notifications(config, ["email", "sms", "push"])

# Test immutable updates
updated_config = update_recipients(config, ["newuser@test.com"])
```

## Function Reference

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `create_email_message()` | Create email message | `NotificationConfig` | `str` |
| `create_sms_message()` | Create SMS message | `NotificationConfig` | `str` |
| `create_push_message()` | Create push message | `NotificationConfig` | `str` |
| `send_notification()` | Dispatch to message creator | `str, NotificationConfig` | `str` |
| `log_and_send()` | Compose logging with sending | `Callable, Callable, NotificationConfig` | `str` |
| `create_email_sender()` | Create specialized email sender | `NotificationConfig` | `Callable` |
| `create_sms_sender()` | Create specialized SMS sender | `NotificationConfig` | `Callable` |
| `process_notifications()` | Process multiple types | `NotificationConfig, List[str]` | `List[str]` |
| `update_recipients()` | Immutable config update | `NotificationConfig, List[str]` | `NotificationConfig` |
