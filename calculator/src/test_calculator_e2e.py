#!/usr/bin/env python3
"""
End-to-end test for the Simple Two-Input Calculator
Tests all 4 basic operations with real config loading and calculation.
"""

import unittest
import os
from calculator import Calculator

class TestCalculatorE2E(unittest.TestCase):
    """End-to-end tests for the calculator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.config_path = "src/calculator.yaml"
        self.calculator = Calculator(self.config_path)
    
    def test_addition_e2e(self):
        """Test addition end-to-end."""
        result = self.calculator.calculate("add", 5.0, 3.0)
        self.assertEqual(result, 8.0)
        print(f"✓ Addition: 5 + 3 = {result}")
    
    def test_subtraction_e2e(self):
        """Test subtraction end-to-end."""
        result = self.calculator.calculate("subtract", 10.0, 4.0)
        self.assertEqual(result, 6.0)
        print(f"✓ Subtraction: 10 - 4 = {result}")
    
    def test_multiplication_e2e(self):
        """Test multiplication end-to-end."""
        result = self.calculator.calculate("multiply", 3.0, 4.0)
        self.assertEqual(result, 12.0)
        print(f"✓ Multiplication: 3 * 4 = {result}")
    
    def test_division_e2e(self):
        """Test division end-to-end."""
        result = self.calculator.calculate("divide", 15.0, 3.0)
        self.assertEqual(result, 5.0)
        print(f"✓ Division: 15 / 3 = {result}")
    
    def test_decimal_precision_e2e(self):
        """Test decimal precision from output_format."""
        result = self.calculator.calculate("divide", 10.0, 3.0)
        # Should be rounded to 2 decimal places as per config
        self.assertEqual(result, 3.33)
        print(f"✓ Decimal precision: 10 / 3 = {result} (rounded to 2 decimal places)")
    
    def test_all_operations_workflow(self):
        """Test complete workflow with all operations."""
        print("\n=== Complete Calculator Workflow ===")
        
        # Test all operations in sequence
        operations = [
            ("add", 2.5, 3.7, 6.2),
            ("subtract", 8.9, 2.1, 6.8),
            ("multiply", 4.2, 3.0, 12.6),
            ("divide", 15.6, 2.0, 7.8)
        ]
        
        for op_name, a, b, expected in operations:
            result = self.calculator.calculate(op_name, a, b)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"✓ {op_name.capitalize()}: {a} {op_name} {b} = {result}")

def run_e2e_tests():
    """Run all end-to-end tests."""
    print("Starting End-to-End Calculator Tests...")
    print("=" * 50)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorE2E)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("🎉 All end-to-end tests passed!")
    else:
        print("❌ Some tests failed!")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_e2e_tests()
