# Market Data Automation

A Python command-line project that retrieves or loads historical price data, calculates reproducible closing-price statistics, and exports CSV, JSON, and Markdown reports.

> **Educational project:** outputs are historical-data summaries, not investment advice, price forecasts, or trading recommendations.

## Project History

This project began as a college automation exercise created without AI assistance. The original repository was later lost, and only one recovered script remained. That script is preserved unchanged in [`legacy/Stockbot_original.py`](legacy/Stockbot_original.py).

The current version rebuilds the original idea with testable modules, offline execution, explicit validation, and local report generation. See [Recovery and Modernization Notes](docs/project-history.md) for the technical comparison.

## 日本語概要

Market Data Automation は、過去の市場価格データを取得またはCSVから読み込み、終値の統計を計算し、CSV・JSON・Markdown形式のレポートを生成するPython CLIプロジェクトです。

本プロジェクトは学習・ポートフォリオ目的です。投資助言、価格予測、売買推奨を提供するものではありません。

## Features

- B3 symbols with automatic `.SA` suffix support;
- global Yahoo Finance symbols such as `AAPL` or `7203.T`;
- inclusive start and exclusive end-date validation;
- online historical data through `yfinance.Ticker.history()`;
- offline CSV mode for repeatable demonstrations;
- minimum, maximum, average, median, and period change calculations;
- raw-history CSV export;
- machine-readable JSON summary;
- human-readable Markdown report;
- automated tests that do not require network access.

## Requirements

- Python 3.10+
- internet access only for Yahoo Finance mode.

## Installation

```bash
git clone https://github.com/artloock/MarketDataAutomation.git
cd MarketDataAutomation
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Offline Demonstration

The included sample allows the complete workflow to run without internet access:

```bash
python -m market_data_automation.cli \
  --ticker SAMPLE \
  --market global \
  --input-csv examples/sample_prices.csv \
  --output-dir output/sample
```

PowerShell version:

```powershell
python -m market_data_automation.cli `
  --ticker SAMPLE `
  --market global `
  --input-csv examples/sample_prices.csv `
  --output-dir output/sample
```

## Yahoo Finance Examples

B3 symbol:

```bash
python -m market_data_automation.cli \
  --ticker PETR4 \
  --market b3 \
  --start 2025-01-01 \
  --end 2026-01-01 \
  --output-dir output/petr4
```

Global symbol:

```bash
python -m market_data_automation.cli \
  --ticker AAPL \
  --market global \
  --start 2025-01-01 \
  --end 2026-01-01 \
  --output-dir output/aapl
```

The end date follows the `yfinance` historical-data convention and is exclusive.

## Generated Files

Each execution creates:

```text
TICKER_history.csv
TICKER_summary.json
TICKER_report.md
```

Prices remain in the instrument's source currency. The project does not perform currency conversion.

## Input CSV Format

Offline data must contain at least `Date` and `Close`:

```csv
Date,Close
2026-01-05,30.50
2026-01-06,31.75
```

Additional OHLCV columns are preserved in the exported history.

## Tests

```bash
python -m unittest discover -s tests -v
```

Tests use local sample data and generated DataFrames. They do not contact Yahoo Finance.

## Reliability Improvements

The recovered version controlled Gmail through fixed screen coordinates. That approach depended on resolution, browser layout, language, login state, and timing.

The modernized version:

- separates collection, analysis, and reporting;
- produces files instead of clicking a browser;
- validates inputs before fetching data;
- supports a deterministic offline mode;
- returns process exit codes;
- preserves the recovered script for historical comparison.

## Limitations

- Yahoo Finance availability and returned data are outside this project's control;
- only historical daily data is analyzed;
- corporate actions, taxes, inflation, fees, dividends, and currency conversion are not modeled;
- statistics describe the selected period and do not predict future performance;
- reports should be independently verified before any consequential use.

## Data Source

Online mode uses the public `Ticker.history()` interface from `yfinance`. The library provides access to Yahoo Finance market data but is not affiliated with or endorsed by Yahoo.

## License and Attribution

Released under the [MIT License](LICENSE). Copies or substantial portions must retain the original copyright and license notice.

## Author

**Arthur Alves Stefanini**
[GitHub](https://github.com/artloock) · [LinkedIn](https://www.linkedin.com/in/arthur-alves-stefanini-973a99169/)
