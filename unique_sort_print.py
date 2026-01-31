#!/usr/bin/env python3
import re
from pathlib import Path
from typing import List, Tuple
import json

DOMAIN_RE = re.compile(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
IP_CIDR_RE = re.compile(r"^\s*(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))\s*$")


def parse_file(path: Path) -> Tuple[List[str], List[str]]:
    domains = set()
    ips = set()

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue

        ip_match = IP_CIDR_RE.match(line)
        if ip_match:
            ip = ip_match.group(1)
            mask = ip_match.group(2) or "32"
            ips.add(f"{ip}/{mask}")
            continue

        if DOMAIN_RE.match(line):
            domains.add(line.lower())

    domains_sorted = sorted(domains)
    ips_sorted = sorted(
        ips,
        key=lambda s: tuple(map(int, s.split("/")[0].split("."))) + (int(s.split("/")[1]),)
    )

    return domains_sorted, ips_sorted


def main() -> None:
    input_file = Path("domain_and_ips.txt")
    output_txt = Path("domain_and_ips_unique_sorted.txt")
    output_json = Path("domain_and_ips_unique_sorted.json")

    if not input_file.exists():
        raise SystemExit(f"Input file not found: {input_file}")

    domains, ips = parse_file(input_file)

    # ---- print to terminal ----
    print("===== DOMAINS =====")
    for d in domains:
        print(d)

    print("\n===== IPS =====")
    for ip in ips:
        print(ip)

    # ---- write TXT (one per row) ----
    with output_txt.open("w", encoding="utf-8") as f:
        for d in domains:
            f.write(d + "\n")
        for ip in ips:
            f.write(ip + "\n")

    # ---- optional JSON output ----
    with output_json.open("w", encoding="utf-8") as f:
        json.dump(
            {"domains": domains, "ips": ips},
            f,
            indent=2
        )

    print(
        f"\nDone ✔\n"
        f"Domains: {len(domains)}\n"
        f"IPs: {len(ips)}\n"
        f"TXT: {output_txt}\n"
        f"JSON: {output_json}"
    )


if __name__ == "__main__":
    main()

