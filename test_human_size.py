import unittest

from human_size import human_size


class TestHumanSize(unittest.TestCase):

    def test_human_size_bytes(self):
        bytes = 0
        result = human_size(bytes)
        self.assertEqual(result, '0.0bytes')

    def test_human_size_kb(self):
        bytes = 1 * (10**3)
        result = human_size(bytes)
        self.assertEqual(result, '1.0kB')

    def test_human_size_mb(self):
        bytes = 1 * (10**6)
        result = human_size(bytes)
        self.assertEqual(result, '1.0MB')

    def test_human_size_gb(self):
        bytes = 1 * (10**9)
        result = human_size(bytes)
        self.assertEqual(result, '1.0GB')

    def test_human_size_yb(self):
        bytes = 5120 * (10**24)
        result = human_size(bytes)
        self.assertEqual(result, '5120.0YB')
