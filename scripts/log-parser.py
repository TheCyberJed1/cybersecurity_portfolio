#!/usr/bin/env python3
"""
log-parser.py
-------------
Parse Nmap XML output into a structured, readable report (table + CSV).
Pairs with nmap-automation.py.

Usage:
    python log-parser.py scans/nmap_192.168.1.0_24_20260101-120000.xml
    python log-parser.py scan.xml --csv report.csv
"""

import argparse
import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_nmap_xml(xml_path: Path) -> list[dict]:
    rows: list[dict] = []
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for host in root.findall("host"):
        status = host.find("status")
        if status is not None and status.get("state") != "up":
            continue

        addr_el = host.find("address")
        address = addr_el.get("addr") if addr_el is not None else "unknown"

        for port in host.findall("./ports/port"):
            state_el = port.find("state")
            if state_el is None or state_el.get("state") != "open":
                continue
            svc = port.find("service")
            rows.append({
                "host": address,
                "port": port.get("portid"),
                "protocol": port.get("protocol"),
                "service": svc.get("name") if svc is not None else "",
                "product": svc.get("product", "") if svc is not None else "",
                "version": svc.get("version", "") if svc is not None else "",
            })
    return rows


def print_table(rows: list[dict]) -> None:
    if not rows:
        print("[!] No open ports found.")
        return
    headers = ["host", "port", "protocol", "service", "product", "version"]
    widths = {h: max(len(h), *(len(str(r[h])) for r in rows)) for h in headers}
    line = "  ".join(h.ljust(widths[h]) for h in headers)
    print(line)
    print("-" * len(line))
    for r in rows:
        print("  ".join(str(r[h]).ljust(widths[h]) for h in headers))


def write_csv(rows: list[dict], csv_path: Path) -> None:
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"[+] CSV written to {csv_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse Nmap XML into a report.")
    parser.add_argument("xml", help="Path to Nmap -oX / -oA XML file")
    parser.add_argument("--csv", help="Optional path to write a CSV report")
    args = parser.parse_args()

    xml_path = Path(args.xml)
    if not xml_path.is_file():
        print(f"[!] File not found: {xml_path}", file=sys.stderr)
        return 1

    rows = parse_nmap_xml(xml_path)
    print_table(rows)

    if args.csv and rows:
        write_csv(rows, Path(args.csv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
