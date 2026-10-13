[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Mode](https://img.shields.io/badge/Mode-CLI%20%2F%20GUI-1f6feb)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Locale](https://img.shields.io/badge/Docs-English%20%7C%209%20More-0ea5e9?logo=googletranslate&logoColor=white)
![License](https://img.shields.io/badge/License-Not%20Included-9ca3af)

這是個 Python 工具集，用來維護精選的 domain/IP/CIDR 清單集合，透過 DNS 解析產生可重複的 IP 區段、去重、並匯出可重現的快照，供路由與過濾流程使用。

| Focus | Details |
|---|---|
| 清單集合 | `ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default` |
| 核心流程 | DNS 解析、確定性合併、標準化、匯出 |
| 輸出成果 | `output/` 中的時間戳 TXT 與 JSON 快照 |
| 介面方式 | CLI 指令腳本 + Flask GUI（`code/gui_app.py`，本地啟動） |
| 資料格式 | `data/` 目錄中的逐行 domain/IP/CIDR 純文字檔 |

---

## 🧭 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Scripts & Workflow Map](#-scripts--workflow-map)
- [Examples](#-examples)
- [Development Notes](#-development-notes)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Support](#️-support)
- [Contact](#-contact)
- [License](#-license)

## 🗂️ At a Glance

| Area | Details |
|---|---|
| 清單集合 | `ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default` |
| 核心流程 | DNS 解析 + 合併、去重/排序、GUI 編輯、快照匯出 |
| 輸出格式 | TXT + JSON |
| 主要輸出目錄 | `output/` |
| 主要進入點 | `code/` 下的 CLI 腳本，以及 `gui_app.py` 的 Flask GUI |

## 🚀 Overview

DomainAndIpManager 旨在建立可重複執行的清單產生流程：

- 在 `data/` 中維護各自獨立的清單組（domains + custom IPs + CIDR + mask 檔）
- 解析網域名稱並轉換為 CIDR 格式條目
- 將解析結果與自訂/精選的網路區段合併
- 輸出穩定排序的可重現結果（TXT + JSON），並可選擇產生時間戳快照
- 可透過 CLI 運行，或啟動 Web GUI 進行互動式編輯與重建

## ✨ Features

| Area | Details |
|---|---|
| 多清單設定 | 針對不同路由策略提供分離的清單集合（`ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default`） |
| DNS 解析 | `code/nslookup*.py` 腳本可將 domain 展開為 IP 區段 |
| 排序與去重 | `code/unique_sort*.py` 會處理 domain/IP/CIDR 混合輸入並做標準化 |
| 確定性匯出 | TXT + JSON 輸出順序穩定，並支援時間戳快照 |
| GUI 編輯 | `gui/` 支援 `domains`、`custom_ips`、`cidr` 與 mask 設定的互動編輯 |
| 診斷 | 選用失敗解析報告，協助除錯 DNS 解析問題 |
| OCR 工具（選用） | `traffics/` 內提供 YouTube/影片擷取輔助 |

---

## ✅ Prerequisites

| Requirement | Notes |
|---|---|
| Python | 3.10+（建議） |
| 網路 | DNS 查詢需要可存取網際網路 |
| Python 套件 | `pip` 與 `requirements.txt` 內的相依套件 |
| Git | 需要用來 clone/更新這個資料庫 |
| OCR optional stack | 若使用流量擷取工具，需同時安裝 `ffmpeg` 與 `tesseract` |

---

## 📦 Installation

```bash
python3 -m pip install -r requirements.txt
```

快速安裝：

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> 假設：直接使用 CLI 並不需要額外的虛擬環境啟動流程；若使用偏好，`start_gui.sh` 仍會自動建立並使用 `.venv`。

## 🧭 Usage

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` 會啟動 `code/gui_app.py`，並提供：

- URL：`http://127.0.0.1:5000`
- 清單檔案的 GUI 編輯介面
- 按需產生與可複製的輸出預覽
- 需要時會自動建立 `.venv` 並安裝/更新套件

你也可以直接啟動：

```bash
python3 code/gui_app.py
```

### CLI Reference

| Common task | Command |
|---|---|
| 解析 AI 相關清單 | `python3 code/nslookup_simplified.py` |
| 解析 GFW 相關清單 | `python3 code/nslookup_simplified_gfw.py` |
| 解析 GFW + AI 合併清單 | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| 解析 GFW 排除 AI 清單 | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| 執行基礎解析流程 | `python3 code/nslookup.py` |
| 將清單排序並去重輸出 JSON | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| 輸出標準 TXT/JSON | `python3 code/unique_sort_print.py` |

注意事項：

- 輸出檔會以時間戳格式寫入，例如 `output/<script>_YYYYMMDD_HHMMSS.txt`。
- 排序腳本可透過參數指定自訂輸入/輸出路徑。

### Optional OCR Utility

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

需要在 `PATH` 中可找到 `ffmpeg` 與 `tesseract`。

## ⚙️ Configuration

- 所有 `data/` 文字檔皆為每行一筆條目。
- 目前共用清單載入邏輯會略過以 `#` 開頭的註解行。
- 各清單的遮罩值存放於 `data/<set>_mask.txt`。
- 目前儲存於版本庫的遮罩值為各清單檔所定義的實際值。
- 寫入前會先將輸入轉為穩定去重的排序輸出。

### List Set Matrix

| List set | Domains file | Custom IPs file | CIDR file | Mask file |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## 🧰 Script & Workflow Map

| Script | Purpose |
|---|---|
| `code/nslookup.py` | 基礎 domain/IP 解析執行器 |
| `code/nslookup_simplified.py` | AI 專用解析 + CIDR 匯出 |
| `code/nslookup_simplified_gfw.py` | GFW 專用解析 |
| `code/nslookup_simplified_gfw_w_ai.py` | 合併 GFW + AI 解析 |
| `code/nslookup_simplified_gfw_wo_ai.py` | 排除 AI 的 GFW 解析 |
| `code/unique_sort.py` | 標準化 + 去重 + JSON 輸出 |
| `code/unique_sort_print.py` | 列印並寫入標準 TXT/JSON 輸出 |
| `code/list_utils.py` | 共用 loader、mask 與清單處理工具 |
| `code/gui_app.py` | Flask GUI 後端 |
| `traffics/extract_youtube_traffic.py` | 流量擷取用選用 OCR 輔助 |
| `start_gui.sh` | 虛擬環境初始化 + 套件安裝 + 啟動伺服器 |

## 🗂️ Project Structure

```text
DomainAndIpManager/
├── AGENTS.md
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
│   ├── *_domains.txt
│   ├── *_custom_ips.txt
│   ├── *_cidr.txt
│   └── *_mask.txt
├── output/
├── demos/
│   └── demo.png
├── figs/
│   └── banner.png
├── traffics/
│   └── extract_youtube_traffic.py
├── i18n/
│   └── localized README.md variants
└── .github/
    └── FUNDING.yml
```

## 🎬 Demo

![Domain & IP Manager demo](demos/demo.png)

## 🧾 Data Files

`data/` 中的資料檔為純文字逐行格式：

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

同樣的命名規則也適用於 `gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw` 與 `default`。

## 🧪 Examples

直接執行某個解析器：

```bash
python3 code/nslookup_simplified_gfw.py
```

常見輸出樣式：

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

將自訂輸入檔輸出為 JSON：

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Development Notes

- 共享 loader 與解析輔助邏輯位於 `code/list_utils.py`。
- 輸出寫入工具採用穩定排序，確保可重現的工件。
- 本專案目前尚未建置自動化測試框架。
- 這是一個以腳本為主的專案，未提供 `setup.py` / `pyproject.toml`。
- `.github/FUNDING.yml` 與 `figs/*` 資產可看出贊助與資金機制。

## 🧯 Troubleshooting

- `Input file not found: domain_and_ips.txt`
  - 請使用 `python3 code/unique_sort.py -i <path> -o <path>` 指向有效輸入，或確認 `domain_and_ips.txt` 已存在於 repo 根目錄。
- DNS 解析逾時或失敗
  - 先確認網路與 DNS 存取，然後重試。
- GUI 無法在 5000 埠啟動
  - 確認已安裝 `flask`，且 `127.0.0.1:5000` 沒有其他程序佔用。
- OCR 工具錯誤
  - 確認 `ffmpeg` 與 `tesseract` 已安裝並可由 `PATH` 取得。

## 🗺️ Roadmap

- 新增用於 parsing、mask 套用與正規化的單元測試。
- 為所有腳本與通用參數補齊清楚的 CLI 說明。
- 提供 Python 依賴的 lock 檔或可重現環境定義。
- 在 GUI 加上失敗 DNS 解析與合併結果差異的匯出/預覽提示。

## 🤝 Contributing

歡迎提交貢獻。建議作法：

1. 開立一則 issue 說明問題或功能需求。
2. 保持變更聚焦且可重現。
3. 在 PR 說明中註明預期指令使用方式與輸出變更。
4. 當行為或指令變更時同步更新 `README.md`。

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Contact

- 有錯誤回報與功能需求請開 GitHub issue。
- 建議在回報中附上簡潔的重現步驟、預期輸出與相關指令上下文。

## 📄 License

在目前這個快照中，儲存庫根目錄沒有追蹤到 `LICENSE` 檔。
