# Repository Guidelines

## Project Structure & Module Organization
- Root scripts are small Python utilities:
  - `nslookup*.py` resolve domain IPs and print CIDR blocks.
  - `unique_sort.py` and `unique_sort_print.py` de-duplicate and sort domain/IP lists.
- Input/output data lives at the repo root, e.g. `domain_and_ips.txt`, `domain_and_ips_unique_sorted.txt`, and `domain_and_ips_unique_sorted.json`.
- No sub-packages or tests directories are currently present.

## Build, Test, and Development Commands
- `python3 nslookup_simplified.py` — resolve the scoped domain list to IPs and print domains + CIDR entries.
- `python3 nslookup_simplified_gfw.py` — resolve a broader list (Google/YouTube/Meta, etc.) for GFW use.
- `python3 unique_sort.py -i domain_and_ips.txt -o domain_and_ips_unique_sorted.json` — normalize and sort inputs into JSON.
- `python3 unique_sort_print.py` — print and write sorted TXT/JSON outputs.

Dependency: these scripts import `dns.resolver` from `dnspython`. Install if needed with `pip install dnspython`.

## Coding Style & Naming Conventions
- Python 3, PEP 8 style, 4-space indentation.
- Use `snake_case` for functions/variables and ALL_CAPS for constants (e.g., regexes).
- Keep scripts single-purpose and CLI-friendly; avoid adding hidden side effects.

## Testing Guidelines
- No automated tests are set up yet.
- If adding tests, place them under a new `tests/` directory and name files `test_*.py`.
- Prefer small unit tests for parsing and sorting logic.

## Commit & Pull Request Guidelines
- Commit messages are short, imperative summaries (e.g., “Limit domain list to ChatGPT, Claude, and Google AI”).
- PRs should include: a brief description, command output samples (if data files change), and any new dependencies.

## Configuration & Data Notes
- `domain_and_ips.txt` is the primary input list; keep entries one per line.
- Output JSON is a two-key object: `domains` and `ips` with sorted arrays.
- Avoid private IP ranges (e.g., `10.x.x.x`) unless explicitly required.
