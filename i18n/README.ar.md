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

أداة Python لإدارة مجموعات النطاقات/IP/CIDR المختارة، وتحويل أسماء النطاقات إلى نطاقات IP حتمية، وإزالة التكرارات، وتصدير لقطات قابلة لإعادة الإنتاج لاستخدامها في سير عمل التوجيه والتصفية.

| المجال | التفاصيل |
|---|---|
| مجموعات النطاق | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| سير العمل الأساسي | حل DNS، دمج حتمي، التطبيع، التصدير |
| مخرجات العمل | ملفات TXT مع طابع زمني ونسخ JSON داخل `output/` |
| الواجهات | سكربتات CLI + واجهة Flask GUI محلية (`code/gui_app.py`) |
| صيغة البيانات | ملفات نصية سطرية للنطاقات/IP/CIDR داخل `data/` |

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
- [Support](#-support)
- [Contact](#-contact)
- [License](#-license)

## 🗂️ At a Glance

| المجال | التفاصيل |
|---|---|
| مجموعات النطاق | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| سير العمل الأساسي | حل DNS + دمج، إزالة التكرارات/الفرز، تحرير عبر GUI، تصدير لحظي |
| صيغ المخرجات | TXT + JSON |
| دليل الإخراج الرئيسي | `output/` |
| نقاط الدخول الأساسية | سكربتات CLI داخل `code/` وواجهة Flask في `code/gui_app.py` |

## 🚀 Overview

تم تصميم DomainAndIpManager لتوليد القوائم بطريقة قابلة للتكرار:

- احتفظ بمجموعات قائمة منفصلة داخل `data/` (النطاقات + عناوين IP المخصصة + CIDR + ملفات القناع)
- حل أسماء النطاقات إلى IPs وتحويلها إلى صيغة CIDR
- دمج السجلات المحلولة مع الكتل المخصصة/المنسقة يدويًا
- تصدير مخرجات حتمية (TXT + JSON) بترتيب ثابت ولقطات زمنية اختيارية
- التشغيل عبر CLI أو تشغيل واجهة الويب للتعديل التفاعلي وإعادة التوليد

## ✨ Features

| المجال | التفاصيل |
|---|---|
| ملفات متعددة القوائم | مجموعات منفصلة (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`) لاستراتيجيات توجيه متخصصة |
| حل DNS | سكربتات `code/nslookup*.py` لتمديد النطاقات إلى كتل IP |
| فرز / إزالة التكرار | `code/unique_sort*.py` يتعامل مع مزيج من النطاقات/IP/CIDR مع التطبيع |
| التصدير الحتمي | ترتيب ثابت لمخرجات TXT + JSON مع لقطات زمنية اختيارية |
| تحرير عبر الواجهة | `gui/` لتحرير `domains` و`custom_ips` و`cidr` وإعدادات القناع |
| التشخيص | تقارير فشل الاختبار لحل DNS متاحة لحل المشكلات |
| أداة OCR اختيارية | أدوات `traffics/` لتدفقات استخراج YouTube/الفيديو |

---

## ✅ Prerequisites

| المتطلب | الملاحظات |
|---|---|
| Python | 3.10+ (موصى به) |
| الشبكة | اتصال إنترنت لعمليات DNS |
| حزم Python | `pip` والاعتماديات من `requirements.txt` |
| Git | مطلوب لاستنساخ/تحديث المستودع |
| OCR stack اختياري | `ffmpeg` + `tesseract` عند استخدام أداة استخراج الحركة المرورية |

---

## 📦 Installation

```bash
python3 -m pip install -r requirements.txt
```

إعداد سريع:

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> افتراض: لا يلزم تحميل virtualenv مسبقًا للاستخدام المباشر للـ CLI؛ يمكن لـ `start_gui.sh` إنشاء `.venv` واستخدامه تلقائيًا عند الحاجة.

## 🧭 Usage

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` يشغّل `code/gui_app.py` ويعرض:

- الرابط: `http://127.0.0.1:5000`
- تحرير ملفات القوائم عبر الواجهة
- توليد ومعاينة مخرجات جاهزة للنسخ عند الطلب
- إنشاء `.venv` تلقائيًا وتثبيت/تحديث المتطلبات عند اللزوم

يمكنك أيضًا تشغيلها مباشرةً:

```bash
python3 code/gui_app.py
```

### CLI Reference

| المهمة الشائعة | الأمر |
|---|---|
| حل النطاقات المركزة على الذكاء الاصطناعي | `python3 code/nslookup_simplified.py` |
| حل النطاقات المركزة على GFW | `python3 code/nslookup_simplified_gfw.py` |
| حل النطاقات المدمجة GFW + AI | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| حل نطاقات GFW دون AI | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| تشغيل مسار الحل الأساسي | `python3 code/nslookup.py` |
| فرز القوائم وإزالة التكرارات إلى JSON | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| تصدير TXT/JSON القياسية | `python3 code/unique_sort_print.py` |

ملاحظات:

- تُكتب الملفات المخرجة بلاحقة زمنية مثل `output/<script>_YYYYMMDD_HHMMSS.txt`.
- سكربتات الفرز تدعم مسارات إدخال/إخراج مخصصة عبر خيارات سطر الأوامر.

### Optional OCR Utility

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

تتطلب وجود `ffmpeg` و`tesseract` في `PATH`.

## ⚙️ Configuration

- احتفظ بسطر واحد لكل إدخال في جميع ملفات `data/` النصية.
- تُهمل أسطر التعليقات التي تبدأ بـ `#` في منطق التحميل المشترك الحالي للقوائم.
- تُخزن الأقنعة لكل قائمة في `data/<set>_mask.txt`.
- قيم الأقنعة المتضمنة حالياً مرتبطة بالمستودع وتعكس محتوى ملفات `data/*_mask.txt`.
- يُجرى التطبيع والترتيب الحتمي وإزالة التكرارات قبل الكتابة النهائية.

### List Set Matrix

| مجموعة القائمة | ملف النطاقات | ملف IP المخصص | ملف CIDR | ملف القناع |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## 🧰 Script & Workflow Map

| السكربت | الغرض |
|---|---|
| `code/nslookup.py` | مِشغِّل حل النطاقات/IP الأساسي |
| `code/nslookup_simplified.py` | حل مخصص للذكاء الاصطناعي + تصدير CIDR |
| `code/nslookup_simplified_gfw.py` | حل موجه لـ GFW |
| `code/nslookup_simplified_gfw_w_ai.py` | حل مدمج لـ GFW + AI |
| `code/nslookup_simplified_gfw_wo_ai.py` | حل GFW بدون AI |
| `code/unique_sort.py` | تطبيع + إزالة تكرار + إخراج JSON |
| `code/unique_sort_print.py` | طباعة + كتابة مخرجات TXT/JSON القياسية |
| `code/list_utils.py` | أدوات التحميل والمقنعة ومساعدات القوائم المشتركة |
| `code/gui_app.py` | خلفية Flask للواجهة الرسومية |
| `traffics/extract_youtube_traffic.py` | أداة OCR اختيارية لاستخراج الحركة المرورية | 
| `start_gui.sh` | إعداد virtualenv + تثبيت الاعتماديات + تشغيل الخادم |

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

ملفات البيانات نصية سطرية في `data/`:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

وينطبق نفس نمط التسمية على `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, و`default`.

## 🧪 Examples

تشغيل أحد أدوات الحل مباشرة:

```bash
python3 code/nslookup_simplified_gfw.py
```

نمط الإخراج الشائع:

```text
domain.example.com
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

فرز ملف إدخال مخصص إلى JSON:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Development Notes

- توجد منطق التحميل وحل النطاقات المشترك في `code/list_utils.py`.
- يستخدم مُنتجو المخرجات ترتيبًا حتميًا لضمان إمكانية إعادة إنتاج النتائج.
- لا يوجد حالياً إطار اختبارات تلقائي في المستودع.
- لا يوجد `setup.py` / `pyproject.toml`; هذا مشروع قائم على السكربتات.
- ملفات `.github/FUNDING.yml` و`figs/*` تدل على تكامل التبرعات/الدعم.

## 🧯 Troubleshooting

- `Input file not found: domain_and_ips.txt`
  - شغّل `python3 code/unique_sort.py -i <path> -o <path>` باستخدام مسار صحيح، أو تأكد من وجود `domain_and_ips.txt` في جذر المستودع.
- فشل أو انقطاع في استعلامات DNS
  - تحقّق من اتصال الشبكة وإتاحة DNS ثم أعد المحاولة.
- فشل GUI في البدء على المنفذ 5000
  - تأكد من تثبيت `flask` ولا يوجد عملية أخرى تستخدم `127.0.0.1:5000`.
- أخطاء أداة OCR
  - تأكد من تثبيت `ffmpeg` و`tesseract` وأنهما متاحان في `PATH`.

## 🗺️ Roadmap

- إضافة اختبارات وحدة لتجزئة التحليل، وتطبيق الأقنعة، ومنطق التطبيع.
- إضافة توثيق أوامر واضح لكل سكربت وخياراته الشائعة.
- توفير lockfile أو تعريف بيئة قابل لإعادة الإنتاج لمتطلبات Python.
- إضافة مؤشرات معاينة/تصغير في GUI للفشل في DNS والفروقات في الناتج المدمج.

## 🤝 Contributing

المساهمات مرحب بها. مسار العمل المفضل:

1. افتح Issue يصف المشكلة أو طلب الميزة.
2. أبقِ التغييرات مركزة وقابلة للتكرار.
3. وثّق أوامر الاستخدام والنتائج المتوقعة في وصف PR.
4. حدّث `README.md` عند تغير السلوك/الأوامر.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Contact

- افتح Issue على GitHub لإبلاغ الأخطاء وطلبات الميزات.
- في تقارير الأخطاء، قدّم خطوات إعادة الإنتاج المختصرة ونتيجة متوقعة وسياق الأوامر.

## 📄 License

لا يوجد ملف `LICENSE` مُدرج حاليًا في جذر المستودع ضمن هذه النسخة.
