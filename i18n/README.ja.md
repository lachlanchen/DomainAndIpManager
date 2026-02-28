[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

AI および GFW 向けのドメイン/IP リストを管理し、DNS ルックアップを実行して、タイムスタンプ付き出力を生成します。CLI スクリプトと GUI エディタを含みます。

## 🚀 概要

DomainAndIpManager は、以下を行う Python ツールキットです。
- 複数のリストセット（`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`）を維持管理。
- ドメインの `A` レコードを解決し、`IP/mask` エントリに変換。
- ドメイン由来 IP とカスタム IP/CIDR ソースを統合。
- 後段のネットワーク/ルーティング運用向けに、再現性のあるタイムスタンプ付き出力ファイルを生成。

以下の両方をサポートします。
- `code/nslookup*.py` とソート系ユーティリティによる CLI ワークフロー。
- Flask ベースの Web GUI（`code/gui_app.py` + `gui/*`）による対話的なリスト編集とルックアップ実行。

### 一覧

| 項目 | 得られるもの |
|---|---|
| リストセット | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| インターフェース | CLI スクリプト + Flask GUI |
| 出力形式 | タイムスタンプ付きテキストスナップショット + ソート済み TXT/JSON |
| 主なワークフロー | リスト編集 → ドメイン解決 → カスタムレンジ統合 → エクスポート |
| オプション補助 | `traffics/` 配下の YouTube トラフィック OCR 抽出 |

## 🎬 デモ

![Domain & IP Manager demo](demos/demo.png)

## ✨ 機能

- 複数リストセット運用: `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`。
- 保存/読み込み/実行/コピーに対応した GUI リストエディタ。
- ドメイン、カスタム IP、CIDR ブロックの任意の有効化制御。
- 出力モード切替: `Domains + IPs` または `IPs only`。
- GUI での失敗ルックアップ報告。
- `output/` 配下へのタイムスタンプ付き出力スナップショット。
- 混在ドメイン/IP 入力を重複排除・ソートして TXT/JSON に整形するユーティリティ。
- `traffics/` 配下のオプション OCR 補助（YouTube 向け抽出）。

## 🗂️ プロジェクト構成

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

## ✅ 前提条件

- Python `3.10+`（推奨。コードで新しい型構文を使用）。
- `pip`。
- DNS クエリのためのネットワーク接続。
- OCR 補助を使う場合: `PATH` 上で利用可能な `ffmpeg` と `tesseract`。

## 📦 インストール

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

依存関係:

```bash
pip install -r requirements.txt
```

## 🖥️ クイックスタート（GUI）

```bash
./start_gui.sh
```

`http://127.0.0.1:5000` を開いてください。

補足:
- `start_gui.sh` は `.venv` を準備し、`requirements.txt` が変更された場合に依存関係をインストールして、`code/gui_app.py` を起動します。
- `python3 code/gui_app.py` で直接起動することもできます。

## 🧭 使い方

### GUI の使い方

1. リストセットを選択（`AI + GFW`, `AI`, `GFW`, `GFW (No AI)`, `Non-GFW (China)`, `Default`）。
2. `Domains`, `Custom IPs`, `CIDR` の各テキストエリアを編集。
3. `Mask` と出力モード（`Domains + IPs` または `IPs only`）を設定。
4. `Save` をクリックして `data/*.txt` に変更を保存。
5. `Run` をクリックして解決と出力生成を実行。
6. `Copy` をクリックして現在の出力をコピー。

### CLI の使い方

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

各スクリプトは結果をターミナルに表示し、`output/<script>_YYYYMMDD_HHMMSS.txt` に書き込みます。

### ソート・正規化ツール

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` は入力/出力のカスタムフラグをサポートし、JSON を書き出します。
- `unique_sort_print.py` はソート済みのドメイン/IP を表示し、TXT と JSON の両方を `output/` に書き出します。
- リポジトリ直下に `domain_and_ips.txt` がない場合は、`unique_sort.py` に `-i <path>` を指定するか、ファイルを作成してください。

### オプションのトラフィック抽出補助

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

この補助ツールは `traffics/` に OCR 由来のドメイン/IP Markdown レポートを生成し、外部ツール（`ffmpeg`, `tesseract`）が必要です。

## 🧾 データファイル

リストは 1 行 1 エントリ形式で、`data/` 配下に保存されます。
- `ai_*`: AI 専用リスト
- `gfw_*`: GFW リスト
- `ai_gfw_*`: 統合リスト
- `gfw_wo_ai_*`: AI を除いた GFW リスト
- `non_gfw_*`: 中国からアクセス可能（非 GFW）リスト
- `default_*`: 従来/デフォルトリスト

例:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### リストセット対応表

| リストセット | Domains ファイル | Custom IPs ファイル | CIDR ファイル | Mask ファイル |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ 設定

- 各リストファイルは 1 行につき 1 エントリ。
- `#` で始まる行は、共通のリスト読み込みロジックでコメントとして扱われ、ルックアップ実行時に無視されます。
- マスクはリストセットごとに `data/<list>_mask.txt` に保存されます。

現在のリポジトリ状態:
- 同梱されているすべてのマスクファイルには現在 `30` が入っています（`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`）。

以前の README バージョンから保持している注記（互換性コンテキストのため）:
- `*_mask.txt` は CIDR マスクを制御します（デフォルトは `32`、`default` リストは `24`）。
- 補足: 現在コミット済みのデータおよびスクリプト既定値では、上書きしない限り実行時の有効デフォルトは `30` です。

## 📤 出力

- GUI + CLI: `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- ソートツール: `output/domain_and_ips_unique_sorted.txt` と `.json`

## 🧪 例

CLI 実行例:

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

典型的な出力形式:

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

カスタム JSON 正規化例:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ 開発メモ

- コードスタイル: Python 3、PEP 8、4 スペースインデント、`snake_case` 命名。
- スクリプトは CLI での利用しやすさを重視し、主に単機能で設計されています。
- `nslookup` の複数バリアントは現在、リストキーのマッピング違いを除いてほぼ同一ロジックを共有しています。
- このリポジトリには現在、自動テストはありません。

## 🧯 トラブルシューティング

- `Input file not found: domain_and_ips.txt`:
  - `code/unique_sort.py` に `-i <input-file>` を指定するか、リポジトリ直下に `domain_and_ips.txt` を作成してください。
- GUI が自動で開かない:
  - 起動後に `http://127.0.0.1:5000` を手動で開いてください。
- 一部ドメインで DNS 結果が空になる:
  - ネットワーク/DNS の可用性を確認してください。解決できないドメインは GUI の `Failed Lookups` に表示されます。
- 依存関係が不足している:
  - `pip install -r requirements.txt` を実行してください。
- OCR 補助でコマンド不足エラーが出る:
  - `ffmpeg` と `tesseract` をインストールし、両方が `PATH` に通っていることを確認してください。

## 🗺️ ロードマップ

- 解析、ソート、ルックアップの境界ケースに対する自動テストを追加。
- パラメータ化した共通ランナーで `nslookup` バリアント間の重複ロジックを削減。
- `i18n/` 配下の多言語ドキュメントを拡充。
- リントとスモークテスト向けの任意 CI チェックを追加。

## 🤝 コントリビュート

コントリビューションを歓迎します。

推奨ワークフロー:
1. 変更用ブランチを作成。
2. コミットは焦点を絞り、命令形で記述（例: `Limit domain list to ChatGPT, Claude, and Google AI`）。
3. 生成データの挙動を変更する場合は、コマンド出力サンプルを含める。
4. 簡潔な要約と依存関係/実行時メモを添えて PR を作成。

## 📄 ライセンス

リポジトリ直下には現在、明示的な `LICENSE` ファイルがありません。再配布または再利用を予定している場合は、先にライセンス条件を追加または確認してください。

## 💖 サポート

資金提供メタデータは `.github/FUNDING.yml` にもあります。

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- プロジェクトリンク: `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### 寄付用 QR（直接支援したい場合）

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 注記

- データファイルは 1 行 1 エントリ。
- `*_mask.txt` は CIDR マスクを制御します（デフォルトは `32`、`default` リストは `24`）。
- i18n ステータス注記: このリポジトリには `i18n/` が存在し、ローカライズ README では先頭に言語オプション行を 1 行だけ置く必要があります。
