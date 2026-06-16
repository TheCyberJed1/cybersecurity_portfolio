#!/usr/bin/env python3
"""
nmap-automation.py
------------------
Run consistent Nmap scans across a target range and save raw + XML output for
downstream parsing (see log-parser.py).

USE ONLY against systems you own or are explicitly authorized to test.

Usage:
    python nmap-automation.py 192.168.1.0/24
    python nmap-automation.py 10.0.0.5 --ports 1-1000 --out scans/
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def build_command(target: str, ports: str, out_dir: Path) -> tuple[list[str], Path]:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe = target.replace("/", "_").replace(":", "_")
    out_base = out_dir / f"nmap_{safe}_{stamp}"
    cmd = [
        "nmap",
        "-sV",            # service/version detection
        "-sS",            # SYN scan (requires privileges)
        "-T4",            # faster timing
        "-p", ports,
        "-oA", str(out_base),  # writes .nmap, .gnmap, .xml
        target,
    ]
    return cmd, out_base


def main() -> int:
    parser = argparse.ArgumentParser(description="Automated Nmap scan runner.")
    parser.add_argument("target", help="IP, hostname, or CIDR range")
    parser.add_argument("--ports", default="1-1024", help="Port range (default 1-1024)")
    parser.add_argument("--out", default="scans", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd, out_base = build_command(args.target, args.ports, out_dir)
    print(f"[*] Running: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("[!] nmap not found. Install nmap and ensure it's on PATH.", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"[!] nmap exited with status {exc.returncode}", file=sys.stderr)
        return exc.returncode

    print(f"[+] Done. Output written to {out_base}.(nmap|gnmap|xml)")
    print(f"[*] Next: python log-parser.py {out_base}.xml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
