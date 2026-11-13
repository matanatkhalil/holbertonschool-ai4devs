import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


class TestSingleRequest(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_single_request(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 250"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 1)
        self.assertEqual(result["averageResponseTime"], 250)


if __name__ == "__main__":
    unittest.main()