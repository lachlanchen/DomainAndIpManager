#!/usr/bin/env python3
import re
import json
from pathlib import Path
from typing import List, Tuple

DOMAIN_RE = re.compile(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
IP_CIDR_RE = re.compile(r"^\s*(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))\s*$")


def parse_file(path: Path) -> Tuple[List[str], List[str]]:
    domains_set = set()
    ips_set = set()

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue

        m = IP_CIDR_RE.match(line)
        if m:
            ip = m.group(1)
            mask = m.group(2) if m.group(2) is not None else "32"
            ips_set.add(f"{ip}/{mask}")
            continue

        if DOMAIN_RE.match(line):
            domains_set.add(line.lower())
            continue

    domains = sorted(domains_set)
    ips = sorted(ips_set, key=lambda s: tuple(int(x) for x in s.split("/")[0].split(".")) + (int(s.split("/")[1]),))

    return domains, ips


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", default="domain_and_ips.txt", help="Input filename")
    ap.add_argument(
        "-o",
        "--output",
        default="output/domain_and_ips_unique_sorted.json",
        help="Output JSON filename",
    )
    args = ap.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        raise SystemExit(f"Input file not found: {in_path}")

    domains, ips = parse_file(in_path)

    out_obj = {"domains": domains, "ips": ips}

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out_obj, indent=2), encoding="utf-8")
    print(f"Done. domains={len(domains)} ips={len(ips)} -> {args.output}")


if __name__ == "__main__":
    main()
