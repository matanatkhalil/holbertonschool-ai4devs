import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


class TestZeroResponseTime(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_zero_response_time(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 0"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 1)
        self.assertEqual(result["averageResponseTime"], 0)
        self.assertEqual(result["malformedEntries"], 0)


if __name__ == "__main__":
    unittest.main()