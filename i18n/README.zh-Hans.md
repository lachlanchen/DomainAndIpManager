[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

用于 AI 与 GFW 场景的域名/IP 列表管理工具，可执行 DNS 查询并导出带时间戳的结果。包含 CLI 脚本与 GUI 编辑器。

## 🚀 概览

DomainAndIpManager 是一个 Python 工具集，主要用于：
- 维护多个列表集合（`ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default`）。
- 解析域名 `A` 记录并转换为 `IP/mask` 条目。
- 将域名解析得到的 IP 与自定义 IP、CIDR 数据源合并。
- 为后续网络/路由工作流导出确定性、带时间戳的输出文件。

同时支持：
- 位于 `code/nslookup*.py` 的 CLI 工作流与排序工具。
- 基于 Flask 的 Web GUI（`code/gui_app.py` + `gui/*`），用于交互式编辑列表与执行查询。

### 一目了然

| 区域 | 你将获得 |
|---|---|
| 列表集合 | `ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default` |
| 交互方式 | CLI 脚本 + Flask GUI |
| 输出风格 | 带时间戳的文本快照 + 排序后的 TXT/JSON |
| 主流程 | 编辑列表 → 解析域名 → 合并自定义网段 → 导出 |
| 可选辅助 | `traffics/` 下的 YouTube 流量 OCR 提取 |

## 🎬 演示

![Domain & IP Manager demo](demos/demo.png)

## ✨ 功能特性

- 多列表集合工作流：`ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default`。
- GUI 列表编辑器，支持保存/加载/运行/复制流程。
- 可选包含控制：域名、自定义 IP、CIDR 网段。
- 输出模式切换：`Domains + IPs` 或 `IPs only`。
- GUI 中提供查询失败报告。
- 在 `output/` 下生成带时间戳的输出快照。
- 提供工具将混合域名/IP 输入去重并排序，输出 TXT/JSON。
- `traffics/` 下提供可选流量 OCR 辅助工具（面向 YouTube 提取）。

## 🗂️ 项目结构

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

## ✅ 先决条件

- Python `3.10+`（推荐；代码使用了较新的类型语法）。
- `pip`。
- 用于 DNS 查询的网络连接。
- OCR 辅助工具可选依赖：`PATH` 中可用的 `ffmpeg` 与 `tesseract` 二进制程序。

## 📦 安装

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

依赖安装：

```bash
pip install -r requirements.txt
```

## 🖥️ 快速开始（GUI）

```bash
./start_gui.sh
```

打开 `http://127.0.0.1:5000`。

说明：
- `start_gui.sh` 会引导创建 `.venv`，当 `requirements.txt` 变更时安装依赖，并启动 `code/gui_app.py`。
- 你也可以直接运行 `python3 code/gui_app.py`。

## 🧭 使用方式

### GUI 用法

1. 选择列表集合（`AI + GFW`、`AI`、`GFW`、`GFW (No AI)`、`Non-GFW (China)`、`Default`）。
2. 编辑 `Domains`、`Custom IPs`、`CIDR` 文本区域。
3. 设置 `Mask` 与输出模式（`Domains + IPs` 或 `IPs only`）。
4. 点击 `Save` 将变更保存到 `data/*.txt`。
5. 点击 `Run` 执行解析并生成输出。
6. 点击 `Copy` 复制当前输出。

### CLI 用法

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

每个脚本都会在终端打印结果，并写入 `output/<script>_YYYYMMDD_HHMMSS.txt`。

### 排序与规范化工具

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` 支持自定义输入/输出参数并写出 JSON。
- `unique_sort_print.py` 会打印排序后的域名/IP，并将 TXT 与 JSON 一并写入 `output/`。
- 如果仓库根目录不存在 `domain_and_ips.txt`，请为 `unique_sort.py` 使用 `-i <path>`，或先创建该文件。

### 可选流量提取辅助工具

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

该辅助工具会在 `traffics/` 中生成基于 OCR 的域名/IP Markdown 报告，并依赖外部工具（`ffmpeg`、`tesseract`）。

## 🧾 数据文件

列表文件按行存储，位于 `data/`：
- `ai_*`：仅 AI 列表
- `gfw_*`：GFW 列表
- `ai_gfw_*`：组合列表
- `gfw_wo_ai_*`：不含 AI 的 GFW 列表
- `non_gfw_*`：中国可访问（非 GFW）列表
- `default_*`：传统/默认列表

示例：

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### 列表集合矩阵

| 列表集合 | 域名文件 | 自定义 IP 文件 | CIDR 文件 | Mask 文件 |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ 配置

- 每个列表文件一行一个条目。
- 以 `#` 开头的行会被共享的列表加载逻辑视为注释，并在查询运行时忽略。
- Mask 按列表集合存储在 `data/<list>_mask.txt` 中。

当前仓库状态：
- 目前已提交的所有 mask 文件均为 `30`（`ai`、`gfw`、`ai_gfw`、`gfw_wo_ai`、`non_gfw`、`default`）。

保留自早期 README 版本的说明（为兼容性上下文保留）：
- `*_mask.txt` 控制 CIDR mask（默认是 `32`，`default` 列表使用 `24`）。
- 说明：在当前已提交的数据与脚本默认设置下，实际运行默认值为 `30`，除非被覆盖。

## 📤 输出

- GUI + CLI：`output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- 排序工具：`output/domain_and_ips_unique_sorted.txt` 和 `.json`

## 🧪 示例

CLI 运行示例：

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

典型输出形态：

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

自定义 JSON 规范化示例：

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ 开发说明

- 代码风格：Python 3、PEP 8、4 空格缩进、`snake_case` 命名。
- 脚本设计目标是 CLI 友好且基本保持单一职责。
- 多个 `nslookup` 变体当前共享近似相同逻辑，仅列表键映射不同。
- 当前仓库暂无自动化测试。

## 🧯 故障排查

- `Input file not found: domain_and_ips.txt`：
  - 为 `code/unique_sort.py` 提供 `-i <input-file>`，或在仓库根目录创建 `domain_and_ips.txt`。
- GUI 未自动打开：
  - 启动后手动访问 `http://127.0.0.1:5000`。
- 某些域名 DNS 结果为空：
  - 检查网络/DNS 可用性；未解析域名会显示在 GUI 的 `Failed Lookups`。
- 依赖缺失：
  - 运行 `pip install -r requirements.txt`。
- OCR 辅助工具提示命令缺失：
  - 安装 `ffmpeg` 和 `tesseract`，并确认二者在 `PATH` 中。

## 🗺️ 路线图

- 为解析、排序与查询边界情况添加自动化测试。
- 通过共享的参数化执行器减少 `nslookup` 各变体间的重复逻辑。
- 扩展 `i18n/` 下的多语言文档。
- 增加可选 CI 检查（lint 与 smoke tests）。

## 🤝 贡献

欢迎贡献。

建议流程：
1. 为你的变更创建分支。
2. 保持提交聚焦且使用祈使句（例如：`Limit domain list to ChatGPT, Claude, and Google AI`）。
3. 如变更影响生成数据行为，请附上命令输出示例。
4. 提交 PR 时附上简要说明和任何依赖/运行时说明。

## 📄 许可证

仓库根目录当前没有明确的 `LICENSE` 文件。如果你计划分发或复用此项目，请先补充或确认许可证条款。

## 💖 支持

资金支持元数据也可在 `.github/FUNDING.yml` 中查看。

- GitHub Sponsors：`https://github.com/sponsors/lachlanchen`
- 项目链接：`https://lazying.art`、`https://chat.lazying.art`、`https://onlyideas.art`

### 捐赠二维码（如需直接支持）

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 备注

- 数据文件每行一个条目。
- `*_mask.txt` 控制 CIDR mask（默认是 `32`，`default` 列表使用 `24`）。
- i18n 状态说明：本仓库已包含 `i18n/`；本地化 README 正在规划中，且应在顶部保持单行语言选项栏。
