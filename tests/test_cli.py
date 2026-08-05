import tempfile
import unittest
from pathlib import Path

from market_data_automation.cli import main


class CliTests(unittest.TestCase):
    def test_offline_sample_generates_three_reports(self):
        sample = Path("examples/sample_prices.csv")
        with tempfile.TemporaryDirectory() as directory:
            exit_code = main(
                [
                    "--ticker",
                    "SAMPLE",
                    "--market",
                    "global",
                    "--input-csv",
                    str(sample),
                    "--output-dir",
                    directory,
                ]
            )

            generated = list(Path(directory).iterdir())

        self.assertEqual(exit_code, 0)
        self.assertEqual(len(generated), 3)


if __name__ == "__main__":
    unittest.main()
