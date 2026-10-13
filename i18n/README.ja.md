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

ドメイン / IP / CIDR の厳選リストセットを管理し、DNS を決定論的な IP ブロックへ変換して重複排除し、ルーティングやフィルタリングのワークフローで使える再現可能なスナップショットとしてエクスポートする Python ツールキットです。

| Focus | Details |
|---|---|
| Domain sets | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Core workflows | DNS 解決、決定論的マージ、正規化、エクスポート |
| Output artifacts | `output/` 配下のタイムスタンプ付き TXT と JSON スナップショット |
| Interfaces | CLI スクリプト + Flask GUI（`code/gui_app.py`、ローカル起動） |
| Data format | `data/` の行ベースの domain/IP/CIDR テキストファイル |

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
| Domain sets | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Core workflows | DNS 解決 + 結合、重複排除/ソート、GUI 編集、スナップショット出力 |
| Output formats | TXT + JSON |
| Primary output directory | `output/` |
| Primary entrypoints | `code/` 配下の CLI スクリプト、`gui_app.py` の Flask GUI |

## 🚀 Overview

DomainAndIpManager は再現可能なリスト生成を目的に設計されています。

- `data/` で専用のリストセットを分離して管理する（domains + custom IPs + CIDR + mask の各ファイル）
- ドメイン名を IP に解決し、CIDR 形式のエントリへ変換する
- 解決結果をカスタム/キュレーション済みのネットワークブロックとマージする
- 決定論的な順序で TXT + JSON の成果物を出力し（必要に応じてタイムスタンプ付きスナップショットも）、安定再現性を確保する
- CLI か Web GUI で実行し、インタラクティブ編集や再生成が可能

## ✨ Features

| Area | Details |
|---|---|
| Multi-list profiles | 戦略別ルーティングのために `ai` / `gfw` / `ai_gfw` / `gfw_wo_ai` / `non_gfw` / `default` の独立セットを保持 |
| DNS resolution | ドメイン → IP ブロック拡張を行う `code/nslookup*.py` |
| Sorting / de-duplication | `code/unique_sort*.py` が domain/IP/CIDR 混在入力の正規化と重複排除を実施 |
| Deterministic export | 安定した並び順で TXT + JSON を出力、タイムスタンプ付きスナップショットも生成 |
| GUI editing | `gui/` から `domains` / `custom_ips` / `cidr` / mask 設定を対話編集 |
| Diagnostics | 解決失敗レポート（オプション）でトラブルシューティングを支援 |
| Optional OCR utility | YouTube / 動画向けの `traffics/` 補助 OCR ツール |

---

## ✅ Prerequisites

| Requirement | Notes |
|---|---|
| Python | 3.10+（推奨） |
| Network | DNS 参照を実行するためのインターネット接続 |
| Python packages | `pip` および `requirements.txt` の依存関係 |
| Git | リポジトリのクローン/更新に必要 |
| OCR optional stack | `traffics/` のトラフィック抽出を使う場合は `ffmpeg` + `tesseract` |

---

## 📦 Installation

```bash
python3 -m pip install -r requirements.txt
```

Quick setup:

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> 想定: 直接の CLI 利用に追加の仮想環境初期化は必須ではありません。必要なら `start_gui.sh` が `.venv` を自動生成して利用します。

## 🧭 Usage

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` は `code/gui_app.py` を起動し、次を提供します。

- URL: `http://127.0.0.1:5000`
- リストファイル編集用の GUI バックエンド
- 必要時に生成し、コピーしやすい出力プレビューを表示
- 必要に応じて `.venv` を作成し、依存関係のインストール/更新を実行

直接起動も可能です。

```bash
python3 code/gui_app.py
```

### CLI Reference

| Common task | Command |
|---|---|
| AI 向けドメインを解決 | `python3 code/nslookup_simplified.py` |
| GFW 向けドメインを解決 | `python3 code/nslookup_simplified_gfw.py` |
| GFW + AI の統合リストを解決 | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| GFW から AI を除いたリストを解決 | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| ベースリゾルバーパスを実行 | `python3 code/nslookup.py` |
| JSON へソート＋重複排除 | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| 公式 TXT/JSON をエクスポート | `python3 code/unique_sort_print.py` |

Notes:

