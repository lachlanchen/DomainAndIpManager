from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Tuple


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def read_list_file(path: Path) -> List[str]:
    if not path.exists():
        return []
    items: List[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        items.append(line)
    return items


def unique_preserve(seq: Iterable[str]) -> List[str]:
    seen = set()
    out = []
    for item in seq:
        if item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def load_lists(stem: str) -> Tuple[List[str], List[str], List[str]]:
    base = repo_root() / "data"
    domains = read_list_file(base / f"{stem}_domains.txt")
    custom_ips = read_list_file(base / f"{stem}_custom_ips.txt")
    cidr = read_list_file(base / f"{stem}_cidr.txt")
    return domains, custom_ips, cidr


def write_output(lines: Iterable[str], prefix: str) -> Path:
    out_dir = repo_root() / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = out_dir / f"{prefix}_{stamp}.txt"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path
