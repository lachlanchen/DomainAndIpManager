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

Набор Python-инструментов для поддержания курируемых наборов доменов/IP/CIDR, детерминированного разрешения DNS в IP-блоки, удаления дубликатов и экспорта воспроизводимых снапшотов для рабочих процессов маршрутизации и фильтрации.

| Направление | Детали |
|---|---|
| Наборы доменов | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Основные процессы | Разрешение DNS, детерминированное объединение, нормализация, экспорт |
| Выходные артефакты | TXT с временными метками и JSON-снимки в `output/` |
| Интерфейсы | CLI-скрипты + Flask GUI (`code/gui_app.py`), локальный запуск |
| Формат данных | Текстовые файлы по строкам с доменами/IP/CIDR в `data/` |

---

## 🧭 Оглавление

- [Обзор](#-обзор)
- [Функции](#-функции)
- [Структура проекта](#-структура-проекта)
- [Предварительные требования](#-предварительные-требования)
- [Установка](#-установка)
- [Использование](#-использование)
- [Настройка](#-настройка)
- [Карта скриптов и workflow](#-карта-скриптов-и-workflow)
- [Примеры](#-примеры)
- [Заметки по разработке](#-заметки-по-разработке)
- [Устранение неполадок](#-устранение-неполадок)
- [Дорожная карта](#-дорожная-карта)
- [Участие в разработке](#-участие-в-разработке)
- [❤️ Support](#️-support)
- [Контакты](#-контакты)
- [Лицензия](#-лицензия)

## 🗂️ Краткий обзор

| Область | Детали |
|---|---|
| Наборы доменов | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Основные процессы | Разрешение DNS + объединение, дедупликация/сортировка, редактирование в GUI, экспорт снапшотов |
| Форматы вывода | TXT + JSON |
| Основной каталог вывода | `output/` |
| Основные точки входа | CLI-скрипты в `code/`, Flask GUI в `gui_app.py` |

## 🚀 Обзор

DomainAndIpManager предназначен для повторяемой генерации списков:

- Храните отдельные курируемые наборы в `data/` (домены + пользовательские IP + CIDR + файлы масок)
- Разрешайте доменные имена в IP и конвертируйте в CIDR-записи
- Объединяйте разрешённые записи с пользовательскими/курируемыми сетевыми блоками
- Экспортируйте детерминированные артефакты (TXT + JSON) со стабильным порядком и необязательными снапшотами с отметкой времени
- Запускайтесь через CLI или открывайте веб-GUI для интерактивного редактирования и регенерации

## ✨ Функции

| Область | Детали |
|---|---|
| Несколько профилей списков | Отдельные наборы (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`) для маршрутизации под конкретную стратегию |
| DNS-разрешение | Скрипты `code/nslookup*.py` для раскрытия доменов в IP-блоки |
| Сортировка / дедупликация | `code/unique_sort*.py` обрабатывает смешанные домены/IP/CIDR и нормализует их |
| Детерминированный экспорт | Стабильный порядок TXT + JSON и опциональные снапшоты с временной меткой |
| Редактирование в GUI | `gui/` для работы с `domains`, `custom_ips`, `cidr` и настройками масок |
| Диагностика | Опциональные отчёты по неудачным DNS-запросам для поиска проблем |
| Дополнительный OCR-инструмент | Утилиты из `traffics/` для рабочих процессов извлечения из YouTube/видео |

---

## ✅ Предварительные требования

| Требование | Комментарий |
|---|---|
| Python | 3.10+ (рекомендуется) |
| Сеть | Доступ к Интернету для DNS-запросов |
| Пакеты Python | `pip` и зависимости из `requirements.txt` |
| Git | Нужен для клонирования/обновления репозитория |
| Дополнительный OCR-стек | `ffmpeg` + `tesseract` для утилиты извлечения трафика |

---

## 📦 Установка

```bash
python3 -m pip install -r requirements.txt
```

Короткая настройка:

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> Предположение: для прямого CLI-использования дополнительная инициализация virtualenv не обязательна; `start_gui.sh` при необходимости сам создаст и использует `.venv`.

## 🧭 Использование

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` запускает `code/gui_app.py` и предоставляет:

- URL: `http://127.0.0.1:5000`
- Редактирование файлов списков через GUI
- Генерация по запросу и предпросмотры вывода, готового к копированию
- Автоматическое создание `.venv` и установка/обновление зависимостей при необходимости

Можно запустить напрямую:

```bash
python3 code/gui_app.py
```

### Справочник CLI

| Типовая задача | Команда |
|---|---|
| Разрешить домены, ориентированные на AI | `python3 code/nslookup_simplified.py` |
| Разрешить домены для GFW | `python3 code/nslookup_simplified_gfw.py` |
| Разрешить объединённые домены GFW + AI | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| Разрешить GFW без AI | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| Запустить базовый путь разрешения | `python3 code/nslookup.py` |
| Сортировать и дедуплицировать списки в JSON | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| Экспортировать канонический TXT/JSON | `python3 code/unique_sort_print.py` |

Примечания:

- Выходные файлы пишутся с суффиксом временной метки вида `output/<script>_YYYYMMDD_HHMMSS.txt`.
- Скрипты сортировки поддерживают пользовательские пути входа/выхода через флаги.

### Опциональная OCR-утилита

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Требуются `ffmpeg` и `tesseract`, доступные через `PATH`.

## ⚙️ Настройка

- Храните по одной записи на строку во всех текстовых файлах `data/`.
- Комментарии `#` игнорируются в текущей общей логике загрузки списков.
- Маски по наборам хранятся в `data/<set>_mask.txt`.
- Текущие сохранённые значения масок зависят от файлов `data/*_mask.txt` в репозитории.
- Перед записью входные данные переводятся в детерминированный порядок без дублей.

### Матрица наборов

| Набор | Файл доменов | Файл пользовательских IP | Файл CIDR | Файл маски |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## 🧰 Карта скриптов и workflow

| Скрипт | Назначение |
|---|---|
| `code/nslookup.py` | Базовый процесс разрешения доменов/IP |
| `code/nslookup_simplified.py` | Разрешение, ориентированное на AI, + экспорт CIDR |
| `code/nslookup_simplified_gfw.py` | Разрешение, ориентированное на GFW |
| `code/nslookup_simplified_gfw_w_ai.py` | Объединённое разрешение GFW + AI |
| `code/nslookup_simplified_gfw_wo_ai.py` | Разрешение GFW без AI |
| `code/unique_sort.py` | Нормализация + дедупликация + вывод JSON |
| `code/unique_sort_print.py` | Печать и запись стандартных TXT/JSON артефактов |
| `code/list_utils.py` | Общие загрузчики, маски и вспомогательные функции списков |
| `code/gui_app.py` | Flask GUI backend |
| `traffics/extract_youtube_traffic.py` | Дополнительная OCR-помощь для извлечения данных трафика |
| `start_gui.sh` | Инициализация virtualenv, установка зависимостей и запуск сервера |

## 🗂️ Структура проекта

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

## 🎬 Демонстрация

![Domain & IP Manager demo](demos/demo.png)

## 🧾 Файлы данных

Файлы данных — обычный текст построчно в `data/`:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

Та же схема именования применяется к `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw` и `default`.

## 🧪 Примеры

Запускать один resolver напрямую:

```bash
python3 code/nslookup_simplified_gfw.py
```

Обычный формат вывода:

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

Отсортировать пользовательский входной файл в JSON:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Заметки по разработке

- Общая логика загрузки и разрешения находится в `code/list_utils.py`.
- Выходные функции используют детерминированный порядок для воспроизводимых артефактов.
- В репозитории пока нет автоматизированного фреймворка тестирования.
- В репозитории отсутствуют `setup.py` / `pyproject.toml`; это проект скриптового типа.
- `.github/FUNDING.yml` и файлы `figs/*` указывают на настройки донатов/поддержки проекта.

## 🧯 Устранение неполадок

- `Input file not found: domain_and_ips.txt`
  - Запустите `python3 code/unique_sort.py -i <path> -o <path>` с корректным входным путём или убедитесь, что `domain_and_ips.txt` существует в корне репозитория.
- Таймауты или сбои DNS
  - Проверьте сетевое подключение и доступность DNS, затем повторите попытку.
- GUI не запускается на порту 5000
  - Убедитесь, что установлен `flask` и на `127.0.0.1:5000` нет другого процесса.
- Ошибки OCR-утилиты
  - Проверьте, что `ffmpeg` и `tesseract` установлены и доступны через `PATH`.

## 🗺️ Дорожная карта

- Добавить unit-тесты для разбора, применения масок и нормализации.
- Добавить понятную справку CLI для всех скриптов и основных флагов.
- Добавить lock-file или воспроизводимое описание Python-среды.
- Добавить в GUI индикаторы экспорта/предпросмотра неуспешных DNS-запросов и диффов объединённого результата.

## 🤝 Участие в разработке

Добро пожаловать к участию. Рекомендуемый рабочий процесс:

1. Откройте issue с описанием проблемы или запроса на фичу.
2. Держите изменения точечными и воспроизводимыми.
3. Документируйте ожидаемый формат запуска команд и изменений вывода в описании PR.
4. Обновляйте `README.md`, если меняется поведение или команды.

## ❤️ Support

<!-- support:start -->
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsors-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/lachlanchen)
[![LazyingArt Support](https://img.shields.io/badge/LazyingArt-Support-0EA5E9?style=for-the-badge)](https://chat.lazying.art/donate)
[![PayPal Support](https://img.shields.io/badge/PayPal-Support-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen)
[![Stripe Support](https://img.shields.io/badge/Stripe-Support-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400)
<!-- support:end -->

## 📬 Контакты

- Откройте issue на GitHub для багов и запросов новых возможностей.
- В отчетах об ошибках лучше указывать пошаговую репродукцию, ожидаемый вывод и контекст выполняемой команды.

## 📄 Лицензия

В текущем снимке репозитория файл `LICENSE` в корне не отслеживается.
