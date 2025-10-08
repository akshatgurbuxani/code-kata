#!/usr/bin/env python3
"""
Comprehensive test suite for the functional notification system.
Tests each function and demonstrates functional programming concepts.
"""

import pytest
from functools import partial
from notification_functional import (
    NotificationConfig,
    create_email_message,
    create_sms_message,
    create_push_message,
    send_notification,
    log_and_send,
    create_email_sender,
    create_sms_sender,
    process_notifications,
    update_recipients
)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestNotificationConfig:
    """Test the immutable configuration data structure."""
    
    def test_config_creation(self):
        """Test creating a notification config."""
        config = NotificationConfig(
            subject="Test Subject",
            body="Test Body",
            recipients=["user@test.com"],
            sender="system@test.com"
        )
        
        assert config.subject == "Test Subject"
        assert config.body == "Test Body"
        assert config.recipients == ["user@test.com"]
        assert config.sender == "system@test.com"
    
    def test_config_immutability(self):
        """Test that config is immutable (frozen dataclass)."""
        config = NotificationConfig(
            subject="Test",
            body="Test",
            recipients=["user@test.com"],
            sender="system@test.com"
        )
        
        # Should raise AttributeError when trying to modify
        with pytest.raises(AttributeError):
            config.subject = "Modified"


class TestMessageCreators:
    """Test the pure message creation functions."""
    
    @pytest.fixture
    def sample_config(self):
        """Sample configuration for testing."""
        return NotificationConfig(
            subject="Test Alert",
            body="This is a test notification",
            recipients=["user@test.com", "admin@test.com"],
            sender="system@test.com"
        )
    
    def test_create_email_message(self, sample_config):
        """Test email message creation."""
        message = create_email_message(sample_config)
        
        assert "Sending email to" in message
        assert "Test Alert" in message
        assert "This is a test notification" in message
        assert "system@test.com" in message
        assert "user@test.com" in message
    
    def test_create_sms_message(self, sample_config):
        """Test SMS message creation."""
        message = create_sms_message(sample_config)
        
        assert "Sending SMS to" in message
        assert "This is a test notification" in message
        assert "system@test.com" in message
        assert "user@test.com" in message
    
    def test_create_push_message(self, sample_config):
        """Test push notification message creation."""
        message = create_push_message(sample_config)
        
        assert "Sending push notification to" in message
        assert "Test Alert" in message
        assert "This is a test notification" in message
        assert "user@test.com" in message


class TestHigherOrderFunctions:
    """Test higher-order functions and function composition."""
    
    @pytest.fixture
    def sample_config(self):
        """Sample configuration for testing."""
        return NotificationConfig(
            subject="Test Alert",
            body="This is a test notification",
            recipients=["user@test.com"],
            sender="system@test.com"
        )
    
    def test_send_notification_email(self, sample_config):
        """Test sending email notification."""
        message = send_notification("email", sample_config)
        
        assert "Sending email to" in message
        assert "Test Alert" in message
    
    def test_send_notification_sms(self, sample_config):
        """Test sending SMS notification."""
        message = send_notification("sms", sample_config)
        
        assert "Sending SMS to" in message
        assert "This is a test notification" in message
    
    def test_send_notification_push(self, sample_config):
        """Test sending push notification."""
        message = send_notification("push", sample_config)
        
        assert "Sending push notification to" in message
        assert "Test Alert" in message
    
    def test_send_notification_invalid_type(self, sample_config):
        """Test error handling for invalid notification type."""
        with pytest.raises(ValueError, match="Unknown notification type"):
            send_notification("invalid", sample_config)
    
    def test_log_and_send_composition(self, sample_config):
        """Test function composition with logging."""
        logged_messages = []
        
        def mock_logger(message):
            logged_messages.append(message)
        
        # Compose logging with email sending
        result = log_and_send(
            mock_logger,
            partial(send_notification, "email"),
            sample_config
        )
        
        assert len(logged_messages) == 1
        assert logged_messages[0] == result
        assert "Sending email to" in result


class TestPartialApplication:
    """Test partial application creating specialized functions."""
    
    @pytest.fixture
    def sample_config(self):
        """Sample configuration for testing."""
        return NotificationConfig(
            subject="Test Alert",
            body="This is a test notification",
            recipients=["user@test.com"],
            sender="system@test.com"
        )
    
    def test_create_email_sender(self, sample_config):
        """Test creating specialized email sender function."""
        email_sender = create_email_sender(sample_config)
        
        # The returned function should work without parameters
        message = email_sender()
        
        assert "Sending email to" in message
        assert "Test Alert" in message
    
    def test_create_sms_sender(self, sample_config):
        """Test creating specialized SMS sender function."""
        sms_sender = create_sms_sender(sample_config)
        
        # The returned function should work without parameters
        message = sms_sender()
        
        assert "Sending SMS to" in message
        assert "This is a test notification" in message


