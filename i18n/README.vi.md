[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Mode](https://img.shields.io/badge/Mode-CLI%20%2F%20GUI-1f6feb)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Locale](https://img.shields.io/badge/Docs-English%20%7C%209%20More-0ea5e9?logo=googletranslate&logoColor=white)
![License](https://img.shields.io/badge/License-Not%20Included-9ca3af)

Bộ công cụ Python dùng để duy trì các tập danh sách domain/IP/CIDR đã được tuyển chọn, giải mã DNS thành các khối IP xác định, loại bỏ trùng lặp và xuất bản snapshot có thể tái tạo cho các quy trình định tuyến và lọc.

| Tập trung | Chi tiết |
|---|---|
| Tập danh sách domain | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Quy trình chính | Giải mã DNS, gộp dữ liệu có thứ tự xác định, chuẩn hóa, xuất kết quả |
| Dữ liệu đầu ra | TXT có dấu thời gian và JSON trong `output/` |
| Giao diện | Script CLI + Flask GUI (`code/gui_app.py`, chạy local) |
| Định dạng dữ liệu | Tệp văn bản domain/IP/CIDR theo từng dòng trong `data/` |

---

## 🧭 Mục lục

- [Tổng quan](#-tổng-quan)
- [Tính năng](#-tính-năng)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
- [Cách sử dụng](#-cách-sử-dụng)
- [Cấu hình](#-cấu-hình)
- [Sơ đồ luồng script](#-sơ-đồ-luồng-script)
- [Ví dụ](#-ví-dụ)
- [Ghi chú phát triển](#-ghi-chú-phát-triển)
- [Xử lý lỗi](#-xử-lý-lỗi)
- [Lộ trình](#-lộ-trình)
- [Đóng góp](#-đóng-góp)
- [Support](#️-support)
- [Liên hệ](#-liên-hệ)
- [Giấy phép](#-giấy-phép)

## 🗂️ Tình hình nhanh

| Khu vực | Chi tiết |
|---|---|
| Tập domain | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Quy trình chính | Giải mã DNS + gộp, loại trùng, GUI chỉnh sửa, xuất snapshot |
| Định dạng đầu ra | TXT + JSON |
| Thư mục xuất chính | `output/` |
| Điểm vào chính | Script CLI trong `code/`, Flask GUI tại `gui_app.py` |

## 🚀 Tổng quan

DomainAndIpManager được thiết kế cho việc tạo danh sách có thể lặp lại:

- Giữ các tập list riêng trong `data/` (domain + custom IP + CIDR + mask)
- Giải mã tên miền sang IP và chuyển thành dạng CIDR
- Gộp các mục đã giải mã với các khối mạng tùy chỉnh/đã chọn lọc
- Xuất artifact có tính xác định (TXT + JSON) theo thứ tự ổn định và snapshot có thời gian tùy chọn
- Chạy qua CLI hoặc mở GUI web để chỉnh sửa tương tác và tạo lại nhanh

## ✨ Tính năng

| Khu vực | Chi tiết |
|---|---|
| Hồ sơ đa danh sách | Các list riêng (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`) cho chiến lược định tuyến theo nhu cầu |
| Giải mã DNS | Các script `code/nslookup*.py` cho mở rộng domain → IP block |
| Sắp xếp / loại bỏ trùng lặp | `code/unique_sort*.py` xử lý chuẩn hóa domain/IP/CIDR kết hợp |
| Xuất có tính xác định | Sắp xếp output TXT + JSON ổn định, kèm snapshot có dấu thời gian khi cần |
| Chỉnh sửa qua GUI | `gui/` cho chỉnh sửa tương tác `domains`, `custom_ips`, `cidr` và cài đặt mask |
| Chẩn đoán | Báo cáo lookup thất bại (tùy chọn) để hỗ trợ troubleshooting |
| Tiện ích OCR tùy chọn | `traffics/` hỗ trợ trích xuất luồng YouTube/video |

---

## ✅ Yêu cầu

| Yêu cầu | Ghi chú |
|---|---|
| Python | 3.10+ (khuyến nghị) |
| Mạng | Có kết nối Internet để tra cứu DNS |
| Gói Python | `pip` và phụ thuộc trong `requirements.txt` |
| Git | Cần thiết để clone/cập nhật repository |
| Stack OCR tùy chọn | `ffmpeg` + `tesseract` khi dùng tiện ích trích xuất traffic |

---

## 📦 Cài đặt

```bash
python3 -m pip install -r requirements.txt
```

Thiết lập nhanh:

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> Giả định: Không cần bootstrap môi trường ảo cho việc dùng CLI trực tiếp; `start_gui.sh` vẫn có thể tạo và dùng `.venv` tự động khi cần.

## 🧭 Cách sử dụng

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` sẽ khởi chạy `code/gui_app.py` và phục vụ:

- URL: `http://127.0.0.1:5000`
- Chỉnh sửa danh sách tệp bằng GUI
- Tạo mới theo yêu cầu và xem trước output sẵn sàng copy
- Tự động tạo `.venv` và cài/cập nhật phụ thuộc khi cần

Bạn cũng có thể chạy trực tiếp:

```bash
python3 code/gui_app.py
```

### Tham chiếu CLI

| Công việc thường gặp | Lệnh |
|---|---|
| Resolve các domain tập trung AI | `python3 code/nslookup_simplified.py` |
| Resolve các domain cho GFW | `python3 code/nslookup_simplified_gfw.py` |
| Resolve AI + GFW đã gộp | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| Resolve GFW trừ AI | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| Resolve đường dẫn resolver cơ bản | `python3 code/nslookup.py` |
| Sắp xếp + loại trùng list thành JSON | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| Xuất TXT/JSON chuẩn hóa | `python3 code/unique_sort_print.py` |

Lưu ý:

- Các file output sẽ có đuôi timestamp như `output/<script>_YYYYMMDD_HHMMSS.txt`.
- Script sort hỗ trợ tùy chỉnh input/output qua flags.

### Tiện ích OCR tùy chọn

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Cần có `ffmpeg` và `tesseract` trong `PATH`.

## ⚙️ Cấu hình

- Mỗi hàng chỉ chứa một mục trong toàn bộ tệp văn bản `data/`.
- Dòng bắt đầu bằng `#` được bỏ qua trong logic loader danh sách chung hiện tại.
- Mask riêng cho từng list được lưu trong `data/<set>_mask.txt`.
- Giá trị mask đã commit hiện tại là theo nội dung từng `data/*_mask.txt` của repository.
- Input sẽ được quy về output đã loại trùng có thứ tự xác định trước khi ghi.

### Ma trận các list set

| List set | Tệp Domains | Tệp custom IP | Tệp CIDR | Tệp mask |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## 🧰 Sơ đồ script & workflow

| Script | Mục đích |
|---|---|
| `code/nslookup.py` | Runner giải mã domain/IP cơ bản |
| `code/nslookup_simplified.py` | Giải mã ưu tiên AI + xuất CIDR |
| `code/nslookup_simplified_gfw.py` | Giải mã tập trung GFW |
| `code/nslookup_simplified_gfw_w_ai.py` | Gộp kết quả GFW + AI |
| `code/nslookup_simplified_gfw_wo_ai.py` | Giải mã GFW loại trừ AI |
| `code/unique_sort.py` | Chuẩn hóa + loại trùng + output JSON |
| `code/unique_sort_print.py` | In + ghi artifact TXT/JSON chuẩn |
| `code/list_utils.py` | Loader chung, xử lý mask và helper list |
| `code/gui_app.py` | Backend Flask GUI |
| `traffics/extract_youtube_traffic.py` | Tiện ích OCR tuỳ chọn cho trích xuất traffic |
| `start_gui.sh` | Tạo virtualenv + cài phụ thuộc + khởi động server |

## 🗂️ Cấu trúc dự án

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

## 🧾 Tệp dữ liệu

Các tệp dữ liệu là văn bản plain-text mỗi dòng một mục trong `data/`:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

Cùng một quy tắc đặt tên áp dụng cho `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw` và `default`.

## 🧪 Ví dụ

Chạy trực tiếp một resolver:

```bash
python3 code/nslookup_simplified_gfw.py
```

Định dạng output điển hình:

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

Sắp xếp một file input tùy chỉnh thành JSON:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Ghi chú phát triển

- Logic loader và resolver dùng chung nằm trong `code/list_utils.py`.
- Bộ xuất dữ liệu dùng thứ tự ổn định để tạo artifact có thể tái tạo.
- Repository hiện chưa có framework test tự động.
- Chưa có `setup.py` / `pyproject.toml`; đây là dự án kiểu script-first.
- `.github/FUNDING.yml` và tài nguyên `figs/*` cho thấy dữ liệu tích hợp donate/funding.

## 🧯 Xử lý lỗi

- `Input file not found: domain_and_ips.txt`
  - Chạy `python3 code/unique_sort.py -i <path> -o <path>` với đường dẫn input hợp lệ, hoặc đảm bảo `domain_and_ips.txt` tồn tại ở root repository.
- Hết thời gian hoặc DNS lookup lỗi
  - Kiểm tra kết nối mạng và quyền truy cập DNS, sau đó thử lại.
- GUI không khởi động được trên cổng 5000
  - Kiểm tra `flask` đã cài và không có tiến trình nào chiếm `127.0.0.1:5000`.
- Lỗi tiện ích OCR
  - Kiểm tra `ffmpeg` và `tesseract` đã cài và có thể gọi từ `PATH`.

## 🗺️ Lộ trình

- Thêm unit test cho phân tích cú pháp, áp dụng mask và hàm chuẩn hóa.
- Thêm mô tả CLI help rõ ràng cho tất cả script và flag phổ biến.
- Cung cấp file lock/reproducible env để khóa phụ thuộc Python.
- Hiển thị thêm indicator xuất/preview trong GUI cho DNS lookup lỗi và chênh lệch output sau gộp.

## 🤝 Đóng góp

Đóng góp luôn được chào đón. Quy trình ưu tiên:

1. Mở một issue mô tả lỗi hoặc yêu cầu tính năng.
2. Giữ thay đổi có trọng tâm và có thể tái tạo.
3. Ghi rõ cách dùng lệnh và thay đổi output trong mô tả PR.
4. Cập nhật `README.md` khi hành vi/lệnh thay đổi.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Liên hệ

- Mở issue trên GitHub cho báo cáo bug và đề xuất tính năng.
- Ưu tiên cung cấp quy trình reproduce ngắn gọn, kết quả mong đợi và ngữ cảnh lệnh.

## 📄 Giấy phép

Hiện tại chưa có file `LICENSE` nào đang được theo dõi tại root repository trong snapshot này.
