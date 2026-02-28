[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

管理 AI 與 GFW 情境的網域/IP 清單、執行 DNS 查詢，並匯出帶時間戳記的輸出檔案。包含 CLI 腳本與 GUI 編輯器。

## 🚀 概覽

DomainAndIpManager 是一套 Python 工具集，可用於：
- 維護多組清單（`ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default`）。
- 解析網域 `A` 記錄並轉換為 `IP/mask` 項目。
- 將網域解析得到的 IP 與自訂 IP、CIDR 來源合併。
- 匯出可重現、帶時間戳記的輸出檔，供後續網路/路由流程使用。

同時支援：
- `code/nslookup*.py` 與排序工具的 CLI 工作流。
- 以 Flask 為基礎的 Web GUI（`code/gui_app.py` + `gui/*`），可互動式編輯清單並執行查詢。

### 一覽

| 區域 | 可獲得內容 |
|---|---|
| 清單集合 | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| 介面 | CLI 腳本 + Flask GUI |
| 輸出形式 | 帶時間戳記的文字快照 + 排序後 TXT/JSON |
| 主要流程 | 編輯清單 → 解析網域 → 合併自訂範圍 → 匯出 |
| 可選輔助 | `traffics/` 下的 YouTube 流量 OCR 擷取 |

## 🎬 Demo

![Domain & IP Manager demo](demos/demo.png)

## ✨ 功能

- 多清單集合工作流：`ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default`。
- GUI 清單編輯器，含 save/load/run/copy 流程。
- 可選擇是否納入 domains、custom IPs 與 CIDR blocks。
- 輸出模式切換：`Domains + IPs` 或 `IPs only`。
- GUI 提供查詢失敗報告。
- 於 `output/` 產生帶時間戳記的輸出快照。
- 工具可將混合 domain/IP 輸入去重與排序並輸出 TXT/JSON。
- `traffics/` 下提供可選流量 OCR 輔助工具（偏向 YouTube 擷取）。

## 🗂️ 專案結構

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

## ✅ 先決條件

- Python `3.10+`（建議；程式碼使用較新的型別語法）。
- `pip`。
- 可用於 DNS 查詢的網路連線。
- OCR 輔助工具為可選：需在 `PATH` 中可找到 `ffmpeg` 與 `tesseract`。

## 📦 安裝

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

相依套件：

```bash
pip install -r requirements.txt
```

## 🖥️ 快速開始（GUI）

```bash
./start_gui.sh
```

開啟 `http://127.0.0.1:5000`。

說明：
- `start_gui.sh` 會建立 `.venv`、在 `requirements.txt` 變更時安裝相依套件，並啟動 `code/gui_app.py`。
- 也可直接使用 `python3 code/gui_app.py` 執行。

## 🧭 使用方式

### GUI 使用

1. 選擇清單集合（`AI + GFW`、`AI`、`GFW`、`GFW (No AI)`、`Non-GFW (China)`、`Default`）。
2. 編輯 `Domains`、`Custom IPs` 與 `CIDR` 文字區塊。
3. 設定 `Mask` 與輸出模式（`Domains + IPs` 或 `IPs only`）。
4. 點擊 `Save` 以儲存變更到 `data/*.txt`。
5. 點擊 `Run` 進行解析並產生輸出。
6. 點擊 `Copy` 複製目前輸出。

### CLI 使用

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

每個腳本都會在終端機輸出結果，並寫入 `output/<script>_YYYYMMDD_HHMMSS.txt`。

### 排序與正規化工具

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` 支援自訂輸入/輸出參數，並寫出 JSON。
- `unique_sort_print.py` 會列印排序後的 domains/IPs，並在 `output/` 寫出 TXT 與 JSON。
- 若 repo 根目錄不存在 `domain_and_ips.txt`，請對 `unique_sort.py` 使用 `-i <path>` 或自行建立檔案。

### 可選流量擷取輔助工具

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

此輔助工具會在 `traffics/` 產生由 OCR 推導的網域/IP Markdown 報告，且需要外部工具（`ffmpeg`、`tesseract`）。

## 🧾 資料檔案

清單採逐行格式，存放於 `data/`：
- `ai_*`：僅 AI 清單
- `gfw_*`：GFW 清單
- `ai_gfw_*`：合併清單
- `gfw_wo_ai_*`：不含 AI 的 GFW 清單
- `non_gfw_*`：中國可存取（非 GFW）清單
- `default_*`：舊版/預設清單

範例：

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### 清單集合對照表

| List set | Domains file | Custom IPs file | CIDR file | Mask file |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ 設定

- 每個清單檔案皆為一行一筆。
- 以 `#` 開頭的行會由共用清單載入邏輯視為註解，並在查詢執行時忽略。
- Mask 依各清單集合儲存在 `data/<list>_mask.txt`。

目前儲存庫狀態：
- 目前所有隨附的 mask 檔皆為 `30`（`ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default`）。

保留自舊版 README 的說明（為相容性背景而保留）：
- `*_mask.txt` 控制 CIDR mask（預設為 `32`，`default` 清單使用 `24`）。
- 補充：在目前已提交的資料與腳本預設中，實際執行預設為 `30`，除非另行覆寫。

## 📤 輸出

- GUI + CLI：`output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- 排序工具：`output/domain_and_ips_unique_sorted.txt` 與 `.json`

## 🧪 範例

CLI 執行範例：

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

典型輸出格式：

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

自訂 JSON 正規化範例：

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ 開發說明

- 程式風格：Python 3、PEP 8、4 空白縮排、`snake_case` 命名。
- 腳本刻意保持 CLI 友善，且多為單一用途。
- 多個 `nslookup` 變體目前邏輯近乎相同，差異在清單鍵值對應。
- 此儲存庫目前尚未提供自動化測試。

## 🧯 疑難排解

- `Input file not found: domain_and_ips.txt`：
  - 對 `code/unique_sort.py` 指定 `-i <input-file>`，或在 repo 根目錄建立 `domain_and_ips.txt`。
- GUI 未自動開啟：
  - 啟動後手動開啟 `http://127.0.0.1:5000`。
- 某些網域 DNS 結果為空：
  - 確認網路/DNS 可用性；未解析項目會顯示於 GUI 的 `Failed Lookups`。
- 缺少相依套件：
  - 執行 `pip install -r requirements.txt`。
- OCR 輔助工具因命令缺失而失敗：
  - 安裝 `ffmpeg` 與 `tesseract`，並確保兩者皆在 `PATH`。

## 🗺️ 路線圖

- 新增解析、排序與查詢邊界情況的自動化測試。
- 以共享、可參數化的 runner 減少 `nslookup` 變體間重複邏輯。
- 擴充 `i18n/` 下的多語文件。
- 新增可選 CI 檢查（lint 與 smoke tests）。

## 🤝 貢獻

歡迎貢獻。

建議流程：
1. 為你的變更建立分支。
2. 讓 commit 保持聚焦且使用祈使句（例如：`Limit domain list to ChatGPT, Claude, and Google AI`）。
3. 變更產生資料行為時，附上命令輸出範例。
4. 開 PR 時附上簡短摘要，以及任何相依/執行環境說明。

## 📄 授權

目前儲存庫根目錄未提供明確的 `LICENSE` 檔案。若你打算散布或重用本專案，請先新增或確認授權條款。

## 💖 支持

資助資訊亦可參考 `.github/FUNDING.yml`。

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- Project links: `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### Donation QR（若你想直接支持）

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 備註

- 資料檔案一行一筆。
- `*_mask.txt` 控制 CIDR mask（預設為 `32`，`default` 清單使用 `24`）。
- i18n 狀態說明：本儲存庫已有 `i18n/`；在地化 README 已規劃，且應在頂端保留單行語言選項列。
