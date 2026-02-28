[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

Gérez des listes de domaines/IP pour des contextes IA et GFW, exécutez des recherches DNS, et exportez des sorties horodatées. Inclut des scripts CLI et un éditeur GUI.

## 🚀 Vue d'ensemble

DomainAndIpManager est une boîte à outils Python pour :
- Maintenir plusieurs ensembles de listes (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).
- Résoudre les enregistrements `A` de domaines et les convertir en entrées `IP/mask`.
- Combiner les IP dérivées des domaines avec des sources d'IP personnalisées et de CIDR.
- Exporter des fichiers de sortie déterministes et horodatés pour des workflows réseau/routage en aval.

Il prend en charge :
- Des workflows CLI dans `code/nslookup*.py` et les utilitaires de tri.
- Une interface web GUI basée sur Flask (`code/gui_app.py` + `gui/*`) pour éditer les listes et lancer les recherches de manière interactive.

### En bref

| Zone | Ce que vous obtenez |
|---|---|
| Ensembles de listes | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Interfaces | Scripts CLI + GUI Flask |
| Type de sortie | Instantanés texte horodatés + TXT/JSON triés |
| Workflow principal | Éditer les listes → résoudre les domaines → combiner les plages personnalisées → exporter |
| Outil facultatif | Extraction OCR du trafic YouTube dans `traffics/` |

## 🎬 Démo

![Domain & IP Manager demo](demos/demo.png)

## ✨ Fonctionnalités

- Workflow multi-ensembles de listes : `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`.
- Éditeur de listes GUI avec workflow sauvegarder/charger/exécuter/copier.
- Contrôles d'inclusion facultatifs pour les domaines, IP personnalisées et blocs CIDR.
- Bascule de mode de sortie : `Domains + IPs` ou `IPs only`.
- Rapport des recherches échouées dans la GUI.
- Instantanés de sortie horodatés sous `output/`.
- Outils utilitaires pour dédupliquer et trier des entrées mixtes domaine/IP en TXT/JSON.
- Outil OCR de trafic facultatif sous `traffics/` (extraction orientée YouTube).

## 🗂️ Structure du projet

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

## ✅ Prérequis

- Python `3.10+` (recommandé ; le code utilise une syntaxe de type moderne).
- `pip`.
- Connectivité réseau pour les requêtes DNS.
- Facultatif pour l'outil OCR : binaires `ffmpeg` et `tesseract` disponibles dans `PATH`.

## 📦 Installation

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

Dépendances :

```bash
pip install -r requirements.txt
```

## 🖥️ Démarrage rapide (GUI)

```bash
./start_gui.sh
```

Ouvrez `http://127.0.0.1:5000`.

Remarques :
- `start_gui.sh` initialise `.venv`, installe les dépendances lorsque `requirements.txt` change, puis lance `code/gui_app.py`.
- Vous pouvez aussi lancer directement avec `python3 code/gui_app.py`.

## 🧭 Utilisation

### Utilisation de la GUI

1. Sélectionnez un ensemble de listes (`AI + GFW`, `AI`, `GFW`, `GFW (No AI)`, `Non-GFW (China)`, `Default`).
2. Éditez les zones de texte `Domains`, `Custom IPs` et `CIDR`.
3. Définissez `Mask` et le mode de sortie (`Domains + IPs` ou `IPs only`).
4. Cliquez sur `Save` pour enregistrer les changements dans `data/*.txt`.
5. Cliquez sur `Run` pour résoudre et générer la sortie.
6. Cliquez sur `Copy` pour copier la sortie actuelle.

### Utilisation en CLI

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

Chaque script affiche les résultats dans le terminal et écrit `output/<script>_YYYYMMDD_HHMMSS.txt`.

### Outils de tri et de normalisation

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` prend en charge des options personnalisées d'entrée/sortie et écrit du JSON.
- `unique_sort_print.py` affiche les domaines/IP triés et écrit à la fois du TXT et du JSON dans `output/`.
- Si `domain_and_ips.txt` n'existe pas à la racine du dépôt, utilisez `-i <path>` avec `unique_sort.py` ou créez le fichier.

### Outil auxiliaire facultatif d'extraction de trafic

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Cet outil génère des rapports markdown domaine/IP dérivés par OCR dans `traffics/` et nécessite des outils externes (`ffmpeg`, `tesseract`).

## 🧾 Fichiers de données

Les listes sont délimitées ligne par ligne et stockées sous `data/` :
- `ai_*` pour les listes IA uniquement
- `gfw_*` pour les listes GFW
- `ai_gfw_*` pour les listes combinées
- `gfw_wo_ai_*` pour GFW sans IA
- `non_gfw_*` pour les listes accessibles en Chine (non-GFW)
- `default_*` pour la liste legacy/par défaut

Exemple :

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### Matrice des ensembles de listes

| Ensemble de listes | Fichier domaines | Fichier IP personnalisées | Fichier CIDR | Fichier mask |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ Configuration

- Une entrée par ligne dans chaque fichier de liste.
- Les lignes commençant par `#` sont traitées comme des commentaires par la logique de chargement partagée et ignorées pendant les exécutions de lookup.
- Les masques sont stockés par ensemble de listes dans `data/<list>_mask.txt`.

État actuel du dépôt :
- Tous les fichiers de masque livrés contiennent actuellement `30` (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).

Note conservée depuis des versions antérieures du README (gardée pour contexte de compatibilité) :
- `*_mask.txt` contrôle le masque CIDR (par défaut `32`, la liste `default` utilise `24`).
- Clarification : dans les données versionnées actuelles et les valeurs par défaut des scripts, les valeurs actives à l'exécution sont `30` sauf remplacement.

## 📤 Sorties

- GUI + CLI : `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- Outils de tri : `output/domain_and_ips_unique_sorted.txt` et `.json`

## 🧪 Exemples

Exemple d'exécution CLI :

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

Forme de sortie typique :

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

Exemple de normalisation JSON personnalisée :

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ Notes de développement

- Style de code : Python 3, PEP 8, indentation de 4 espaces, noms en `snake_case`.
- Les scripts sont volontairement orientés CLI et pour la plupart mono-fonction.
- Plusieurs variantes `nslookup` partagent actuellement une logique quasi identique avec un mapping de clés de listes différent.
- Aucun test automatisé n'est actuellement présent dans ce dépôt.

## 🧯 Dépannage

- `Input file not found: domain_and_ips.txt` :
  - Fournissez `-i <input-file>` à `code/unique_sort.py` ou créez `domain_and_ips.txt` à la racine du dépôt.
- La GUI ne s'ouvre pas automatiquement :
  - Ouvrez `http://127.0.0.1:5000` manuellement après le démarrage.
- Les résultats DNS sont vides pour certains domaines :
  - Vérifiez la disponibilité du réseau/DNS ; les domaines non résolus sont listés dans `Failed Lookups` de la GUI.
- Dépendances manquantes :
  - Exécutez `pip install -r requirements.txt`.
- L'outil OCR échoue avec une commande manquante :
  - Installez `ffmpeg` et `tesseract` et assurez-vous qu'ils sont tous deux dans `PATH`.

## 🗺️ Feuille de route

- Ajouter des tests automatisés pour les cas limites de parsing, tri et lookup.
- Réduire la logique dupliquée entre les variantes `nslookup` via un exécuteur partagé paramétrable.
- Étendre la documentation multilingue sous `i18n/`.
- Ajouter des vérifications CI facultatives pour le linting et des smoke tests.

## 🤝 Contribution

Les contributions sont les bienvenues.

Workflow suggéré :
1. Créez une branche pour votre changement.
2. Gardez des commits ciblés et impératifs (par exemple : `Limit domain list to ChatGPT, Claude, and Google AI`).
3. Incluez des exemples de sortie de commandes quand vous modifiez le comportement des données générées.
4. Ouvrez une PR avec un bref résumé et toute note sur les dépendances/runtime.

## 📄 Licence

Aucun fichier `LICENSE` explicite n'est actuellement présent à la racine du dépôt. Si vous prévoyez de redistribuer ou réutiliser ce projet, ajoutez d'abord une licence ou confirmez ses conditions.

## 💖 Support

Les métadonnées de financement sont également disponibles dans `.github/FUNDING.yml`.

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- Liens du projet : `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### QR de don (si vous souhaitez soutenir directement)

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 Notes

- Une entrée par ligne dans les fichiers de données.
- `*_mask.txt` contrôle le masque CIDR (par défaut `32`, la liste `default` utilise `24`).
- Note de statut i18n : `i18n/` existe dans ce dépôt ; les README localisés sont prévus et doivent garder une seule ligne d'options de langue en haut.
