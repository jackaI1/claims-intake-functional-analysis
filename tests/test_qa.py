import unittest

from claims_intake.qa import aggregate
from tests.test_intake import requirement


class ReportTests(unittest.TestCase):
    @requirement("R14")
    def test_missing_failed_and_skipped_coverage_cannot_pass(self):
        for status in ("FAIL", "SKIP"):
            rows = aggregate(["R1", "R2"], [{"test": "case", "status": status, "requirements": ["R1"]}])
            self.assertEqual([r["status"] for r in rows], ["FAIL", "FAIL"])
        rows = aggregate(["R1"], [{"test": "a", "status": "PASS", "requirements": ["R1"]},
                                  {"test": "b", "status": "FAIL", "requirements": ["R1"]}])
        self.assertEqual(rows[0]["status"], "FAIL")

    @requirement("R14")
    def test_all_linked_tests_must_pass(self):
        rows = aggregate(["R1", "R2"], [{"test": "case", "status": "PASS", "requirements": ["R1", "R2"]}])
        self.assertEqual([r["status"] for r in rows], ["PASS", "PASS"])
