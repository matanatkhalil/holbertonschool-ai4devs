import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer


class TestEndpointTie(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_endpoint_tie(self):
        logs = [
            "2026-11-13T10:30:00Z GET /api/users 200 100",
            "2026-11-13T10:31:00Z GET /api/products 200 100"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(
            result["mostRequestedEndpoint"], "/api/products"
        )


if __name__ == "__main__":
    unittest.main()