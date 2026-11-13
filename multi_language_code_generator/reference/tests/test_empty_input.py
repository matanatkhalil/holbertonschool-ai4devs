import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


class TestEmptyInput(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_empty_input(self):
        result = self.analyzer.analyze([])

        self.assertEqual(result["totalRequests"], 0)
        self.assertEqual(result["errorRate"], 0)
        self.assertEqual(result["mostRequestedEndpoint"], None)


if __name__ == "__main__":
    unittest.main()