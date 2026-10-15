[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner — apps and four buddies](https://lazying.art/media/brand/lazyingart-intro.gif)](https://lazying.art)

# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Mode](https://img.shields.io/badge/Mode-CLI%20%2F%20GUI-1f6feb)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Locale](https://img.shields.io/badge/Docs-English%20%7C%209%20More-0ea5e9?logo=googletranslate&logoColor=white)
![License](https://img.shields.io/badge/License-Not%20Included-9ca3af)

这是一个 Python 工具集，用于维护筛选后的域名 / IP / CIDR 列表集，解析 DNS 到确定性 IP 块、去重，并导出可复现快照，便于路由与过滤工作流使用。

| Focus | Details |
|---|---|
| Domain sets | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Core workflows | DNS 解析、确定性合并、标准化、导出 |
| Output artifacts | `output/` 下按时间戳生成的 TXT 与 JSON 快照 |
| Interfaces | CLI 脚本 + 本地运行的 Flask GUI（`code/gui_app.py`） |
| Data format | `data/` 中的行式域名/IP/CIDR 文本文件 |

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
| Core workflows | DNS 解析 + 合并、去重/排序、GUI 编辑、快照导出 |
| Output formats | TXT + JSON |
| Primary output directory | `output/` |
| Primary entrypoints | `code/` 下的 CLI 脚本 + `gui_app.py` 提供的 Flask GUI |

## 🚀 Overview

DomainAndIpManager 设计用于可重复生成列表：

- 在 `data/` 中维护独立的列表集合（域名 + 自定义 IP + CIDR + 掩码文件）
- 将域名解析为 IP 并转换为 CIDR 风格条目
- 将解析结果与自定义/精选网络块合并
- 导出确定性产物（TXT + JSON），并保持稳定顺序、可选时间戳快照
- 可通过 CLI 运行，也可启动 Web GUI 进行交互式编辑与重新生成

## ✨ Features

| Area | Details |
|---|---|
| Multi-list profiles | 为策略化路由保留独立的列表集合（`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`） |
| DNS resolution | `code/nslookup*.py` 脚本用于域名 → IP 块扩展 |
| Sorting / de-duplication | `code/unique_sort*.py` 处理混合域名/IP/CIDR 输入并进行标准化与去重 |
| Deterministic export | 带稳定顺序的 TXT + JSON 输出，可生成可选时间戳快照 |
| GUI editing | 通过 `gui/` 交互编辑 `domains`、`custom_ips`、`cidr` 和掩码设置 |
| Diagnostics | 可选输出解析失败项，便于排障 |
| Optional OCR utility | `traffics/` 提供用于 YouTube/视频提取流程的 OCR 辅助 |

---

## ✅ Prerequisites

| Requirement | Notes |
|---|---|
| Python | 3.10+（推荐） |
| Network | DNS 查询需要可访问互联网 |
| Python packages | `pip` 与 `requirements.txt` 中的依赖 |
| Git | 克隆与更新仓库所需 |
| OCR optional stack | 使用流量提取工具时需要 `ffmpeg` + `tesseract` |

---

## 📦 Installation

```bash
python3 -m pip install -r requirements.txt
```

快速安装：

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> 假设：直接使用 CLI 时不强制要求提前创建虚拟环境；如需可优先使用 `start_gui.sh`，它会按需自动创建并使用 `.venv`。

## 🧭 Usage

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` 会启动 `code/gui_app.py`，并提供：

- URL: `http://127.0.0.1:5000`
- 基于 GUI 的列表文件编辑能力
- 按需生成并提供可直接复制的输出预览
- 必要时自动创建 `.venv`，并自动安装/更新依赖

你也可以直接运行：

```bash
python3 code/gui_app.py
```

### CLI Reference

| Common task | Command |
|---|---|
| 解析 AI 聚焦列表 | `python3 code/nslookup_simplified.py` |
| 解析 GFW 聚焦列表 | `python3 code/nslookup_simplified_gfw.py` |
| 解析 GFW + AI 合并列表 | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| 解析不包含 AI 的 GFW 列表 | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| 执行基础解析流程 | `python3 code/nslookup.py` |
| 排序并去重列表到 JSON | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| 导出标准 TXT/JSON | `python3 code/unique_sort_print.py` |

说明：

- 输出文件按 `output/<script>_YYYYMMDD_HHMMSS.txt` 命名，带时间戳后缀。
- 排序脚本通过参数支持自定义输入与输出路径。

### Optional OCR Utility

```bash
python3 traffics/extract_youtube_traffic.py \\
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \\
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

需要 `PATH` 可访问 `ffmpeg` 与 `tesseract`。

## ⚙️ Configuration

- 所有 `data/` 文本文件保持每行一条记录。
- 当前的共享列表加载逻辑会忽略以 `#` 开头的注释行。
- 每个列表的掩码存储在 `data/<set>_mask.txt`。
- 仓库内提交的掩码值由 `data/*_mask.txt` 的内容决定。
- 写入前会将输入标准化为确定性去重顺序。

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
| `code/nslookup.py` | 基础域名/IP 解析运行器 |
| `code/nslookup_simplified.py` | AI 聚焦解析 + CIDR 导出 |
| `code/nslookup_simplified_gfw.py` | GFW 聚焦解析 |
| `code/nslookup_simplified_gfw_w_ai.py` | 合并 GFW + AI 解析 |
| `code/nslookup_simplified_gfw_wo_ai.py` | 排除 AI 的 GFW 解析 |
| `code/unique_sort.py` | 标准化 + 去重 + JSON 输出 |
| `code/unique_sort_print.py` | 打印 + 写入标准 TXT/JSON 产物 |
| `code/list_utils.py` | 共享加载器、掩码与列表辅助方法 |
| `code/gui_app.py` | Flask GUI 后端 |
| `traffics/extract_youtube_traffic.py` | 用于流量提取的可选 OCR 工具 |
| `start_gui.sh` | 虚拟环境引导、依赖安装和服务启动 |

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

`data/` 下的数据文件为纯文本逐行格式：

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

同样的命名规则适用于 `gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw` 和 `default`。

## 🧪 Examples

直接运行某个解析脚本：

```bash
python3 code/nslookup_simplified_gfw.py
```

典型输出示例：

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

排序自定义输入文件到 JSON：

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Development Notes

- 共享加载器和解析辅助逻辑位于 `code/list_utils.py`。
- 输出写入器使用确定性排序，生成可复现的产物。
- 当前仓库尚未包含自动化测试框架。
- 仓库中未包含 `setup.py` / `pyproject.toml`，这是一个脚本优先项目。
- `.github/FUNDING.yml` 与 `figs/*` 资源反映了捐赠/赞助集成信息。

## 🧯 Troubleshooting

- `Input file not found: domain_and_ips.txt`
  - 使用 `python3 code/unique_sort.py -i <path> -o <path>` 指定有效输入路径，或确保仓库根目录存在 `domain_and_ips.txt`。
- DNS 查找超时或失败
  - 检查网络连接与 DNS 可达性后重试。
- GUI 启动失败（端口 5000）
  - 确认已安装 `flask`，且没有其他进程占用 `127.0.0.1:5000`。
- OCR 工具报错
  - 确认 `ffmpeg` 与 `tesseract` 已安装并可在 `PATH` 中找到。

## 🗺️ Roadmap

- 为解析、掩码应用和标准化工具补充单元测试。
- 为所有脚本及常用参数补充清晰的 CLI 帮助。
- 增加 Python 依赖锁文件或可复现环境定义。
- 在 GUI 中增加失败 DNS 解析和合并输出差异的导出/预览提示。

## 🤝 Contributing

欢迎贡献代码。建议流程：

1. 创建问题单描述问题或功能需求。
2. 保持改动集中且可复现。
3. 在 PR 描述中记录预期命令用法和输出变化。
4. 行为或命令变更时同步更新 `README.md`。

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Contact

- 如有 bug 报告或功能请求，请在 GitHub 开 Issue。
- 在 Issue 中请尽量提供简洁的复现步骤、预期输出与执行命令上下文。

## 📄 License

当前快照中，仓库根目录未跟踪 `LICENSE` 文件。
