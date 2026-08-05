"""Command-line entry point for market-data reporting."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .analysis import (
    MarketDataError,
    calculate_summary,
    normalize_ticker,
    prepare_history,
    validate_period,
)
from .data_source import fetch_yahoo_history, load_csv_history
from .reporting import write_reports


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download or load historical prices and generate local reports."
    )
    parser.add_argument("--ticker", required=True, help="Symbol such as PETR4 or AAPL.")
    parser.add_argument(
        "--market",
        choices=("b3", "global"),
        default="b3",
        help="B3 automatically adds the .SA Yahoo Finance suffix.",
    )
    parser.add_argument("--start", help="Inclusive start date in YYYY-MM-DD format.")
    parser.add_argument("--end", help="Exclusive end date in YYYY-MM-DD format.")
    parser.add_argument(
        "--input-csv",
        type=Path,
        help="Use an offline CSV with Date and Close columns instead of Yahoo Finance.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
        help="Directory for CSV, JSON, and Markdown reports.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    try:
        args = create_parser().parse_args(argv)
        ticker = normalize_ticker(args.ticker, args.market)

        if args.input_csv:
            history = load_csv_history(args.input_csv)
            source = f"offline CSV: {args.input_csv}"
        else:
            if not args.start or not args.end:
                raise MarketDataError(
                    "--start and --end are required when --input-csv is not used."
                )
            validate_period(args.start, args.end)
            history = fetch_yahoo_history(ticker, args.start, args.end)
            source = "Yahoo Finance via yfinance"

        prepared = prepare_history(history)
        summary = calculate_summary(ticker, prepared)
        paths = write_reports(args.output_dir, ticker, prepared, summary, source)

        print(f"Report generated for {ticker} ({summary.observations} observations).")
        for path in paths:
            print(f"- {path}")
        return 0
    except MarketDataError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"File error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