- 出力ファイルは `output/<script>_YYYYMMDD_HHMMSS.txt` のようなタイムスタンプ付きファイル名で書き込まれます。
- ソート系スクリプトは、`-i`/`-o` フラグで入力・出力パスを指定できます。

### Optional OCR Utility

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

`PATH` に `ffmpeg` と `tesseract` が必要です。

## ⚙️ Configuration

- `data/` 配下のテキストファイルは 1 行 1 項目で管理します。
- `#` で始まるコメント行は、現在の共通リストローダーで無視されます。
- セットごとのマスクは `data/<set>_mask.txt` に保持されます。
- いまチェックインされているマスク値は `data/*_mask.txt` の内容に依存します。
- 入力は書き込み前に決定論的で重複排除済みの順序へ変換されます。

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
| `code/nslookup.py` | ベースの domain/IP 解決ランナー |
| `code/nslookup_simplified.py` | AI 向け解決 + CIDR エクスポート |
| `code/nslookup_simplified_gfw.py` | GFW 向け解決 |
| `code/nslookup_simplified_gfw_w_ai.py` | GFW + AI 統合解決 |
| `code/nslookup_simplified_gfw_wo_ai.py` | GFW から AI を除いて解決 |
| `code/unique_sort.py` | 正規化 + 重複排除 + JSON 出力 |
| `code/unique_sort_print.py` | 標準 TXT/JSON 成果物の表示 + 書き込み |
| `code/list_utils.py` | 共通ローダー、マスク、リストユーティリティ |
| `code/gui_app.py` | Flask GUI バックエンド |
| `traffics/extract_youtube_traffic.py` | トラフィック抽出のための任意 OCR 補助 |
| `start_gui.sh` | 仮想環境初期化 + 依存インストール + サーバ起動 |

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

`data/` のデータは行区切りのテキストです。

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

同様の命名パターンは `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` にも適用されます。

## 🧪 Examples

リゾルバーを直接 1 つ実行:

```bash
python3 code/nslookup_simplified_gfw.py
```

典型的な出力形式:

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

カスタム入力ファイルを JSON へソート:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## ✅ Development Notes

- 共有ローダーとリゾルバー支援ロジックは `code/list_utils.py` にあります。
- 出力ライターは再現可能性のある順序を保証する決定論的な並び順を使用します。
- 現在このリポジトリに自動テストフレームワークはありません。
- `setup.py` / `pyproject.toml` はありません。スクリプト中心の構成です。
- `.github/FUNDING.yml` と `figs/*` のアセットには寄付/支援の統合情報が含まれています。

## 🧯 Troubleshooting

- `Input file not found: domain_and_ips.txt`
  - `python3 code/unique_sort.py -i <path> -o <path>` で有効な入力パスを指定するか、リポジトリルートに `domain_and_ips.txt` を追加してください。
- DNS lookup timeouts or failures
  - ネットワーク接続と DNS 到達性を確認し、再実行してください。
- GUI fails to start on port 5000
  - `flask` がインストール済みであること、`127.0.0.1:5000` を既に使用しているプロセスがないことを確認してください。
- OCR utility errors
  - `ffmpeg` と `tesseract` がインストールされ、`PATH` から参照可能であることを確認してください。

## 🗺️ Roadmap

- 解析、マスク適用、正規化ユーティリティ向けにユニットテストを追加。
- すべてのスクリプトと主要フラグに対する明確な CLI ヘルプを追加。
- Python 依存関係のロックファイルまたは再現可能な環境定義を提供。
- 失敗した DNS 解決と結合結果差分を GUI で可視化するエクスポート/プレビュー指標を追加。

## 🤝 Contributing

Contribution は歓迎します。推奨ワークフロー:

1. 問題点や機能要望を整理して issue を作成します。
2. 変更は小さく、再現可能に保ちます。
3. 期待するコマンド利用と出力の変化を PR 説明に記載します。
4. 挙動やコマンドが変わった場合は `README.md` を更新します。

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Contact

- 不具合報告や機能要望は GitHub issue で受け付けます。
- issue では再現手順、期待される出力、実行コマンドの情報を簡潔に記載してください。

## 📄 License

この時点ではリポジトリルートに明示的な `LICENSE` ファイルはありません。
