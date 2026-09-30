import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "apps" / "sample-api"))
from sample_api import health_response


class HealthTests(unittest.TestCase):
    def test_health_response(self):
        self.assertEqual(health_response()["status"], "ok")
        self.assertEqual(health_response()["application"], "sample-api")


if __name__ == "__main__":
    unittest.main()
