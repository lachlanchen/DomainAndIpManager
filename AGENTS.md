# Repository Guidelines

## Project Structure & Module Organization
- `code/` holds Python utilities:
  - `nslookup*.py` resolve domain IPs and print CIDR blocks.
  - `unique_sort.py` and `unique_sort_print.py` de-duplicate and sort domain/IP lists.
- `data/` contains line-delimited input lists (domains, custom IPs, CIDR blocks) keyed by list set:
  - `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, and `default`.
  - Example: `data/ai_domains.txt`, `data/ai_custom_ips.txt`, `data/ai_cidr.txt`, `data/ai_mask.txt`.
- `output/` contains generated artifacts (sorted lists, lookup outputs).
- Repo root keeps inputs like `domain_and_ips.txt` and project docs.
- No sub-packages or tests directories are currently present.

## Build, Test, and Development Commands
- `python3 code/nslookup_simplified.py` — resolve the scoped domain list to IPs and print domains + CIDR entries.
- `python3 code/nslookup_simplified_gfw.py` — resolve a broader list (Google/YouTube/Meta, etc.) for GFW use.
- `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` — normalize and sort inputs into JSON.
- `python3 code/unique_sort_print.py` — print and write sorted TXT/JSON outputs into `output/`.
  - DNS outputs are also saved to `output/<script>_YYYYMMDD_HHMMSS.txt`.
- `python3 code/gui_app.py` — launch the GUI at `http://127.0.0.1:5000` (default list: AI + GFW).

Dependencies: `dnspython` for DNS resolution and `flask` for the GUI (`pip install -r requirements.txt`).

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
- Commit after each change; keep commits focused and self-contained.
- PRs should include: a brief description, command output samples (if data files change), and any new dependencies.

## Configuration & Data Notes
- `domain_and_ips.txt` is the primary input list; keep entries one per line.
- Output JSON is a two-key object: `domains` and `ips` with sorted arrays.
- Avoid private IP ranges (e.g., `10.x.x.x`) unless explicitly required.
- Masks are stored per list set in `data/<list>_mask.txt` (defaults: `32`, `default` uses `24`).
