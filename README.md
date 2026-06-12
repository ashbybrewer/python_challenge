# PyBank & PyPoll — Python Fundamentals, Real Ledgers

Two small command-line analyzers built with the Python standard library only (`csv`, `os`) — no pandas allowed. The point was to do the bookkeeping by hand: accumulators, dictionaries, edge-aware loops.

## PyBank — `PyBank/main.py`
Reads 86 months of company P&L (`budget_data.csv`) and reports:

- Total months: **86** · Net total: **$22,564,198**
- Average month-over-month change: **−$8,311.11**
- Greatest increase: **Aug-2016 (+$1,862,002)** · Greatest decrease: **Feb-2014 (−$1,825,558)**

## PyPoll — `PyPoll/main.py`
Tallies a 369,711-ballot election (`election_data.csv`) into per-candidate counts and percentages:

- **Diana DeGette — 73.81% (272,892) — winner**, Charles Casper Stockham 23.05%, Raymon Anthony Doane 3.14%

Both scripts print to terminal and write their results to `analysis/*.txt`.

## Run it
```bash
cd PyBank  && python main.py
cd PyPoll  && python main.py
```

---
*Built during the University of Texas Data Analysis Boot Camp (2023–24), with help from classmates, tutors, and AI tools — disclosed then, kept honest now.*
