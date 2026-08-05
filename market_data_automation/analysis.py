"""Validation and statistical analysis for historical market prices."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from typing import Any

import pandas as pd


class MarketDataError(ValueError):
    """Raised when market data cannot be validated or analyzed."""


@dataclass(frozen=True)
class MarketSummary:
    ticker: str
    first_session: str
    last_session: str
    observations: int
    minimum_close: float
    maximum_close: float
    average_close: float
    median_close: float
    first_close: float
    last_close: float
    absolute_change: float
    percentage_change: float | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def normalize_ticker(ticker: str, market: str) -> str:
    """Normalize a symbol and optionally add the B3 Yahoo Finance suffix."""
    normalized = ticker.strip().upper()
    if not normalized:
        raise MarketDataError("Ticker cannot be empty.")
    if any(character.isspace() for character in normalized):
        raise MarketDataError("Ticker cannot contain spaces.")
    if market == "b3" and not normalized.endswith(".SA"):
        normalized += ".SA"
    return normalized


def parse_date(value: str, label: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise MarketDataError(f"{label} must use YYYY-MM-DD format.") from exc


def validate_period(start: str, end: str) -> tuple[date, date]:
    start_date = parse_date(start, "Start date")
    end_date = parse_date(end, "End date")
    if end_date <= start_date:
        raise MarketDataError("End date must be later than start date.")
    return start_date, end_date


def prepare_history(data: pd.DataFrame) -> pd.DataFrame:
    """Return sorted OHLCV rows containing a valid closing price."""
    if data.empty:
        raise MarketDataError("No market data was returned for the requested period.")
    if "Close" not in data.columns:
        raise MarketDataError("Market data does not contain a Close column.")

    prepared = data.copy()
    prepared.index = pd.to_datetime(prepared.index, errors="coerce")
    prepared = prepared[~prepared.index.isna()].sort_index()
    prepared["Close"] = pd.to_numeric(prepared["Close"], errors="coerce")
    prepared = prepared.dropna(subset=["Close"])
    if prepared.empty:
        raise MarketDataError("No valid closing prices were found.")
    return prepared


def calculate_summary(ticker: str, data: pd.DataFrame) -> MarketSummary:
    prepared = prepare_history(data)
    close = prepared["Close"]
    first_close = float(close.iloc[0])
    last_close = float(close.iloc[-1])
    absolute_change = last_close - first_close
    percentage_change = (
        None if first_close == 0 else (absolute_change / first_close) * 100
    )

    return MarketSummary(
        ticker=ticker,
        first_session=prepared.index[0].date().isoformat(),
        last_session=prepared.index[-1].date().isoformat(),
        observations=int(close.count()),
        minimum_close=round(float(close.min()), 4),
        maximum_close=round(float(close.max()), 4),
        average_close=round(float(close.mean()), 4),
        median_close=round(float(close.median()), 4),
        first_close=round(first_close, 4),
        last_close=round(last_close, 4),
        absolute_change=round(absolute_change, 4),
        percentage_change=(
            None if percentage_change is None else round(percentage_change, 4)
        ),
    )
