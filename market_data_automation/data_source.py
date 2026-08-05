"""Online and offline market-data sources."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .analysis import MarketDataError


def fetch_yahoo_history(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Fetch unadjusted daily history from Yahoo Finance through yfinance."""
    try:
        import yfinance as yf

        return yf.Ticker(ticker).history(
            start=start,
            end=end,
            interval="1d",
            auto_adjust=False,
            actions=False,
            timeout=15,
            raise_errors=True,
        )
    except Exception as exc:
        raise MarketDataError(f"Yahoo Finance request failed: {exc}") from exc


def load_csv_history(path: Path) -> pd.DataFrame:
    """Load offline historical data containing Date and Close columns."""
    if not path.is_file():
        raise MarketDataError(f"CSV file was not found: {path}")
    try:
        data = pd.read_csv(path)
    except Exception as exc:
        raise MarketDataError(f"Could not read CSV file: {exc}") from exc
    if "Date" not in data.columns:
        raise MarketDataError("CSV file must contain a Date column.")
    return data.set_index("Date")