class TestFunctionalProcessing:
    """Test functional approaches to processing multiple notifications."""
    
    @pytest.fixture
    def sample_config(self):
        """Sample configuration for testing."""
        return NotificationConfig(
            subject="Test Alert",
            body="This is a test notification",
            recipients=["user@test.com"],
            sender="system@test.com"
        )
    
    def test_process_notifications_all_types(self, sample_config):
        """Test processing all notification types functionally."""
        messages = process_notifications(sample_config, ["email", "sms", "push"])
        
        assert len(messages) == 3
        assert "Sending email to" in messages[0]
        assert "Sending SMS to" in messages[1]
        assert "Sending push notification to" in messages[2]
    
    def test_process_notifications_subset(self, sample_config):
        """Test processing a subset of notification types."""
        messages = process_notifications(sample_config, ["email", "push"])
        
        assert len(messages) == 2
        assert "Sending email to" in messages[0]
        assert "Sending push notification to" in messages[1]
    
    def test_process_notifications_empty_list(self, sample_config):
        """Test processing empty notification types list."""
        messages = process_notifications(sample_config, [])
        
        assert len(messages) == 0


class TestImmutableDataTransformation:
    """Test immutable data transformations."""
    
    @pytest.fixture
    def sample_config(self):
        """Sample configuration for testing."""
        return NotificationConfig(
            subject="Test Alert",
            body="This is a test notification",
            recipients=["user@test.com"],
            sender="system@test.com"
        )
    
    def test_update_recipients(self, sample_config):
        """Test immutable update of recipients."""
        new_recipients = ["newuser@test.com", "admin@test.com"]
        updated_config = update_recipients(sample_config, new_recipients)
        
        # Original config should be unchanged
        assert sample_config.recipients == ["user@test.com"]
        assert sample_config.subject == "Test Alert"
        
        # New config should have updated recipients
        assert updated_config.recipients == new_recipients
        assert updated_config.subject == "Test Alert"  # Other fields unchanged
        assert updated_config.body == "This is a test notification"
        assert updated_config.sender == "system@test.com"
    
    def test_update_recipients_immutability(self, sample_config):
        """Test that update_recipients creates a new object."""
        new_recipients = ["newuser@test.com"]
        updated_config = update_recipients(sample_config, new_recipients)
        
        # Should be different objects
        assert updated_config is not sample_config
        
        # Original should be unchanged
        assert sample_config.recipients == ["user@test.com"]


class TestFunctionalWorkflow:
    """Test complete functional workflow end-to-end."""
    
    def test_complete_functional_workflow(self):
        """Test complete functional workflow from start to finish."""
        # 1. Create initial configuration
        config = NotificationConfig(
            subject="System Alert",
            body="Server is down",
            recipients=["admin@company.com"],
            sender="monitoring@company.com"
        )
        
        # 2. Test individual message creators
        email_msg = create_email_message(config)
        sms_msg = create_sms_message(config)
        push_msg = create_push_message(config)
        
        assert "Sending email to" in email_msg
        assert "Sending SMS to" in sms_msg
        assert "Sending push notification to" in push_msg
        
        # 3. Test higher-order function
        email_via_hof = send_notification("email", config)
        assert email_msg == email_via_hof
        
        # 4. Test function composition with logging
        logged_messages = []
        def mock_logger(msg):
            logged_messages.append(msg)
        
        logged_result = log_and_send(
            mock_logger,
            partial(send_notification, "sms"),
            config
        )
        
        assert len(logged_messages) == 1
        assert logged_result == sms_msg
        
        # 5. Test partial application
        email_sender = create_email_sender(config)
        specialized_result = email_sender()
        assert specialized_result == email_msg
        
        # 6. Test functional processing
        all_messages = process_notifications(config, ["email", "sms", "push"])
        assert len(all_messages) == 3
        assert all_messages[0] == email_msg
        assert all_messages[1] == sms_msg
        assert all_messages[2] == push_msg
        
        # 7. Test immutable data transformation
        new_recipients = ["admin@company.com", "manager@company.com"]
        updated_config = update_recipients(config, new_recipients)
        
        # Original unchanged
        assert config.recipients == ["admin@company.com"]
        
        # New config with updated recipients
        updated_messages = process_notifications(updated_config, ["email"])
        assert "manager@company.com" in updated_messages[0]
        
        logger.info({
            "original_config": config,
            "updated_config": updated_config,
            "all_messages": all_messages,
            "logged_messages": logged_messages
        })


def test_functional_programming_principles():
    """Test that our functions follow functional programming principles."""
    
    # Test pure functions (same input, same output)
    config = NotificationConfig(
        subject="Test",
        body="Test",
        recipients=["user@test.com"],
        sender="system@test.com"
    )
    
    # Multiple calls should produce identical results
    result1 = create_email_message(config)
    result2 = create_email_message(config)
    assert result1 == result2
    
    # Test immutability
    original_recipients = config.recipients.copy()
    updated_config = update_recipients(config, ["new@test.com"])
    
    # Original should be unchanged
    assert config.recipients == original_recipients
    assert updated_config.recipients == ["new@test.com"]


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
