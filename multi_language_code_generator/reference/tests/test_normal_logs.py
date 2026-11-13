import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


class TestNormalLogs(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_normal_logs(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 120",
            "2026-11-13T10:31:00Z POST /api/users 201 150",
            "2026-11-13T10:32:00Z GET /api/products 404 80"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 3)
        self.assertEqual(result["errorRate"], 33.33)
        self.assertEqual(result["averageResponseTime"], 116.67)


if __name__ == "__main__":
    unittest.main()
