"""Report generation for analyzed market data."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .analysis import MarketSummary


def render_markdown(summary: MarketSummary, source: str) -> str:
    percentage = (
        "not available"
        if summary.percentage_change is None
        else f"{summary.percentage_change:.2f}%"
    )
    return f"""# Market Data Report — {summary.ticker}

> Educational historical-data summary. This is not investment advice.

## Period

- First trading session: {summary.first_session}
- Last trading session: {summary.last_session}
- Valid observations: {summary.observations}
- Data source: {source}

## Closing-price statistics

| Metric | Value |
|---|---:|
| First close | {summary.first_close:.4f} |
| Last close | {summary.last_close:.4f} |
| Minimum close | {summary.minimum_close:.4f} |
| Maximum close | {summary.maximum_close:.4f} |
| Average close | {summary.average_close:.4f} |
| Median close | {summary.median_close:.4f} |
| Absolute change | {summary.absolute_change:.4f} |
| Percentage change | {percentage} |

Prices are shown in the instrument's source currency. Currency conversion is not performed.
"""


def write_reports(
    output_directory: Path,
    ticker: str,
    history: pd.DataFrame,
    summary: MarketSummary,
    source: str,
) -> list[Path]:
    output_directory.mkdir(parents=True, exist_ok=True)
    safe_ticker = ticker.replace(".", "_").replace("/", "_")

    csv_path = output_directory / f"{safe_ticker}_history.csv"
    json_path = output_directory / f"{safe_ticker}_summary.json"
    markdown_path = output_directory / f"{safe_ticker}_report.md"

    history.to_csv(csv_path, index_label="Date")
    json_path.write_text(
        json.dumps(summary.to_dict(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    markdown_path.write_text(render_markdown(summary, source), encoding="utf-8")
    return [csv_path, json_path, markdown_path]
