[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

AI 및 GFW 컨텍스트의 도메인/IP 목록을 관리하고, DNS 조회를 실행하며, 타임스탬프가 포함된 결과를 내보내는 도구입니다. CLI 스크립트와 GUI 편집기를 모두 포함합니다.

## 🚀 개요

DomainAndIpManager는 다음을 위한 Python 툴킷입니다:
- 여러 목록 세트 유지 관리(`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).
- 도메인 `A` 레코드 조회 후 `IP/mask` 항목으로 변환.
- 도메인에서 파생된 IP와 사용자 정의 IP/CIDR 소스 결합.
- 후속 네트워크/라우팅 워크플로를 위한 결정론적(deterministic) 타임스탬프 출력 파일 내보내기.

다음 두 방식을 모두 지원합니다:
- `code/nslookup*.py` 및 정렬 유틸리티 기반 CLI 워크플로.
- 목록 편집과 조회를 대화형으로 수행하는 Flask 기반 웹 GUI(`code/gui_app.py` + `gui/*`).

### 한눈에 보기

| 영역 | 제공 내용 |
|---|---|
| 목록 세트 | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| 인터페이스 | CLI 스크립트 + Flask GUI |
| 출력 형식 | 타임스탬프 텍스트 스냅샷 + 정렬된 TXT/JSON |
| 주요 워크플로 | 목록 편집 → 도메인 조회 → 사용자 정의 범위 결합 → 내보내기 |
| 선택 도우미 | `traffics/`의 YouTube 트래픽 OCR 추출 |

## 🎬 데모

![Domain & IP Manager demo](demos/demo.png)

## ✨ 기능

- 멀티 목록 세트 워크플로: `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`.
- 저장/불러오기/실행/복사 흐름을 갖춘 GUI 목록 편집기.
- 도메인, 사용자 정의 IP, CIDR 블록의 선택적 포함 제어.
- 출력 모드 전환: `Domains + IPs` 또는 `IPs only`.
- GUI에서 실패한 조회 결과 보고.
- `output/` 아래 타임스탬프 출력 스냅샷.
- 혼합 도메인/IP 입력을 TXT/JSON으로 중복 제거 및 정렬하는 유틸리티.
- `traffics/` 아래 선택적 트래픽 OCR 도우미(YouTube 중심 추출).

## 🗂️ 프로젝트 구조

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

## ✅ 사전 요구사항

- Python `3.10+` (권장; 코드에서 최신 타입 문법 사용).
- `pip`.
- DNS 질의를 위한 네트워크 연결.
- OCR 도우미(선택): `PATH`에 `ffmpeg`, `tesseract` 바이너리 필요.

## 📦 설치

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

의존성 설치:

```bash
pip install -r requirements.txt
```

## 🖥️ 빠른 시작 (GUI)

```bash
./start_gui.sh
```

`http://127.0.0.1:5000`을 여세요.

참고:
- `start_gui.sh`는 `.venv`를 부트스트랩하고, `requirements.txt` 변경 시 의존성을 설치한 뒤 `code/gui_app.py`를 실행합니다.
- `python3 code/gui_app.py`로 직접 실행할 수도 있습니다.

## 🧭 사용법

### GUI 사용

1. 목록 세트를 선택합니다(`AI + GFW`, `AI`, `GFW`, `GFW (No AI)`, `Non-GFW (China)`, `Default`).
2. `Domains`, `Custom IPs`, `CIDR` 텍스트 영역을 편집합니다.
3. `Mask`와 출력 모드(`Domains + IPs` 또는 `IPs only`)를 설정합니다.
4. `Save`를 눌러 `data/*.txt`에 변경사항을 저장합니다.
5. `Run`을 눌러 조회를 실행하고 출력을 생성합니다.
6. `Copy`를 눌러 현재 출력을 복사합니다.

### CLI 사용

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

각 스크립트는 결과를 터미널에 출력하고 `output/<script>_YYYYMMDD_HHMMSS.txt`를 작성합니다.

### 정렬 및 정규화 도구

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py`는 사용자 지정 입력/출력 플래그를 지원하며 JSON을 작성합니다.
- `unique_sort_print.py`는 정렬된 도메인/IP를 출력하고 `output/`에 TXT와 JSON을 모두 작성합니다.
- 저장소 루트에 `domain_and_ips.txt`가 없다면 `unique_sort.py`에 `-i <path>`를 사용하거나 파일을 생성하세요.

### 선택적 트래픽 추출 도우미

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

이 도우미는 `traffics/`에 OCR 기반 도메인/IP 마크다운 리포트를 생성하며, 외부 도구(`ffmpeg`, `tesseract`)가 필요합니다.

## 🧾 데이터 파일

목록은 한 줄당 하나의 항목으로 `data/` 아래에 저장됩니다:
- AI 전용 목록은 `ai_*`
- GFW 목록은 `gfw_*`
- 결합 목록은 `ai_gfw_*`
- AI 제외 GFW 목록은 `gfw_wo_ai_*`
- 중국에서 접근 가능한(non-GFW) 목록은 `non_gfw_*`
- 레거시/기본 목록은 `default_*`

예시:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### 목록 세트 매트릭스

| List set | Domains file | Custom IPs file | CIDR file | Mask file |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ 구성

- 각 목록 파일은 한 줄당 하나의 항목을 사용합니다.
- `#`로 시작하는 줄은 공용 목록 로딩 로직에서 주석으로 처리되며 조회 실행 시 무시됩니다.
- 마스크는 목록 세트별로 `data/<list>_mask.txt`에 저장됩니다.

현재 저장소 상태:
- 현재 제공되는 모든 mask 파일은 `30`을 포함합니다(`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).

이전 README 버전에서 유지된 참고 사항(호환성 문맥 보존):
- `*_mask.txt`는 CIDR 마스크를 제어합니다(기본값 `32`, `default` 목록은 `24`).
- 보충 설명: 현재 체크인된 데이터와 스크립트 기본값 기준으로, 재정의하지 않으면 실제 런타임 기본값은 `30`입니다.

## 📤 출력

- GUI + CLI: `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- 정렬 도구: `output/domain_and_ips_unique_sorted.txt` 및 `.json`

## 🧪 예시

CLI 실행 예시:

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

일반적인 출력 형태:

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

사용자 지정 JSON 정규화 예시:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ 개발 노트

- 코드 스타일: Python 3, PEP 8, 4칸 들여쓰기, `snake_case` 네이밍.
- 스크립트는 의도적으로 CLI 친화적이며 대부분 단일 목적입니다.
- 현재 여러 `nslookup` 변형은 목록 키 매핑만 다르고 거의 동일한 로직을 공유합니다.
- 이 저장소에는 현재 자동화된 테스트가 없습니다.

## 🧯 문제 해결

- `Input file not found: domain_and_ips.txt`:
  - `code/unique_sort.py`에 `-i <input-file>`를 제공하거나 저장소 루트에 `domain_and_ips.txt`를 생성하세요.
- GUI가 자동으로 열리지 않을 때:
  - 시작 후 `http://127.0.0.1:5000`을 수동으로 여세요.
- 일부 도메인에서 DNS 결과가 비어 있을 때:
  - 네트워크/DNS 사용 가능 여부를 확인하세요. 조회 실패 도메인은 GUI의 `Failed Lookups`에 표시됩니다.
- 의존성 누락:
  - `pip install -r requirements.txt`를 실행하세요.
- OCR 도우미가 명령 누락으로 실패할 때:
  - `ffmpeg`와 `tesseract`를 설치하고 둘 다 `PATH`에 포함되었는지 확인하세요.

## 🗺️ 로드맵

- 파싱, 정렬, 조회 엣지 케이스에 대한 자동화 테스트 추가.
- 공유 파라미터형 실행기로 `nslookup` 변형 간 중복 로직 축소.
- `i18n/` 하위의 다국어 문서 확장.
- 린트 및 스모크 테스트용 선택적 CI 검사 추가.

## 🤝 기여

기여를 환영합니다.

권장 워크플로:
1. 변경용 브랜치를 생성합니다.
2. 커밋은 집중도 높게 유지하고 명령형으로 작성합니다(예: `Limit domain list to ChatGPT, Claude, and Google AI`).
3. 생성 데이터 동작을 변경할 때는 명령 출력 샘플을 포함합니다.
4. 간단한 요약과 의존성/런타임 참고사항을 포함해 PR을 엽니다.

## 📄 라이선스

현재 저장소 루트에는 명시적인 `LICENSE` 파일이 없습니다. 이 프로젝트를 재배포하거나 재사용할 계획이라면 먼저 라이선스 조건을 추가하거나 확인하세요.

## 💖 후원

후원 메타데이터는 `.github/FUNDING.yml`에서도 확인할 수 있습니다.

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- 프로젝트 링크: `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### 기부 QR (직접 후원하고 싶다면)

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 참고

- 데이터 파일은 한 줄당 하나의 항목을 사용합니다.
- `*_mask.txt`는 CIDR 마스크를 제어합니다(기본값 `32`, `default` 목록은 `24`).
- i18n 상태 참고: 이 저장소에는 `i18n/`이 존재하며, 로컬라이즈된 README 파일은 상단에 단일 언어 옵션 줄을 유지해야 합니다.
