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

도메인/IP/CIDR 목록을 선별적으로 관리하고, DNS 해석을 통해 결정론적 IP 블록으로 변환한 뒤 정렬·중복 제거하여 라우팅 및 필터링 워크플로에서 재현 가능한 스냅샷으로 내보내는 Python 툴킷입니다.

| Focus | Details |
|---|---|
| Domain sets | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Core workflows | DNS resolution, deterministic merging, normalization, export |
| Output artifacts | Timestamped TXT plus JSON snapshots in `output/` |
| Interfaces | CLI scripts + Flask GUI (`code/gui_app.py`, served locally) |
| Data format | Line-based domain/IP/CIDR text files in `data/` |

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
| Core workflows | DNS resolve + merge, dedupe/sort, GUI editing, snapshot export |
| Output formats | TXT + JSON |
| Primary output directory | `output/` |
| Primary entrypoints | CLI scripts under `code/`, Flask GUI in `gui_app.py` |

## 🚀 Overview

DomainAndIpManager는 반복 가능한 목록 생성을 위해 설계되었습니다.

- `data/`에서 관리 영역별로 리스트 세트를 분리해 둡니다. (domains + custom IPs + CIDR + mask 파일)
- 도메인 이름을 IP로 해석하고 CIDR 스타일 항목으로 변환합니다.
- 해석된 항목을 사용자 지정/큐레이션 네트워크 블록과 병합합니다.
- 안정적인 순서의 TXT와 JSON 결과물을 내보내며, 필요 시 타임스탬프가 붙은 스냅샷도 생성합니다.
- CLI로 실행하거나 웹 GUI를 통해 인터랙티브 편집/재생성을 수행합니다.

## ✨ Features

| Area | Details |
|---|---|
| Multi-list profiles | 전략별 라우팅용으로 `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`를 각각 분리 관리 |
| DNS resolution | `code/nslookup*.py` 스크립트로 domain → IP 블록 확장 |
| Sorting / de-duplication | `code/unique_sort*.py`가 domain/IP/CIDR 혼합 입력을 정규화하고 중복 제거 수행 |
| Deterministic export | 안정적인 정렬 순서의 TXT + JSON 출력, 필요 시 타임스탬프 스냅샷 생성 |
| GUI editing | `gui/`에서 `domains`, `custom_ips`, `cidr`, mask 설정을 대화형으로 편집 |
| Diagnostics | DNS 실패 보고(옵션)로 트러블슈팅 지원 |
| Optional OCR utility | YouTube/비디오 추출 워크플로를 위한 `traffics/` OCR 헬퍼 |

---

## ✅ Prerequisites

| Requirement | Notes |
|---|---|
| Python | 3.10+ (권장) |
| Network | DNS 조회를 위한 인터넷 연결 |
| Python packages | `pip` 및 `requirements.txt`의 종속성 |
| Git | 리포지토리 클론/업데이트에 필요 |
| OCR optional stack | 트래픽 추출 유틸리티 사용 시 `ffmpeg` + `tesseract` |

---

## 📦 Installation

```bash
python3 -m pip install -r requirements.txt
```

빠른 설정:

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> 가정: 직접 CLI로 사용할 때는 별도의 가상환경 부트스트랩이 필수는 아닙니다. 선호하는 경우 `start_gui.sh`가 `.venv`를 자동 생성해 사용할 수 있습니다.

## 🧭 Usage

### GUI

```bash
./start_gui.sh
```

`start_gui.sh`는 `code/gui_app.py`를 실행하고 아래 기능을 제공합니다.

- URL: `http://127.0.0.1:5000`
- 리스트 파일 편집용 GUI 기반 인터페이스
- 필요 시 생성하고 바로 복사 가능한 미리보기 출력
- 필요한 경우 `.venv`를 자동 생성하고 의존성 install/update 수행

직접 실행도 가능합니다.

```bash
python3 code/gui_app.py
```

### CLI Reference

| Common task | Command |
|---|---|
| AI 중심 도메인 해석 | `python3 code/nslookup_simplified.py` |
| GFW 중심 도메인 해석 | `python3 code/nslookup_simplified_gfw.py` |
| GFW + AI 통합 도메인 해석 | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| GFW에서 AI를 제외한 해석 | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| 기본 리졸버 경로 실행 | `python3 code/nslookup.py` |
| 목록을 정렬해 JSON으로 저장 | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| 표준 TXT/JSON 내보내기 | `python3 code/unique_sort_print.py` |

참고:

- 출력 파일은 `output/<script>_YYYYMMDD_HHMMSS.txt` 형식으로 타임스탬프 접미사를 붙여 저장됩니다.
- 정렬 스크립트는 `-i`/`-o` 플래그로 커스텀 입력/출력 경로를 지원합니다.

