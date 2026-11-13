import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


class TestAllRequestsAreErrors(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_all_requests_are_errors(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 404 100",
            "2026-11-13T10:31:00Z POST /api/users 500 200",
            "2026-11-13T10:32:00Z GET /api/products 503 300"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["errorRate"], 100)


if __name__ == "__main__":
    unittest.main()