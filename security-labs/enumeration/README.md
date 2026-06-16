# Automated Network Reconnaissance Workflow Using Nmap and Python Parsing

> ⚠️ **Authorized targets only.** Run against systems you own or are explicitly
> permitted to test.

## Objective
Turn manual reconnaissance into a repeatable pipeline: automate Nmap scans, parse
the output with Python, and produce a structured report.

## Workflow
1. **Scan automation** — driven by [`../../scripts/nmap-automation.py`](../../scripts/nmap-automation.py).
2. **Output parsing** — [`../../scripts/log-parser.py`](../../scripts/log-parser.py) turns raw output into structured data.
3. **Reporting** — normalized host/port/service table for triage.

## Tools Used
- Nmap
- Python 3
- Helpers in [`../../scripts/recon-tools/`](../../scripts/recon-tools/)

## Reporting Structure
| Host | Port | Service | Version | Notes |
|------|------|---------|---------|-------|
|      |      |         |         |       |

## Real-World Application
Repeatable recon pipelines are the backbone of professional assessments — they
keep coverage consistent and findings auditable.

## Evidence
<!-- Sample scan output, parsed report -->
