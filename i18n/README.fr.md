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

Un outil Python pour maintenir des jeux de listes de domaines/IP/CIDR, résoudre le DNS vers des blocs IP déterministes, supprimer les doublons et exporter des instantanés reproductibles pour les flux de routage et de filtrage.

| Axe | Détails |
|---|---|
| Jeux de domaines | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Flux principaux | Résolution DNS, fusion déterministe, normalisation, export |
| Artéfacts de sortie | TXT horodaté + instantanés JSON dans `output/` |
| Interfaces | Scripts CLI + GUI Flask (`code/gui_app.py`), servie localement |
| Format des données | Fichiers texte ligne par ligne de domaines/IP/CIDR dans `data/` |

---

## 🧭 Table des matières

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Structure du projet](#-structure-du-projet)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Configuration](#-configuration)
- [Scripts et carte des workflows](#-scripts-et-carte-des-workflows)
- [Exemples](#-exemples)
- [Notes de développement](#-notes-de-développement)
- [Dépannage](#-dépannage)
- [Feuille de route](#-feuille-de-route)
- [Contribution](#-contribution)
- [❤️ Support](#️-support)
- [Contact](#-contact)
- [Licence](#-licence)

## 🗂️ En bref

| Zone | Détails |
|---|---|
| Jeux de domaines | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Flux principaux | Résolution DNS + fusion, tri et dédoublonnage, édition GUI, export de snapshot |
| Formats de sortie | TXT + JSON |
| Répertoire de sortie principal | `output/` |
| Points d'entrée principaux | Scripts CLI dans `code/`, GUI Flask dans `gui_app.py` |

## 🚀 Aperçu

DomainAndIpManager est conçu pour la génération répétable de listes :

- Conserver des jeux de listes distincts dans `data/` (domaines + IP personnalisées + CIDR + fichiers mask)
- Résoudre des noms de domaine en IP et les convertir en entrées de type CIDR
- Fusionner les entrées résolues avec des blocs réseau personnalisés/curatés
- Exporter des artefacts déterministes (TXT + JSON) avec un ordre stable et des snapshots horodatés optionnels
- Exécuter via CLI ou lancer l’interface web pour éditer et regénérer de manière interactive

## ✨ Fonctionnalités

| Axe | Détails |
|---|---|
| Profils multi-listes | Jeux de listes séparés (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`) pour un routage par stratégie |
| Résolution DNS | Scripts `code/nslookup*.py` pour l’expansion domaine → blocs IP |
| Tri / dédoublonnage | `code/unique_sort*.py` normalise les domaines/IP/CIDR mixtes |
| Export déterministe | Ordonnancement stable TXT + JSON avec snapshots horodatés optionnels |
| Édition GUI | `gui/` pour éditer `domains`, `custom_ips`, `cidr` et les réglages de mask |
| Diagnostics | Signalement optionnel des résolutions échouées pour le dépannage |
| Utilitaire OCR optionnel | Aides `traffics/` pour les flux d’extraction YouTube/vidéo |

---

## ✅ Prérequis

| Exigence | Remarque |
|---|---|
| Python | 3.10+ (recommandé) |
| Réseau | Accès Internet pour les résolutions DNS |
| Packages Python | `pip` et dépendances définies dans `requirements.txt` |
| Git | Requis pour cloner/mettre à jour le dépôt |
| Stack OCR optionnelle | `ffmpeg` + `tesseract` lors de l’usage de l’outil d’extraction de trafic |

---

## 📦 Installation

```bash
python3 -m pip install -r requirements.txt
```

Installation rapide :

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> Hypothèse : aucun bootstrap de virtualenv n’est requis pour l’usage CLI direct ; `start_gui.sh` peut créer et utiliser `.venv` automatiquement si on le préfère.

## 🧭 Utilisation

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` lance `code/gui_app.py` et sert :

- URL : `http://127.0.0.1:5000`
- Édition basée sur l’interface des fichiers de liste
- Génération à la demande et aperçu des sorties prêts à copier
- Création automatique de `.venv` et installation/mise à jour des dépendances si nécessaire

Vous pouvez aussi lancer directement :

```bash
python3 code/gui_app.py
```

### Référence CLI

| Tâche courante | Commande |
|---|---|
| Résoudre les domaines orientés IA | `python3 code/nslookup_simplified.py` |
| Résoudre les domaines orientés GFW | `python3 code/nslookup_simplified_gfw.py` |
| Résoudre domaines GFW + IA fusionnés | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| Résoudre GFW sans IA | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| Chemin de résolution de base | `python3 code/nslookup.py` |
| Trier + dédoublonner en JSON | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| Exporter TXT/JSON canonique | `python3 code/unique_sort_print.py` |

Remarques :

- Les fichiers de sortie sont écrits avec un suffixe horodaté comme `output/<script>_YYYYMMDD_HHMMSS.txt`.
- Les scripts de tri acceptent des chemins d’entrée/sortie personnalisés via des options.

### Utilitaire OCR optionnel

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Nécessite `ffmpeg` et `tesseract` dans le `PATH`.

## ⚙️ Configuration

- Une entrée par ligne dans tous les fichiers texte de `data/`.
- Les lignes de commentaire `#` sont ignorées par la logique actuelle du chargeur de listes.
- Les masques par liste sont stockés dans `data/<set>_mask.txt`.
- Les valeurs de masks présentes dans le dépôt actuel sont propres au dépôt et reflétées par le contenu de `data/*_mask.txt`.
- Les entrées sont normalisées en sortie triée et dédupliquée avant écriture.

### Matrice des jeux de listes

| Jeu | Fichier domaines | Fichier IP personnalisées | Fichier CIDR | Fichier mask |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## 🧰 Carte des scripts et workflow

| Script | Objectif |
|---|---|
| `code/nslookup.py` | Exécuteur de résolution de base domaine/IP |
| `code/nslookup_simplified.py` | Résolution orientée IA + export CIDR |
| `code/nslookup_simplified_gfw.py` | Résolution orientée GFW |
| `code/nslookup_simplified_gfw_w_ai.py` | Résolution fusionnée GFW + IA |
| `code/nslookup_simplified_gfw_wo_ai.py` | Résolution GFW sans IA |
| `code/unique_sort.py` | Normaliser + dédupliquer + sortie JSON |
| `code/unique_sort_print.py` | Afficher + écrire les artefacts TXT/JSON canoniques |
| `code/list_utils.py` | Chargeurs, masks et utilitaires partagés |
| `code/gui_app.py` | Backend Flask de la GUI |
| `traffics/extract_youtube_traffic.py` | Utilitaire OCR optionnel pour extraction de trafic |
| `start_gui.sh` | Bootstrap venv + installation dépendances + démarrage serveur |

## 🗂️ Structure du projet

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

## 🎬 Démo

![Domain & IP Manager demo](demos/demo.png)

## 🧾 Fichiers de données

Les fichiers de données sont des textes à une ligne par entrée dans `data/` :

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

Le même motif de nommage s’applique à `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw` et `default`.

## 🧪 Exemples

Exécuter directement un résolveur :

```bash
python3 code/nslookup_simplified_gfw.py
```

Exemple de sortie typique :

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

Trier un fichier personnalisé vers JSON :

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Notes de développement

- La logique partagée de chargement et de résolution se trouve dans `code/list_utils.py`.
- Les writers de sortie utilisent un ordonnancement déterministe pour des artefacts reproductibles.
- Le dépôt ne contient actuellement pas de framework de tests automatisés.
- Aucun `setup.py` / `pyproject.toml` n’est présent ; c’est un projet basé scripts.
- `.github/FUNDING.yml` et `figs/*` indiquent une intégration donation/soutien.

## 🧯 Dépannage

- `Input file not found: domain_and_ips.txt`
  - Lancez `python3 code/unique_sort.py -i <chemin> -o <chemin>` avec un chemin valide, ou assurez-vous que `domain_and_ips.txt` existe à la racine du dépôt.
- Délai d’attente ou échecs de résolution DNS
  - Vérifiez la connectivité réseau et l’accès DNS, puis relancez.
- La GUI ne démarre pas sur le port 5000
  - Vérifiez que `flask` est installé et qu’aucun autre processus n’utilise déjà `127.0.0.1:5000`.
- Erreurs de l’utilitaire OCR
  - Vérifiez que `ffmpeg` et `tesseract` sont installés et accessibles via `PATH`.

## 🗺️ Feuille de route

- Ajouter des tests unitaires pour le parsing, l’application des masks et les utilitaires de normalisation.
- Ajouter une aide CLI (`--help`) claire pour tous les scripts et options courantes.
- Fournir un lockfile ou un environnement reproductible pour les dépendances Python.
- Ajouter dans la GUI des indicateurs de prévisualisation pour les échecs DNS et les diff de sortie fusionnée.

## 🤝 Contribution

Les contributions sont les bienvenues. Flux de travail recommandé :

1. Ouvrir une issue décrivant le problème ou la demande de fonctionnalité.
2. Garder les changements ciblés et reproductibles.
3. Documenter l’usage attendu des commandes et les changements de sortie dans la description de votre PR.
4. Mettre à jour `README.md` quand le comportement ou les commandes évoluent.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Contact

- Ouvrez une issue GitHub pour les rapports de bugs et les demandes de fonctionnalités.
- Préférez des étapes de reproduction courtes, une sortie attendue et le contexte des commandes dans vos rapports d’issue.

## 📄 License

Aucun fichier `LICENSE` n’est actuellement présent à la racine du dépôt dans cet extrait.
