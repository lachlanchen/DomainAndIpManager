[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

Manage domain/IP lists for AI and GFW contexts, run DNS lookups, and export timestamped outputs. Includes CLI scripts and a GUI editor.

## 🚀 Overview

DomainAndIpManager is a Python toolkit for:
- Maintaining multiple list sets (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).
- Resolving domain `A` records and converting them to `IP/mask` entries.
- Combining domain-derived IPs with custom IP and CIDR sources.
- Exporting deterministic, timestamped output files for downstream networking/routing workflows.

It supports both:
- CLI workflows in `code/nslookup*.py` and sorting utilities.
- A Flask-based web GUI (`code/gui_app.py` + `gui/*`) for editing lists and running lookups interactively.

### At a Glance

| Area | What You Get |
|---|---|
| List sets | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Interfaces | CLI scripts + Flask GUI |
| Output style | Timestamped text snapshots + sorted TXT/JSON |
| Primary workflow | Edit lists → resolve domains → combine custom ranges → export |
| Optional helper | YouTube traffic OCR extraction under `traffics/` |

## 🎬 Demo

![Domain & IP Manager demo](demos/demo.png)

## ✨ Features

- Multi-list-set workflow: `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`.
- GUI list editor with save/load/run/copy workflow.
- Optional inclusion controls for domains, custom IPs, and CIDR blocks.
- Output mode switch: `Domains + IPs` or `IPs only`.
- Failed-lookup reporting in GUI.
- Timestamped output snapshots under `output/`.
- Utility tools to deduplicate and sort mixed domain/IP input into TXT/JSON.
- Optional traffic OCR helper under `traffics/` (YouTube-oriented extraction).

## 🗂️ Project Structure

```text
DomainAndIpManager/
├── README.md
├── requirements.txt
├── start_gui.sh
├── code/
│   ├── gui_app.py
│   ├── list_utils.py
│   ├── nslookup.py
│   ├── nslookup_simplified.py
│   ├── nslookup_simplified_gfw.py
│   ├── nslookup_simplified_gfw_w_ai.py
│   ├── nslookup_simplified_gfw_wo_ai.py
│   ├── unique_sort.py
│   └── unique_sort_print.py
├── gui/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── data/
│   ├── {ai,gfw,ai_gfw,gfw_wo_ai,non_gfw,default}_domains.txt
│   ├── {ai,gfw,ai_gfw,gfw_wo_ai,non_gfw,default}_custom_ips.txt
│   ├── {ai,gfw,ai_gfw,gfw_wo_ai,non_gfw,default}_cidr.txt
│   └── {ai,gfw,ai_gfw,gfw_wo_ai,non_gfw,default}_mask.txt
├── output/
├── demos/
├── figs/
├── traffics/
└── i18n/
```

## ✅ Prerequisites

- Python `3.10+` (recommended; code uses modern type syntax).
- `pip`.
- Network connectivity for DNS queries.
- Optional for OCR helper: `ffmpeg` and `tesseract` binaries available in `PATH`.

## 📦 Installation

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

Dependencies:

```bash
pip install -r requirements.txt
```

## 🖥️ Quick Start (GUI)

```bash
./start_gui.sh
```

Open `http://127.0.0.1:5000`.

Notes:
- `start_gui.sh` bootstraps `.venv`, installs dependencies when `requirements.txt` changes, and launches `code/gui_app.py`.
- You can also run directly with `python3 code/gui_app.py`.

## 🧭 Usage

### GUI Usage

1. Select a list set (`AI + GFW`, `AI`, `GFW`, `GFW (No AI)`, `Non-GFW (China)`, `Default`).
2. Edit `Domains`, `Custom IPs`, and `CIDR` text areas.
3. Set `Mask` and output mode (`Domains + IPs` or `IPs only`).
4. Click `Save` to persist changes to `data/*.txt`.
5. Click `Run` to resolve and generate output.
6. Click `Copy` to copy current output.

### CLI Usage

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

Each script prints results to the terminal and writes `output/<script>_YYYYMMDD_HHMMSS.txt`.

### Sorting & Normalization Tools

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` supports custom input/output flags and writes JSON.
- `unique_sort_print.py` prints sorted domains/IPs and writes both TXT and JSON into `output/`.
- If `domain_and_ips.txt` does not exist at repo root, use `-i <path>` with `unique_sort.py` or create the file.

### Optional Traffic Extraction Helper

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

This helper generates OCR-derived domain/IP markdown reports in `traffics/` and requires external tools (`ffmpeg`, `tesseract`).

## 🧾 Data Files

Lists are line-delimited and stored under `data/`:
- `ai_*` for AI-only lists
- `gfw_*` for GFW lists
- `ai_gfw_*` for combined lists
- `gfw_wo_ai_*` for GFW without AI
- `non_gfw_*` for China-accessible (non-GFW) lists
- `default_*` for the legacy/default list

Example:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### List Set Matrix

| List set | Domains file | Custom IPs file | CIDR file | Mask file |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ Configuration

- One entry per line in each list file.
- Lines beginning with `#` are treated as comments by shared list-loading logic and ignored during lookup runs.
- Masks are stored per list set in `data/<list>_mask.txt`.

Current repository state:
- All shipped mask files currently contain `30` (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).

Preserved note from earlier README versions (kept for compatibility context):
- `*_mask.txt` controls CIDR mask (default is `32`, `default` list uses `24`).
- Clarification: in current checked-in data and script defaults, active runtime defaults are `30` unless overridden.

## 📤 Outputs

- GUI + CLI: `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- Sorting tools: `output/domain_and_ips_unique_sorted.txt` and `.json`

## 🧪 Examples

Example CLI run:

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

Typical output shape:

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

Example custom JSON normalization:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ Development Notes

- Code style: Python 3, PEP 8, 4-space indentation, `snake_case` naming.
- Scripts are intentionally CLI-friendly and mostly single-purpose.
- Several `nslookup` variants currently share near-identical logic with different list-key mapping.
- No automated tests are currently present in this repository.

## 🧯 Troubleshooting

- `Input file not found: domain_and_ips.txt`:
  - Provide `-i <input-file>` to `code/unique_sort.py` or create `domain_and_ips.txt` in repo root.
- GUI not opening automatically:
  - Open `http://127.0.0.1:5000` manually after start.
- DNS results empty for some domains:
  - Verify network/DNS availability; unresolved domains are listed in GUI `Failed Lookups`.
- Missing dependencies:
  - Run `pip install -r requirements.txt`.
- OCR helper fails with missing command:
  - Install `ffmpeg` and `tesseract` and ensure both are on `PATH`.

## 🗺️ Roadmap

- Add automated tests for parsing, sorting, and lookup edge cases.
- Reduce duplicated logic across `nslookup` variants via shared parameterized runner.
- Expand multilingual docs under `i18n/`.
- Add optional CI checks for linting and smoke tests.

## 🤝 Contributing

Contributions are welcome.

Suggested workflow:
1. Create a branch for your change.
2. Keep commits focused and imperative (for example: `Limit domain list to ChatGPT, Claude, and Google AI`).
3. Include command output samples when changing generated data behavior.
4. Open a PR with a brief summary and any dependency/runtime notes.

## 📄 License

No explicit `LICENSE` file is currently present in the repository root. If you plan to redistribute or reuse this project, add or confirm license terms first.

## 💖 Support

Funding metadata is also available in `.github/FUNDING.yml`.

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- Project links: `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### Donation QR (if you want to support directly)

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 Notes

- One entry per line in data files.
- `*_mask.txt` controls CIDR mask (default is `32`, `default` list uses `24`).
- i18n status note: `i18n/` exists in this repository; localized README files are planned and should keep one language-options line at the top.
