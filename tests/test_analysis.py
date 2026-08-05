import unittest

import pandas as pd

from market_data_automation.analysis import (
    MarketDataError,
    calculate_summary,
    normalize_ticker,
    validate_period,
)


class AnalysisTests(unittest.TestCase):
    def setUp(self):
        self.history = pd.DataFrame(
            {"Close": [10.0, 12.0, 11.0]},
            index=pd.to_datetime(["2026-01-05", "2026-01-06", "2026-01-07"]),
        )

    def test_b3_ticker_receives_sa_suffix(self):
        self.assertEqual(normalize_ticker("petr4", "b3"), "PETR4.SA")

    def test_global_ticker_is_not_modified(self):
        self.assertEqual(normalize_ticker("aapl", "global"), "AAPL")

    def test_invalid_period_is_rejected(self):
        with self.assertRaises(MarketDataError):
            validate_period("2026-01-10", "2026-01-10")

    def test_summary_calculates_expected_values(self):
        summary = calculate_summary("TEST", self.history)

        self.assertEqual(summary.observations, 3)
        self.assertEqual(summary.minimum_close, 10.0)
        self.assertEqual(summary.maximum_close, 12.0)
        self.assertEqual(summary.average_close, 11.0)
        self.assertEqual(summary.percentage_change, 10.0)


if __name__ == "__main__":
    unittest.main()
