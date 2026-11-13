import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


class TestMixedValidAndInvalidEntries(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_mixed_valid_and_invalid_entries(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 100",
            "INVALID ENTRY",
            "2026-11-13T10:32:00Z POST /api/users 201 200",
            "2026-11-13T10:33:00Z GET /api/products 700 150"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 2)
        self.assertEqual(result["malformedEntries"], 2)
        self.assertEqual(result["averageResponseTime"], 150)


if __name__ == "__main__":
    unittest.main()