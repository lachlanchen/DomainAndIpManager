[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# DomainAndIpManager

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask&logoColor=white)
![dnspython](https://img.shields.io/badge/dnspython-2.4%2B-2A6DB0)
![Platform](https://img.shields.io/badge/Platform-CLI%20%2B%20GUI-0A7B83)
![Status](https://img.shields.io/badge/Project-Active-2ea44f)
![Data](https://img.shields.io/badge/Data%20Sets-6-orange)

Administra listas de dominios/IP para contextos de IA y GFW, ejecuta búsquedas DNS y exporta salidas con marca de tiempo. Incluye scripts CLI y un editor GUI.

## 🚀 Resumen

DomainAndIpManager es un toolkit en Python para:
- Mantener múltiples conjuntos de listas (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).
- Resolver registros `A` de dominios y convertirlos en entradas `IP/mask`.
- Combinar IP derivadas de dominios con fuentes personalizadas de IP y CIDR.
- Exportar archivos de salida deterministas y con marca de tiempo para flujos de red/enrutamiento posteriores.

Soporta ambos modos:
- Flujos CLI en `code/nslookup*.py` y utilidades de ordenación.
- Una GUI web basada en Flask (`code/gui_app.py` + `gui/*`) para editar listas y ejecutar búsquedas de forma interactiva.

### Vista rápida

| Área | Lo que obtienes |
|---|---|
| Conjuntos de listas | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Interfaces | Scripts CLI + GUI Flask |
| Estilo de salida | Snapshots de texto con timestamp + TXT/JSON ordenados |
| Flujo principal | Editar listas → resolver dominios → combinar rangos personalizados → exportar |
| Ayudante opcional | Extracción OCR de tráfico de YouTube en `traffics/` |

## 🎬 Demostración

![Domain & IP Manager demo](demos/demo.png)

## ✨ Características

- Flujo con múltiples conjuntos de listas: `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`.
- Editor de listas en GUI con flujo de guardar/cargar/ejecutar/copiar.
- Controles opcionales de inclusión para dominios, IP personalizadas y bloques CIDR.
- Selector de modo de salida: `Domains + IPs` o `IPs only`.
- Reporte de búsquedas fallidas en la GUI.
- Snapshots de salida con timestamp en `output/`.
- Herramientas para eliminar duplicados y ordenar entradas mixtas dominio/IP a TXT/JSON.
- Ayudante OCR opcional en `traffics/` (enfocado en YouTube).

## 🗂️ Estructura del proyecto

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

## ✅ Requisitos previos

- Python `3.10+` (recomendado; el código usa sintaxis de tipos moderna).
- `pip`.
- Conectividad de red para consultas DNS.
- Opcional para el ayudante OCR: binarios `ffmpeg` y `tesseract` disponibles en `PATH`.

## 📦 Instalación

```bash
git clone <your-fork-or-this-repo-url>
cd DomainAndIpManager
pip install -r requirements.txt
```

Dependencias:

```bash
pip install -r requirements.txt
```

## 🖥️ Inicio rápido (GUI)

```bash
./start_gui.sh
```

Abre `http://127.0.0.1:5000`.

Notas:
- `start_gui.sh` prepara `.venv`, instala dependencias cuando cambia `requirements.txt` e inicia `code/gui_app.py`.
- También puedes ejecutarlo directamente con `python3 code/gui_app.py`.

## 🧭 Uso

### Uso de la GUI

1. Selecciona un conjunto de listas (`AI + GFW`, `AI`, `GFW`, `GFW (No AI)`, `Non-GFW (China)`, `Default`).
2. Edita las áreas de texto `Domains`, `Custom IPs` y `CIDR`.
3. Define `Mask` y el modo de salida (`Domains + IPs` o `IPs only`).
4. Haz clic en `Save` para persistir cambios en `data/*.txt`.
5. Haz clic en `Run` para resolver y generar salida.
6. Haz clic en `Copy` para copiar la salida actual.

### Uso por CLI

```bash
python3 code/nslookup_simplified.py
python3 code/nslookup_simplified_gfw.py
python3 code/nslookup_simplified_gfw_w_ai.py
python3 code/nslookup_simplified_gfw_wo_ai.py
python3 code/nslookup.py
```

Cada script imprime resultados en la terminal y escribe `output/<script>_YYYYMMDD_HHMMSS.txt`.

### Herramientas de ordenación y normalización

```bash
python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json
python3 code/unique_sort_print.py
```

- `unique_sort.py` soporta flags personalizadas de entrada/salida y escribe JSON.
- `unique_sort_print.py` imprime dominios/IP ordenados y escribe TXT y JSON en `output/`.
- Si `domain_and_ips.txt` no existe en la raíz del repositorio, usa `-i <path>` con `unique_sort.py` o crea el archivo.

### Ayudante opcional de extracción de tráfico

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Este ayudante genera reportes markdown de dominios/IP derivados por OCR en `traffics/` y requiere herramientas externas (`ffmpeg`, `tesseract`).

## 🧾 Archivos de datos

Las listas son de una entrada por línea y se guardan en `data/`:
- `ai_*` para listas solo de IA
- `gfw_*` para listas GFW
- `ai_gfw_*` para listas combinadas
- `gfw_wo_ai_*` para GFW sin IA
- `non_gfw_*` para listas accesibles desde China (no-GFW)
- `default_*` para la lista heredada/predeterminada

Ejemplo:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

### Matriz de conjuntos de listas

| List set | Domains file | Custom IPs file | CIDR file | Mask file |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## ⚙️ Configuración

- Una entrada por línea en cada archivo de lista.
- Las líneas que empiezan por `#` se tratan como comentarios por la lógica compartida de carga de listas y se ignoran durante las ejecuciones.
- Las máscaras se guardan por conjunto de listas en `data/<list>_mask.txt`.

Estado actual del repositorio:
- Todos los archivos de máscara incluidos actualmente contienen `30` (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`).

Nota preservada de versiones anteriores del README (mantenida por compatibilidad):
- `*_mask.txt` controla la máscara CIDR (el valor predeterminado es `32`, la lista `default` usa `24`).
- Aclaración: en los datos actualmente versionados y en los valores por defecto de scripts, los predeterminados activos en ejecución son `30` salvo que se sobrescriban.

## 📤 Salidas

- GUI + CLI: `output/<script or gui>_YYYYMMDD_HHMMSS.txt`
- Herramientas de ordenación: `output/domain_and_ips_unique_sorted.txt` y `.json`

## 🧪 Ejemplos

Ejemplo de ejecución CLI:

```bash
python3 code/nslookup_simplified_gfw_w_ai.py
```

Forma típica de la salida:

```text
<domain.example>
<resolved-ip>/30
<custom-ip>/30
<cidr-block>
```

Ejemplo de normalización JSON personalizada:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🛠️ Notas de desarrollo

- Estilo de código: Python 3, PEP 8, indentación de 4 espacios, nombres `snake_case`.
- Los scripts son intencionalmente amigables para CLI y en su mayoría de propósito único.
- Varias versiones de `nslookup` comparten actualmente una lógica casi idéntica con diferentes mapeos de claves de lista.
- Actualmente no hay pruebas automatizadas en este repositorio.

## 🧯 Solución de problemas

- `Input file not found: domain_and_ips.txt`:
  - Proporciona `-i <input-file>` a `code/unique_sort.py` o crea `domain_and_ips.txt` en la raíz del repositorio.
- La GUI no se abre automáticamente:
  - Abre `http://127.0.0.1:5000` manualmente después del inicio.
- Resultados DNS vacíos para algunos dominios:
  - Verifica disponibilidad de red/DNS; los dominios no resueltos se listan en `Failed Lookups` de la GUI.
- Faltan dependencias:
  - Ejecuta `pip install -r requirements.txt`.
- El ayudante OCR falla por comando faltante:
  - Instala `ffmpeg` y `tesseract` y asegúrate de que ambos estén en `PATH`.

## 🗺️ Hoja de ruta

- Agregar pruebas automatizadas para casos límite de parsing, ordenación y lookup.
- Reducir lógica duplicada entre variantes de `nslookup` mediante un ejecutor compartido parametrizado.
- Ampliar la documentación multilingüe en `i18n/`.
- Agregar verificaciones CI opcionales para linting y smoke tests.

## 🤝 Contribuciones

Las contribuciones son bienvenidas.

Flujo sugerido:
1. Crea una rama para tu cambio.
2. Mantén los commits enfocados y en modo imperativo (por ejemplo: `Limit domain list to ChatGPT, Claude, and Google AI`).
3. Incluye ejemplos de salida de comandos al cambiar el comportamiento de datos generados.
4. Abre un PR con un breve resumen y notas sobre dependencias/runtime.

## 📄 Licencia

Actualmente no hay un archivo `LICENSE` explícito en la raíz del repositorio. Si planeas redistribuir o reutilizar este proyecto, agrega o confirma primero los términos de licencia.

## 💖 Soporte

Los metadatos de financiación también están disponibles en `.github/FUNDING.yml`.

- GitHub Sponsors: `https://github.com/sponsors/lachlanchen`
- Enlaces del proyecto: `https://lazying.art`, `https://chat.lazying.art`, `https://onlyideas.art`

### QR de donación (si quieres apoyar directamente)

| WeChat | Alipay |
|---|---|
| ![WeChat donation QR](figs/donate_wechat.png) | ![Alipay donation QR](figs/donate_alipay.png) |

## 📝 Notas

- Una entrada por línea en archivos de datos.
- `*_mask.txt` controla la máscara CIDR (el valor predeterminado es `32`, la lista `default` usa `24`).
- Nota de estado de i18n: `i18n/` existe en este repositorio; los README localizados están planificados y deben mantener una sola línea de opciones de idioma en la parte superior.
