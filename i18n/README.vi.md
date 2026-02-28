[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

Quản lý danh sách domain/IP cho ngữ cảnh AI và GFW, chạy truy vấn DNS, và xuất kết quả có đóng dấu thời gian. Bao gồm script CLI và trình GUI chỉnh sửa.

## 🚀 Tổng quan

DomainAndIpManager là bộ công cụ Python dùng để:
- Duy trì nhiều bộ danh sách (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).
- Phân giải bản ghi `A` của domain và chuyển thành mục `IP/mask`.
- Kết hợp IP lấy từ domain với nguồn IP tùy chỉnh và CIDR.
- Xuất tệp đầu ra có timestamp, ổn định để dùng cho các quy trình mạng/định tuyến phía sau.

Hỗ trợ cả:
- Luồng CLI trong `code/nslookup*.py` và các tiện ích sắp xếp.
- GUI web dựa trên Flask (`code/gui_app.py` + `gui/*`) để chỉnh sửa danh sách và chạy lookup tương tác.

### Tóm tắt nhanh

| Khu vực | Bạn nhận được |
|---|---|
| Bộ danh sách | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Giao diện | Script CLI + Flask GUI |
| Kiểu đầu ra | Ảnh chụp văn bản có timestamp + TXT/JSON đã sắp xếp |
| Luồng chính | Chỉnh danh sách → phân giải domain → kết hợp dải tùy chỉnh → xuất |
| Trợ giúp tùy chọn | Trích xuất OCR lưu lượng YouTube trong `traffics/` |

## 🎬 Demo

![Domain & IP Manager demo](demos/demo.png)

## ✨ Tính năng

- Luồng làm việc đa bộ danh sách: `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`.
- GUI chỉnh sửa danh sách với luồng lưu/tải/chạy/sao chép.
- Điều khiển bật/tắt để bao gồm domains, custom IPs và CIDR blocks.
- Chuyển chế độ đầu ra: `Domains + IPs` hoặc `IPs only`.
- Báo cáo tra cứu thất bại trong GUI.
- Ảnh chụp đầu ra có timestamp dưới `output/`.
- Công cụ tiện ích để khử trùng lặp và sắp xếp dữ liệu domain/IP hỗn hợp sang TXT/JSON.
- Trợ giúp OCR lưu lượng tùy chọn dưới `traffics/` (ưu tiên YouTube).

## 🗂️ Cấu trúc dự án

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

## ✅ Yêu cầu trước khi chạy

- Python `3.10+` (khuyến nghị; mã nguồn dùng cú pháp kiểu hiện đại).
- `pip`.
- Kết nối mạng cho truy vấn DNS.
- Tùy chọn cho OCR helper: có sẵn binary `ffmpeg` và `tesseract` trong `PATH`.

## 📦 Cài đặt

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

Phụ thuộc:

```bash
pip install -r requirements.txt
```

## 🖥️ Bắt đầu nhanh (GUI)

```bash
./start_gui.sh
```

Mở `http://127.0.0.1:5000`.

Lưu ý:
- `start_gui.sh` sẽ khởi tạo `.venv`, cài phụ thuộc khi `requirements.txt` thay đổi, và chạy `code/gui_app.py`.
- Bạn cũng có thể chạy trực tiếp bằng `python3 code/gui_app.py`.

## 🧭 Cách dùng

### Dùng GUI

1. Chọn bộ danh sách (`AI + GFW`, `AI`, `GFW`, `GFW (No AI)`, `Non-GFW (China)`, `Default`).
2. Chỉnh các vùng văn bản `Domains`, `Custom IPs`, và `CIDR`.
3. Đặt `Mask` và chế độ đầu ra (`Domains + IPs` hoặc `IPs only`).
4. Nhấn `Save` để lưu thay đổi vào `data/*.txt`.
5. Nhấn `Run` để phân giải và tạo đầu ra.
6. Nhấn `Copy` để sao chép đầu ra hiện tại.

### Dùng CLI

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

Mỗi script sẽ in kết quả ra terminal và ghi `output/<script>_YYYYMMDD_HHMMSS.txt`.

### Công cụ sắp xếp & chuẩn hóa

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` hỗ trợ cờ input/output tùy chỉnh và ghi JSON.
- `unique_sort_print.py` in domain/IP đã sắp xếp và ghi cả TXT lẫn JSON vào `output/`.
- Nếu `domain_and_ips.txt` không tồn tại ở thư mục gốc repo, dùng `-i <path>` với `unique_sort.py` hoặc tạo tệp đó.

### Trợ giúp trích xuất lưu lượng (tùy chọn)

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Trợ giúp này tạo báo cáo markdown domain/IP từ OCR trong `traffics/` và yêu cầu công cụ ngoài (`ffmpeg`, `tesseract`).

## 🧾 Tệp dữ liệu

Danh sách được lưu mỗi dòng một mục dưới `data/`:
- `ai_*` cho danh sách chỉ AI
- `gfw_*` cho danh sách GFW
- `ai_gfw_*` cho danh sách kết hợp
- `gfw_wo_ai_*` cho GFW không gồm AI
- `non_gfw_*` cho danh sách có thể truy cập từ Trung Quốc (không bị GFW)
- `default_*` cho danh sách legacy/mặc định

Ví dụ:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### Ma trận bộ danh sách

| List set | Domains file | Custom IPs file | CIDR file | Mask file |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ Cấu hình

- Mỗi tệp danh sách một mục trên mỗi dòng.
- Dòng bắt đầu bằng `#` được logic nạp danh sách chung coi là comment và bỏ qua khi chạy lookup.
- Mask được lưu theo từng bộ danh sách trong `data/<list>_mask.txt`.

Trạng thái hiện tại của repo:
- Tất cả tệp mask hiện có đều chứa `30` (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).

Ghi chú được giữ lại từ các phiên bản README cũ hơn (để tương thích ngữ cảnh):
- `*_mask.txt` kiểm soát CIDR mask (mặc định là `32`, danh sách `default` dùng `24`).
- Làm rõ: trong dữ liệu đã commit hiện tại và mặc định script, mặc định runtime đang hoạt động là `30` nếu không ghi đè.

## 📤 Đầu ra

- GUI + CLI: `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- Công cụ sắp xếp: `output/domain_and_ips_unique_sorted.txt` và `.json`

## 🧪 Ví dụ

Ví dụ chạy CLI:

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

Dạng đầu ra điển hình:

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

Ví dụ chuẩn hóa JSON tùy chỉnh:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ Ghi chú phát triển

- Chuẩn mã: Python 3, PEP 8, thụt lề 4 khoảng trắng, đặt tên `snake_case`.
- Các script được thiết kế ưu tiên CLI và phần lớn làm một nhiệm vụ cụ thể.
- Nhiều biến thể `nslookup` hiện chia sẻ logic gần giống nhau nhưng ánh xạ list-key khác nhau.
- Hiện chưa có kiểm thử tự động trong repo này.

## 🧯 Khắc phục sự cố

- `Input file not found: domain_and_ips.txt`:
  - Cung cấp `-i <input-file>` cho `code/unique_sort.py` hoặc tạo `domain_and_ips.txt` ở thư mục gốc repo.
- GUI không tự mở:
  - Mở thủ công `http://127.0.0.1:5000` sau khi khởi chạy.
- Kết quả DNS trống với một số domain:
  - Kiểm tra kết nối mạng/DNS; các domain không phân giải được sẽ nằm trong `Failed Lookups` của GUI.
- Thiếu phụ thuộc:
  - Chạy `pip install -r requirements.txt`.
- OCR helper lỗi thiếu lệnh:
  - Cài `ffmpeg` và `tesseract`, đảm bảo cả hai có trong `PATH`.

## 🗺️ Lộ trình

- Thêm kiểm thử tự động cho các trường hợp biên của parsing, sorting và lookup.
- Giảm logic trùng lặp giữa các biến thể `nslookup` bằng runner tham số hóa dùng chung.
- Mở rộng tài liệu đa ngôn ngữ dưới `i18n/`.
- Thêm kiểm tra CI tùy chọn cho linting và smoke test.

## 🤝 Đóng góp

Rất hoan nghênh đóng góp.

Quy trình đề xuất:
1. Tạo một nhánh cho thay đổi của bạn.
2. Giữ commit tập trung, ở dạng mệnh lệnh (ví dụ: `Limit domain list to ChatGPT, Claude, and Google AI`).
3. Đính kèm mẫu output lệnh khi thay đổi hành vi dữ liệu sinh ra.
4. Mở PR với tóm tắt ngắn cùng ghi chú về phụ thuộc/runtime nếu có.

## 📄 Giấy phép

Hiện chưa có tệp `LICENSE` rõ ràng ở thư mục gốc repo. Nếu bạn dự định phân phối lại hoặc tái sử dụng dự án này, hãy thêm hoặc xác nhận điều khoản giấy phép trước.

## 💖 Hỗ trợ

Metadata tài trợ cũng có trong `.github/FUNDING.yml`.

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- Liên kết dự án: `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### Mã QR quyên góp (nếu bạn muốn hỗ trợ trực tiếp)

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 Ghi chú

- Một mục trên mỗi dòng trong các tệp dữ liệu.
- `*_mask.txt` kiểm soát CIDR mask (mặc định là `32`, danh sách `default` dùng `24`).
- Ghi chú trạng thái i18n: `i18n/` có trong repo này; các README bản địa hóa được lên kế hoạch và nên giữ một dòng tùy chọn ngôn ngữ ở đầu.
