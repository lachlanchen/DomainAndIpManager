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

Ein Python-Toolkit zur Pflege kuratierter Domain/IP/CIDR-Listen, zur deterministischen DNS-Auflösung, zum Entfernen von Duplikaten und zum Export reproduzierbarer Snapshots für Routing- und Filter-Workflows.

| Fokus | Details |
|---|---|
| Domainsätze | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Kernausrichtung | DNS-Auflösung, deterministisches Merging, Normalisierung, Export |
| Ausgabedateien | Zeitgestempelte TXT- und JSON-Snapshots in `output/` |
| Schnittstellen | CLI-Skripte + Flask-GUI (`code/gui_app.py`), lokal bereitgestellt |
| Datenformat | Zeilenbasierte Domain/IP/CIDR-Textdateien in `data/` |

---

## 🧭 Inhaltsverzeichnis

- [Überblick](#-überblick)
- [Funktionen](#-funktionen)
- [Projektstruktur](#-projektstruktur)
- [Voraussetzungen](#-voraussetzungen)
- [Installation](#-installation)
- [Verwendung](#-verwendung)
- [Konfiguration](#-konfiguration)
- [Skripte und Workflow-Map](#-skripte-und-workflow-map)
- [Beispiele](#-beispiele)
- [Entwicklungsnotizen](#-entwicklungsnotizen)
- [Fehlerbehebung](#-fehlerbehebung)
- [Roadmap](#-roadmap)
- [Mitwirken](#-mitwirken)
- [❤️ Support](#️-support)
- [Kontakt](#-kontakt)
- [Lizenz](#-lizenz)

## 🗂️ Kurzüberblick

| Bereich | Details |
|---|---|
| Domainsätze | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Kernabläufe | DNS-Auflösung + Mergen, Sortieren/De-Duplizieren, GUI-Bearbeitung, Snapshot-Export |
| Ausgabeformate | TXT + JSON |
| Primäres Ausgabeverzeichnis | `output/` |
| Haupteinstiegspunkte | CLI-Skripte unter `code/`, Flask-GUI in `gui_app.py` |

## 🚀 Übersicht

DomainAndIpManager ist für wiederholbare Listengenerierung ausgelegt:

- Halte getrennte kuratierte Listenmengen in `data/` (Domains + benutzerdefinierte IPs + CIDR + Mask-Dateien)
- Löse Domainnamen in IPs auf und konvertiere sie zu CIDR-Einträgen
- Führe aufgelöste Einträge mit benutzerdefinierten/kurierten Netzwerkblöcken zusammen
- Exportiere deterministische Artefakte (TXT + JSON) mit stabiler Sortierung und optionalen Zeitstempeln
- Starte per CLI oder öffne die Web-GUI für interaktive Bearbeitung und Neugenerierung

## ✨ Funktionen

| Bereich | Details |
|---|---|
| Multi-Listenprofile | Separate Domainsätze (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`) für strategie-spezifisches Routing |
| DNS-Auflösung | `code/nslookup*.py`-Skripte für Domain → IP-Block-Erweiterung |
| Sortierung / De-Duplizierung | `code/unique_sort*.py` normalisiert gemischte Domain/IP/CIDR-Daten |
| Deterministischer Export | Stabile TXT + JSON Ausgaben mit optionalen zeitgestempelten Snapshots |
| GUI-Bearbeitung | `gui/` für interaktive Bearbeitung von `domains`, `custom_ips`, `cidr` und Masken |
| Diagnose | Optionale Fehlerberichte für nicht aufgelöste Lookups |
| Optionales OCR-Werkzeug | `traffics/` Hilfsprogramme für YouTube/Video-Extraktions-Workflows |

---

## ✅ Voraussetzungen

| Anforderung | Hinweis |
|---|---|
| Python | 3.10+ (empfohlen) |
| Netzwerk | Internetzugang für DNS-Abfragen |
| Python-Pakete | `pip` und Abhängigkeiten aus `requirements.txt` |
| Git | Zum Klonen/Aktualisieren des Repositories benötigt |
| Optionaler OCR-Stack | `ffmpeg` + `tesseract`, falls die Traffic-Extraktions-Helfer genutzt werden |

---

## 📦 Installation

```bash
python3 -m pip install -r requirements.txt
```

Kurze Einrichtung:

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> Annahme: Für direkte CLI-Nutzung ist kein Virtual-Environment-Bootstrap zwingend erforderlich; `start_gui.sh` kann bei Bedarf automatisch eine `.venv` erstellen und verwenden.

## 🧭 Verwendung

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` startet `code/gui_app.py` und stellt bereit:

- URL: `http://127.0.0.1:5000`
- GUI-gestützte Bearbeitung der Listendateien
- Erzeugung auf Abruf und kopierfertige Vorschauen
- Automatische `.venv`-Erstellung sowie erforderliche Installationen/Updates bei Bedarf

Du kannst es auch direkt starten:

```bash
python3 code/gui_app.py
```

### CLI-Referenz

| Häufige Aufgabe | Befehl |
|---|---|
| AI-fokussierte Domains auflösen | `python3 code/nslookup_simplified.py` |
| GFW-fokussierte Domains auflösen | `python3 code/nslookup_simplified_gfw.py` |
| GFW + AI zusammengeführte Domains auflösen | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| GFW ohne AI auflösen | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| Basisauflösungs-Pfad starten | `python3 code/nslookup.py` |
| Listen in JSON sortiert und dedupliziert | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| Standard-TXT/JSON exportieren | `python3 code/unique_sort_print.py` |

Hinweise:

- Ausgabedateien erhalten Zeitstempel wie `output/<script>_YYYYMMDD_HHMMSS.txt`.
- Sortierskripte unterstützen benutzerdefinierte Ein- und Ausgabepfade über Flags.

### Optionales OCR-Werkzeug

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Erfordert `ffmpeg` und `tesseract` im `PATH`.

## ⚙️ Konfiguration

- Speichere je einen Eintrag pro Zeile in allen Textdateien in `data/`.
- Kommentarzeilen mit `#` werden in der aktuellen gemeinsamen Listennormalisierung ignoriert.
- Pro-Set-Masken liegen in `data/<set>_mask.txt`.
- Die im Repository enthaltenen Maskenwerte sind je nach Set hinterlegt und entsprechen den Dateien `data/*_mask.txt`.
- Vor dem Schreiben erfolgt eine deterministische Bereinigung, Sortierung und Deduplizierung.

### Set-Matrix

| Set | Domains-Datei | Custom-IP-Datei | CIDR-Datei | Mask-Datei |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## 🧰 Skript- und Workflow-Map

| Skript | Zweck |
|---|---|
| `code/nslookup.py` | Basisrunner für Domain/IP-Auflösung |
| `code/nslookup_simplified.py` | KI-fokussierte Auflösung + CIDR-Export |
| `code/nslookup_simplified_gfw.py` | GFW-fokussierte Auflösung |
| `code/nslookup_simplified_gfw_w_ai.py` | Zusammengelegte GFW + AI Auflösung |
| `code/nslookup_simplified_gfw_wo_ai.py` | GFW ohne AI-Auflösung |
| `code/unique_sort.py` | Normalisierung + Deduplizierung + JSON-Export |
| `code/unique_sort_print.py` | Druckt und schreibt standardisierte TXT/JSON-Artefakte |
| `code/list_utils.py` | Gemeinsame Loader-, Masken- und Listen-Helfer |
| `code/gui_app.py` | Flask-GUI Backend |
| `traffics/extract_youtube_traffic.py` | Optionaler OCR-Helfer für Traffic-Extraktion |
| `start_gui.sh` | Virtualenv-Bootstrap, Abhängigkeitsinstallation und Serverstart |

## 🗂️ Projektstruktur

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

## 🧾 Datendateien

Die Dateien in `data/` sind zeilenorientierte Textdateien:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

Dasselbe Namensschema gilt für `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw` und `default`.

## 🧪 Beispiele

Starte einen Resolver direkt:

```bash
python3 code/nslookup_simplified_gfw.py
```

Typische Ausgabenform:

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

Sortiere eine eigene Eingabedatei in JSON:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Entwicklungsnotizen

- Gemeinsame Lade- und Resolverhilfslogik liegt in `code/list_utils.py`.
- Writer nutzen deterministische Sortierung für reproduzierbare Artefakte.
- Das Repository enthält aktuell kein automatisiertes Test-Framework.
- Es gibt kein `setup.py` / `pyproject.toml`; dies ist ein skriptzentriertes Projekt.
- `.github/FUNDING.yml` und `figs/*`-Assets weisen auf integrierte Spenden/Funding-Optionen hin.

## 🧯 Fehlerbehebung

- `Input file not found: domain_and_ips.txt`
  - Führe `python3 code/unique_sort.py -i <path> -o <path>` mit gültigem Pfad aus oder stelle sicher, dass `domain_and_ips.txt` im Repository-Root liegt.
- DNS-Lookup-Timeouts oder -Fehler
  - Prüfe Netzwerkverbindung und DNS-Zugang, dann erneut versuchen.
- GUI startet nicht auf Port 5000
  - Prüfe, ob `flask` installiert ist, und ob bereits ein Prozess `127.0.0.1:5000` belegt.
- OCR-Utility-Fehler
  - Stelle sicher, dass `ffmpeg` und `tesseract` installiert sind und im `PATH` gefunden werden.

## 🗺️ Roadmap

- Unit-Tests für Parsing, Maskenlogik und Normalisierung hinzufügen.
- Eindeutige CLI-Hilfe für alle Skripte und gängigen Parameter ergänzen.
- Lock-Datei oder reproduzierbare Python-Umgebungsdefinition ergänzen.
- Export- und Vorschauhinweise in der GUI für fehlgeschlagene DNS-Lookups und Unterschiedsanzeigen beim Merge hinzufügen.

## 🤝 Mitwirken

Beiträge sind willkommen. Bevorzugter Ablauf:

1. Eröffne ein Issue mit Problem oder Feature-Anfrage.
2. Halte Änderungen fokussiert und reproduzierbar.
3. Dokumentiere erwartete Nutzung und Ausgabenänderungen in der PR-Beschreibung.
4. Aktualisiere `README.md`, wenn sich Verhalten oder Befehle ändern.

## ❤️ Support

<!-- support:start -->
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsors-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/lachlanchen)
[![LazyingArt Support](https://img.shields.io/badge/LazyingArt-Support-0EA5E9?style=for-the-badge)](https://chat.lazying.art/donate)
[![PayPal Support](https://img.shields.io/badge/PayPal-Support-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen)
[![Stripe Support](https://img.shields.io/badge/Stripe-Support-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400)
<!-- support:end -->

## 📬 Kontakt

- Öffne ein GitHub-Issue für Fehlerberichte und Featureanfragen.
- Gib in Issue-Beschreibungen bevorzugt eine kompakte Reproduktionsbeschreibung, erwartete Ausgabe und den Kommandokontext an.

## 📄 Lizenz

Es ist derzeit keine `LICENSE`-Datei im Repository-Root vorhanden.
