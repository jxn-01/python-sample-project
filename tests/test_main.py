import tempfile
import unittest
from pathlib import Path

from main import format_summary, load_numbers_from_csv, summarize_numbers


class TestDataProcessing(unittest.TestCase):
    def test_load_numbers_from_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "values.csv"
            path.write_text("1\n2\n3\n", encoding="utf-8")
            self.assertEqual(load_numbers_from_csv(str(path)), [1.0, 2.0, 3.0])

    def test_load_numbers_from_csv_invalid_value(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad.csv"
            path.write_text("a\n2\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_numbers_from_csv(str(path))

    def test_summarize_numbers(self):
        summary = summarize_numbers([1.0, 2.0, 3.0])
        self.assertEqual(summary["count"], 3)
        self.assertEqual(summary["sum"], 6.0)
        self.assertEqual(summary["min"], 1.0)
        self.assertEqual(summary["max"], 3.0)
        self.assertAlmostEqual(summary["average"], 2.0)

    def test_format_summary(self):
        summary = {"count": 3, "sum": 6.0, "min": 1.0, "max": 3.0, "average": 2.0}
        formatted = format_summary(summary)
        self.assertIn("Count:", formatted)
        self.assertIn("Average: 2.00", formatted)


if __name__ == "__main__":
    unittest.main()
