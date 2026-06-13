# test_coinstorm.py
"""
Tests for CoinStorm module.
"""

import unittest
from coinstorm import CoinStorm

class TestCoinStorm(unittest.TestCase):
    """Test cases for CoinStorm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinStorm()
        self.assertIsInstance(instance, CoinStorm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinStorm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
