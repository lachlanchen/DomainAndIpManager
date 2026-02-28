[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

Verwalte Domain-/IP-Listen für AI- und GFW-Kontexte, führe DNS-Lookups aus und exportiere zeitgestempelte Ausgaben. Enthält CLI-Skripte und einen GUI-Editor.

## 🚀 Überblick

DomainAndIpManager ist ein Python-Toolkit für:
- Pflege mehrerer Listensätze (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).
- Auflösung von Domain-`A`-Records und Umwandlung in `IP/mask`-Einträge.
- Zusammenführung domainbasierter IPs mit benutzerdefinierten IP- und CIDR-Quellen.
- Export deterministischer, zeitgestempelter Ausgabedateien für nachgelagerte Netzwerk-/Routing-Workflows.

Es unterstützt beide Arbeitsweisen:
- CLI-Workflows in `code/nslookup*.py` und Sortier-Utilities.
- Eine Flask-basierte Web-GUI (`code/gui_app.py` + `gui/*`) zum Bearbeiten von Listen und interaktiven Ausführen von Lookups.

### Auf einen Blick

| Bereich | Was du bekommst |
|---|---|
| Listensätze | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Oberflächen | CLI-Skripte + Flask-GUI |
| Ausgabeformat | Zeitgestempelte Text-Snapshots + sortierte TXT/JSON |
| Primärer Workflow | Listen bearbeiten → Domains auflösen → benutzerdefinierte Bereiche kombinieren → exportieren |
| Optionaler Helfer | YouTube-Traffic-OCR-Extraktion unter `traffics/` |

## 🎬 Demo

![Domain & IP Manager demo](demos/demo.png)

## ✨ Funktionen

- Multi-Listenset-Workflow: `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`.
- GUI-Listeneditor mit Save/Load/Run/Copy-Workflow.
- Optionale Ein-/Ausblendung für Domains, benutzerdefinierte IPs und CIDR-Blöcke.
- Umschaltbarer Ausgabemodus: `Domains + IPs` oder `IPs only`.
- Reporting fehlgeschlagener Lookups in der GUI.
- Zeitgestempelte Ausgabe-Snapshots unter `output/`.
- Utility-Tools zum Deduplizieren und Sortieren gemischter Domain-/IP-Eingaben in TXT/JSON.
- Optionaler Traffic-OCR-Helfer unter `traffics/` (YouTube-orientierte Extraktion).

## 🗂️ Projektstruktur

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

## ✅ Voraussetzungen

- Python `3.10+` (empfohlen; der Code nutzt moderne Typsyntax).
- `pip`.
- Netzwerkverbindung für DNS-Abfragen.
- Optional für den OCR-Helfer: `ffmpeg`- und `tesseract`-Binärdateien in `PATH` verfügbar.

## 📦 Installation

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

Abhängigkeiten:

```bash
pip install -r requirements.txt
```

## 🖥️ Schnellstart (GUI)

```bash
./start_gui.sh
```

Öffne `http://127.0.0.1:5000`.

Hinweise:
- `start_gui.sh` bootstrapped `.venv`, installiert Abhängigkeiten bei Änderungen in `requirements.txt` und startet `code/gui_app.py`.
- Du kannst auch direkt mit `python3 code/gui_app.py` starten.

## 🧭 Nutzung

### GUI-Nutzung

1. Wähle einen Listensatz (`AI + GFW`, `AI`, `GFW`, `GFW (No AI)`, `Non-GFW (China)`, `Default`).
2. Bearbeite die Textbereiche `Domains`, `Custom IPs` und `CIDR`.
3. Setze `Mask` und den Ausgabemodus (`Domains + IPs` oder `IPs only`).
4. Klicke auf `Save`, um Änderungen in `data/*.txt` zu speichern.
5. Klicke auf `Run`, um aufzulösen und Ausgaben zu erzeugen.
6. Klicke auf `Copy`, um die aktuelle Ausgabe zu kopieren.

### CLI-Nutzung

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

Jedes Skript gibt Ergebnisse im Terminal aus und schreibt `output/<script>_YYYYMMDD_HHMMSS.txt`.

### Sortier- und Normalisierungs-Tools

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` unterstützt benutzerdefinierte Input-/Output-Flags und schreibt JSON.
- `unique_sort_print.py` gibt sortierte Domains/IPs aus und schreibt sowohl TXT als auch JSON nach `output/`.
- Falls `domain_and_ips.txt` im Repo-Root nicht existiert, verwende `-i <path>` mit `unique_sort.py` oder erstelle die Datei.

### Optionaler Traffic-Extraktions-Helfer

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Dieser Helfer erzeugt OCR-abgeleitete Domain/IP-Markdown-Reports in `traffics/` und benötigt externe Tools (`ffmpeg`, `tesseract`).

## 🧾 Datendateien

Listen sind zeilenbasiert und liegen unter `data/`:
- `ai_*` für reine AI-Listen
- `gfw_*` für GFW-Listen
- `ai_gfw_*` für kombinierte Listen
- `gfw_wo_ai_*` für GFW ohne AI
- `non_gfw_*` für in China erreichbare (nicht-GFW) Listen
- `default_*` für die Legacy-/Standardliste

Beispiel:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### Listensatz-Matrix

| Listensatz | Domains-Datei | Custom-IPs-Datei | CIDR-Datei | Mask-Datei |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ Konfiguration

- Ein Eintrag pro Zeile in jeder Listendatei.
- Zeilen, die mit `#` beginnen, werden von der gemeinsamen List-Loading-Logik als Kommentare behandelt und bei Lookup-Läufen ignoriert.
- Masks werden pro Listensatz in `data/<list>_mask.txt` gespeichert.

Aktueller Repository-Status:
- Alle mitgelieferten Mask-Dateien enthalten derzeit `30` (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).

Übernommener Hinweis aus früheren README-Versionen (für Kompatibilitätskontext beibehalten):
- `*_mask.txt` steuert die CIDR-Maske (Standard ist `32`, die `default`-Liste nutzt `24`).
- Klarstellung: In den aktuell eingecheckten Daten und Skript-Defaults sind die aktiven Laufzeit-Defaults `30`, sofern nicht überschrieben.

## 📤 Ausgaben

- GUI + CLI: `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- Sortier-Tools: `output/domain_and_ips_unique_sorted.txt` und `.json`

## 🧪 Beispiele

Beispielhafter CLI-Lauf:

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

Typische Ausgabestruktur:

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

Beispiel für benutzerdefinierte JSON-Normalisierung:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ Entwicklungshinweise

- Code-Stil: Python 3, PEP 8, 4 Leerzeichen Einrückung, `snake_case`-Benennung.
- Skripte sind bewusst CLI-freundlich und größtenteils Single-Purpose.
- Mehrere `nslookup`-Varianten teilen derzeit nahezu identische Logik mit unterschiedlichem List-Key-Mapping.
- In diesem Repository sind aktuell keine automatisierten Tests vorhanden.

## 🧯 Fehlerbehebung

- `Input file not found: domain_and_ips.txt`:
  - Übergib `-i <input-file>` an `code/unique_sort.py` oder erstelle `domain_and_ips.txt` im Repo-Root.
- GUI öffnet sich nicht automatisch:
  - Öffne `http://127.0.0.1:5000` nach dem Start manuell.
- DNS-Ergebnisse sind für manche Domains leer:
  - Prüfe Netzwerk-/DNS-Verfügbarkeit; nicht aufgelöste Domains stehen in der GUI unter `Failed Lookups`.
- Fehlende Abhängigkeiten:
  - Führe `pip install -r requirements.txt` aus.
- OCR-Helfer schlägt wegen fehlendem Befehl fehl:
  - Installiere `ffmpeg` und `tesseract` und stelle sicher, dass beide in `PATH` liegen.

## 🗺️ Roadmap

- Automatisierte Tests für Parsing, Sorting und Lookup-Edge-Cases hinzufügen.
- Doppelte Logik über `nslookup`-Varianten durch einen gemeinsamen parametrisierten Runner reduzieren.
- Mehrsprachige Doku unter `i18n/` erweitern.
- Optionale CI-Checks für Linting und Smoke-Tests hinzufügen.

## 🤝 Mitwirken

Beiträge sind willkommen.

Empfohlener Workflow:
1. Erstelle einen Branch für deine Änderung.
2. Halte Commits fokussiert und im Imperativ (zum Beispiel: `Limit domain list to ChatGPT, Claude, and Google AI`).
3. Füge Command-Output-Beispiele hinzu, wenn sich das Verhalten generierter Daten ändert.
4. Öffne einen PR mit kurzer Zusammenfassung und Hinweisen zu Abhängigkeiten/Laufzeit.

## 📄 Lizenz

Im Repository-Root ist derzeit keine explizite `LICENSE`-Datei vorhanden. Wenn du dieses Projekt weiterverteilen oder wiederverwenden willst, füge zuerst Lizenzbedingungen hinzu oder bestätige sie.

## 💖 Support

Funding-Metadaten sind auch in `.github/FUNDING.yml` verfügbar.

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- Projektlinks: `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### Spenden-QR (wenn du direkt unterstützen möchtest)

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 Hinweise

- Ein Eintrag pro Zeile in Datendateien.
- `*_mask.txt` steuert die CIDR-Maske (Standard ist `32`, die `default`-Liste nutzt `24`).
- i18n-Statushinweis: `i18n/` existiert in diesem Repository; lokalisierte README-Dateien sind geplant und sollen oben genau eine Sprachoptionszeile enthalten.
