#!/usr/bin/env python3
"""
Simple test for the notification system workflow.
"""

import pytest
from notification import NotificationFactory


def test_notification_workflow():
    """Test complete notification workflow with all types."""
    
    # Sample configuration data
    config_data = {
        "notification_data_config": {
            "subject": "Test Alert",
            "body": "This is a test notification",
            "recipients": ["user@test.com", "admin@test.com"],
            "sender": "system@test.com"
        }
    }
    
    # Create factory
    factory = NotificationFactory(config_data)
    
    # Test supported types
    supported_types = factory.get_supported_types()
    assert set(supported_types) == {"email", "sms", "push"}
    
    # Test each notification type and collect messages
    messages = []
    for notif_type in ["email", "sms", "push"]:
        notification = factory.create_notification(notif_type)
        assert notification is not None
        message = notification.send()
        messages.append(message)
    
    # Verify messages contain expected content
    all_messages = " ".join(messages)
    assert "Sending email to" in all_messages
    assert "Sending SMS to" in all_messages
    assert "Sending push notification to" in all_messages
    assert "Test Alert" in all_messages
    assert "This is a test notification" in all_messages
    
    # Test error handling for unknown type
    with pytest.raises(ValueError):
        factory.create_notification("unknown")