### Optional OCR Utility

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

`PATH`에 `ffmpeg`와 `tesseract`가 있어야 합니다.

## ⚙️ Configuration

- 모든 `data/` 텍스트 파일은 한 줄에 하나의 항목만 담습니다.
- 현재 공유 리스트 로더 로직은 `#`로 시작하는 주석 줄을 무시합니다.
- 리스트별 마스크는 `data/<set>_mask.txt`에 저장됩니다.
- 현재 체크인된 마스크 값은 `data/*_mask.txt` 내용에 따라 결정됩니다.
- 입력은 쓰기 전에 결정론적으로 중복 제거된 순서로 정렬됩니다.

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
| `code/nslookup.py` | 기본 domain/IP 해석 실행기 |
| `code/nslookup_simplified.py` | AI 중심 해석 + CIDR 내보내기 |
| `code/nslookup_simplified_gfw.py` | GFW 중심 해석 |
| `code/nslookup_simplified_gfw_w_ai.py` | GFW + AI 통합 해석 |
| `code/nslookup_simplified_gfw_wo_ai.py` | AI를 제외한 GFW 해석 |
| `code/unique_sort.py` | 정규화 + 중복 제거 + JSON 출력 |
| `code/unique_sort_print.py` | TXT/JSON 표준 아티팩트 출력 및 저장 |
| `code/list_utils.py` | 공통 로더, 마스크, 목록 유틸리티 |
| `code/gui_app.py` | Flask GUI 백엔드 |
| `traffics/extract_youtube_traffic.py` | 트래픽 추출용 OCR 보조 도구 |
| `start_gui.sh` | 가상환경 부트스트랩 + 의존성 설치 + 서버 시작 |

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

data 파일은 `data/`에 줄 단위 텍스트로 저장됩니다.

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

동일한 파일명 규칙이 `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`에도 적용됩니다.

## 🧪 Examples

리졸버를 직접 한 번 실행해 보기:

```bash
python3 code/nslookup_simplified_gfw.py
```

일반적인 출력 예:

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

사용자 입력 파일을 JSON으로 정렬:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Development Notes

- 공유 로더 및 해석기 도우미 로직은 `code/list_utils.py`에 있습니다.
- 출력 writer는 재현 가능한 산출물을 위해 결정론적 순서를 사용합니다.
- 현재 이 저장소에는 자동 테스트 프레임워크가 없습니다.
- `setup.py` / `pyproject.toml`은 없습니다. 스크립트 우선 구조입니다.
- `.github/FUNDING.yml`과 `figs/*` 자산은 기부/후원 연동 정보를 나타냅니다.

## 🧯 Troubleshooting

- `Input file not found: domain_and_ips.txt`
  - 유효한 경로로 `python3 code/unique_sort.py -i <path> -o <path>`를 실행하거나, 리포지토리 루트에 `domain_and_ips.txt`가 있는지 확인하세요.
- DNS 조회 시간 초과 또는 실패
  - 네트워크 연결 및 DNS 접속을 확인한 뒤 다시 실행하세요.
- GUI가 5000 포트에서 시작되지 않음
  - `flask`가 설치되어 있고 `127.0.0.1:5000` 포트를 사용하는 프로세스가 없는지 확인하세요.
- OCR 유틸리티 오류
  - `PATH`에서 `ffmpeg`와 `tesseract`가 설치되고 접근 가능한지 확인하세요.

## 🗺️ Roadmap

- 파싱, 마스크 적용, 정규화 유틸리티에 대한 단위 테스트 추가.
- 모든 스크립트 및 공통 플래그에 대한 명확한 CLI 도움말 추가.
- Python 의존성에 대한 lockfile/재현 가능한 환경 정의 제공.
- GUI에서 DNS 실패 목록 및 병합 결과 diff 미리보기 지표 추가.

## 🤝 Contributing

기여는 환영합니다. 권장 workflow:

1. 문제 또는 기능 요청을 설명하는 이슈를 생성합니다.
2. 변경은 작고 재현 가능하게 유지합니다.
3. PR 설명에 예상 명령 사용법과 출력 변화 내용을 기록합니다.
4. 동작이나 명령이 바뀌었을 때는 `README.md`를 업데이트합니다.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Contact

- 버그 신고와 기능 요청은 GitHub issue로 남겨주세요.
- 이슈에는 재현 단계, 기대 출력, 실행 명령 컨텍스트를 간결하게 적어주세요.

## 📄 License

현재 스냅샷에서는 저장소 루트에 `LICENSE` 파일이 추적되지 않습니다.
