# Recovery and Modernization Notes

## Origin

The original Market Data Automation project was created as a college exercise without AI assistance. Its goal was to:

1. ask for a stock symbol and date range;
2. retrieve historical prices;
3. calculate maximum, minimum, and average closing prices;
4. prepare an email containing the result.

After the original repository was lost, a single recovered file remained. It is preserved unchanged in `legacy/Stockbot_original.py` so the project's authorship and technical evolution remain visible.

## Why the Recovered Script Was Unreliable

The historical-data calculation contained the core of a useful idea, but delivery depended on desktop automation:

- Gmail was opened in a browser;
- execution waited a fixed number of seconds;
- buttons were clicked at hard-coded coordinates;
- text was pasted through simulated keyboard input;
- success was reported without confirming delivery.

Any change in screen resolution, window position, browser zoom, Gmail layout, interface language, connection speed, or authentication state could break the process.

The script also combined input, data retrieval, analysis, formatting, browser control, and error handling in one execution block, making isolated testing difficult.

## Modernization Strategy

The rebuilt version preserves the original purpose while replacing fragile UI automation with deterministic file reports.

| Area | Recovered version | Modernized version |
|---|---|---|
| Input | interactive prompts | explicit CLI arguments |
| B3 ticker | automatic `.SA` | configurable B3/global market mode |
| Data | Yahoo Finance only | Yahoo Finance or offline CSV |
| Analysis | max/min/mean | observations, max, min, mean, median, and change |
| Output | Gmail UI automation | CSV, JSON, and Markdown files |
| Testing | none | offline automated tests |
| Errors | one broad exception | validation and categorized exit codes |
| Reproducibility | dependent on desktop state | deterministic offline sample |

## Authorship Statement

The recovered script documents Arthur Alves Stefanini's original academic work. The current repository presents both that historical artifact and a later engineering revision, without claiming that the original version was production-ready.
