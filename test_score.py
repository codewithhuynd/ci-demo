import unittest
from score import is_valid_score


class TestScoreValidation(unittest.TestCase):
    def test_valid_normal_score(self):
        self.assertTrue(is_valid_score(7.5))

    def test_valid_boundaries(self):
        self.assertTrue(is_valid_score(0))
        self.assertTrue(is_valid_score(10))

    def test_below_min_boundary(self):
        self.assertFalse(is_valid_score(-0.5))

    def test_above_max_boundary(self):
        self.assertFalse(is_valid_score(10.5))

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            is_valid_score("8")
