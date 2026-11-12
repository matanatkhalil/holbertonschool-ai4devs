import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):

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

    def test_empty_input(self):
        result = self.analyzer.analyze([])

        self.assertEqual(result["totalRequests"], 0)
        self.assertEqual(result["errorRate"], 0)
        self.assertEqual(result["mostRequestedEndpoint"], None)

    def test_malformed_entry(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 100",
            "INVALID LOG ENTRY"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 1)
        self.assertEqual(result["malformedEntries"], 1)

    def test_invalid_status_code(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 700 100"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 0)
        self.assertEqual(result["malformedEntries"], 1)

    def test_negative_response_time(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 -50"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 0)
        self.assertEqual(result["malformedEntries"], 1)

    def test_all_requests_are_errors(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 404 100",
            "2026-11-13T10:31:00Z POST /api/users 500 200",
            "2026-11-13T10:32:00Z GET /api/products 503 300"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["errorRate"], 100)

    def test_single_request(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 250"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 1)
        self.assertEqual(result["averageResponseTime"], 250)

    def test_endpoint_tie(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 100",
            "2026-11-13T10:31:00Z GET /api/products 200 100"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(
            result["mostRequestedEndpoint"], "/api/products"
        )

    def test_zero_response_time(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 0"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["totalRequests"], 1)
        self.assertEqual(result["averageResponseTime"], 0)
        self.assertEqual(result["malformedEntries"], 0)

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
