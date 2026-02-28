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

Un kit de herramientas en Python para mantener conjuntos curados de dominios/IP/CIDR, resolver DNS a bloques IP deterministas, eliminar duplicados y exportar instantáneas reproducibles para flujos de enrutamiento y filtrado.

| Enfoque | Detalles |
|---|---|
| Conjuntos de dominio | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Flujos principales | Resolución DNS, fusión determinista, normalización, exportación |
| Artefactos de salida | TXT con marca temporal y JSON en `output/` |
| Interfaces | Scripts CLI + GUI de Flask (`code/gui_app.py`, servido localmente) |
| Formato de datos | Archivos de texto por línea con dominios/IP/CIDR en `data/` |

---

## 🧭 Tabla de contenido

- [Resumen rápido](#-resumen-rapido)
- [Visión general](#-vision-general)
- [Características](#-caracteristicas)
- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalacion)
- [Uso](#-uso)
- [Configuración](#-configuracion)
- [Mapa de scripts y flujo](#-mapa-de-scripts-y-flujo)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Demostración](#-demostracion)
- [Archivos de datos](#-archivos-de-datos)
- [Ejemplos](#-ejemplos)
- [Notas de desarrollo](#-notas-de-desarrollo)
- [Solución de problemas](#-solucion-de-problemas)
- [Hoja de ruta](#-hoja-de-ruta)
- [Contribución](#-contribucion)
- [Support](#️-support)
- [Contacto](#-contacto)
- [Licencia](#-licencia)

## 🗂️ Resumen rapido

| Area | Detalles |
|---|---|
| Conjuntos de dominio | `ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default` |
| Flujo principal | Resolución DNS + fusión, deduplicación/ordenación, edición por GUI y exportación de instantáneas |
| Formatos de salida | TXT + JSON |
| Directorio principal de salida | `output/` |
| Puntos de entrada principales | Scripts CLI en `code/`, GUI Flask en `gui_app.py` |

## 🚀 Vision general

DomainAndIpManager está diseñado para generar listas de forma repetible:

- Mantiene conjuntos de listas separados en `data/` (dominios + IPs personalizadas + CIDR + archivos de máscara)
- Resuelve nombres de dominio a IP y convierte a entradas tipo CIDR
- Fusiona entradas resueltas con bloques de red personalizados/curados
- Exporta artefactos deterministas (TXT + JSON) con orden estable y, opcionalmente, instantáneas con marca temporal
- Ejecuta desde CLI o inicia la GUI web para edición interactiva y regeneración

## ✨ Caracteristicas

| Area | Detalles |
|---|---|
| Perfiles multi-lista | Conjuntos separados de listas (`ai`, `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw`, `default`) para enrutamiento por estrategia |
| Resolución DNS | Scripts `code/nslookup*.py` para expansión dominio → bloque IP |
| Ordenado / desduplicación | `code/unique_sort*.py` gestiona normalización de dominios/IP/CIDR mixtos |
| Exportación determinista | Orden de salida TXT + JSON estable, con instantáneas opcionales y marca temporal |
| Edición por GUI | `gui/` para edición interactiva de `domains`, `custom_ips`, `cidr` y ajustes de máscara |
| Diagnóstico | Informes opcionales de resoluciones fallidas para depuración |
| Utilidad OCR opcional | Utilidades en `traffics/` para flujos de extracción de YouTube/video |

---

## ✅ Requisitos previos

| Requisito | Notas |
|---|---|
| Python | 3.10+ (recomendado) |
| Red | Acceso a Internet para consultas DNS |
| Paquetes de Python | `pip` y dependencias de `requirements.txt` |
| Git | Requerido para clonar/actualizar el repositorio |
| Stack OCR opcional | `ffmpeg` + `tesseract` al usar la utilidad de extracción de tráfico |

---

## 📦 Instalacion

```bash
python3 -m pip install -r requirements.txt
```

Configuración rápida:

```bash
git clone <tu-fork-o-url-de-este-repo>
cd DomainAndIpManager
python3 -m pip install -r requirements.txt
```

> Suposición: no es necesaria una inicialización explícita de entorno virtual para uso directo de CLI; `start_gui.sh` aún puede crear y usar `.venv` automáticamente si se prefiere.

## 🧭 Uso

### GUI

```bash
./start_gui.sh
```

`start_gui.sh` inicia `code/gui_app.py` y expone:

- URL: `http://127.0.0.1:5000`
- Edición respaldada por GUI para archivos de listas
- Generación bajo demanda y vista previa de salida lista para copiar
- Creación automática de `.venv` e instalación/actualización de dependencias cuando hace falta

También puedes ejecutarlo directamente:

```bash
python3 code/gui_app.py
```

### Referencia de CLI

| Tarea común | Comando |
|---|---|
| Resolver dominios con enfoque AI | `python3 code/nslookup_simplified.py` |
| Resolver dominios con enfoque GFW | `python3 code/nslookup_simplified_gfw.py` |
| Resolver dominios GFW + AI fusionados | `python3 code/nslookup_simplified_gfw_w_ai.py` |
| Resolver dominios GFW sin AI | `python3 code/nslookup_simplified_gfw_wo_ai.py` |
| Resolver ruta de resolución base | `python3 code/nslookup.py` |
| Ordenar y deduplicar listas en JSON | `python3 code/unique_sort.py -i domain_and_ips.txt -o output/domain_and_ips_unique_sorted.json` |
| Exportar TXT/JSON canónico | `python3 code/unique_sort_print.py` |

Notas:

- Los archivos de salida se escriben con sufijos de marca temporal como `output/<script>_YYYYMMDD_HHMMSS.txt`.
- Los scripts de ordenado admiten rutas de entrada/salida personalizadas mediante banderas.

### Utilidad OCR opcional

```bash
python3 traffics/extract_youtube_traffic.py \
  --videos "traffics/ScreenRecording_02-03-2026 07-34-48_1.MP4" \
           "traffics/ScreenRecording_02-03-2026 07-36-29_1.MP4"
```

Requiere `ffmpeg` y `tesseract` en `PATH`.

## ⚙️ Configuracion

- Mantén una entrada por línea en todos los archivos de `data/`.
- Las líneas de comentario con `#` se ignoran en la lógica compartida actual del cargador de listas.
- Las máscaras por lista se almacenan en `data/<set>_mask.txt`.
- Los valores de máscara actuales del repositorio están reflejados en los contenidos de `data/*_mask.txt`.
- La entrada se normaliza en un orden deduplicado determinista antes de escribirse.

### Matriz de conjuntos de lista

| Conjunto | Archivo de dominios | Archivo de IPs personalizadas | Archivo CIDR | Archivo de máscara |
|---|---|---|---|---|
| `ai` | `data/ai_domains.txt` | `data/ai_custom_ips.txt` | `data/ai_cidr.txt` | `data/ai_mask.txt` |
| `gfw` | `data/gfw_domains.txt` | `data/gfw_custom_ips.txt` | `data/gfw_cidr.txt` | `data/gfw_mask.txt` |
| `ai_gfw` | `data/ai_gfw_domains.txt` | `data/ai_gfw_custom_ips.txt` | `data/ai_gfw_cidr.txt` | `data/ai_gfw_mask.txt` |
| `gfw_wo_ai` | `data/gfw_wo_ai_domains.txt` | `data/gfw_wo_ai_custom_ips.txt` | `data/gfw_wo_ai_cidr.txt` | `data/gfw_wo_ai_mask.txt` |
| `non_gfw` | `data/non_gfw_domains.txt` | `data/non_gfw_custom_ips.txt` | `data/non_gfw_cidr.txt` | `data/non_gfw_mask.txt` |
| `default` | `data/default_domains.txt` | `data/default_custom_ips.txt` | `data/default_cidr.txt` | `data/default_mask.txt` |

## 🧰 Mapa de scripts y flujo

| Script | Propósito |
|---|---|
| `code/nslookup.py` | Ejecutor base de resolución de dominio/IP |
| `code/nslookup_simplified.py` | Resolución centrada en AI + exportación CIDR |
| `code/nslookup_simplified_gfw.py` | Resolución centrada en GFW |
| `code/nslookup_simplified_gfw_w_ai.py` | Resolución combinada GFW + AI |
| `code/nslookup_simplified_gfw_wo_ai.py` | Resolución de GFW sin AI |
| `code/unique_sort.py` | Normalizar + desduplicar + salida JSON |
| `code/unique_sort_print.py` | Imprimir + escribir artefactos TXT/JSON canónicos |
| `code/list_utils.py` | Cargadores compartidos, máscaras y helpers de lista |
| `code/gui_app.py` | Backend de la GUI de Flask |
| `traffics/extract_youtube_traffic.py` | Ayuda OCR opcional para extracción de tráfico |
| `start_gui.sh` | Inicialización de virtualenv + instalación de dependencias + arranque del servidor |

## 🗂️ Estructura del proyecto

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

## 🎬 Demostración

![Domain & IP Manager demo](demos/demo.png)

## 🧾 Archivos de datos

Los archivos de datos son texto plano por líneas en `data/`:

```text
data/ai_domains.txt
data/ai_custom_ips.txt
data/ai_cidr.txt
data/ai_mask.txt
```

El mismo patrón de nombres se aplica a `gfw`, `ai_gfw`, `gfw_wo_ai`, `non_gfw` y `default`.

## 🧪 Ejemplos

Ejecutar un resolvedor directamente:

```bash
python3 code/nslookup_simplified_gfw.py
```

Formato de salida típico:

```text
domain.example.com
198.51.100.12/30
203.0.113.44/30
203.0.113.0/24
```

Ordenar una entrada personalizada a JSON:

```bash
python3 code/unique_sort.py -i ./my_list.txt -o ./output/my_list_unique_sorted.json
```

## 🧪 Notas de desarrollo

- La lógica compartida de carga y resolución reside en `code/list_utils.py`.
- Los escritores de salida usan un orden determinista para artefactos reproducibles.
- El repositorio actualmente no incluye un framework automático de pruebas.
- No hay `setup.py` / `pyproject.toml`; este es un proyecto orientado a scripts.
- `.github/FUNDING.yml` y los assets en `figs/*` indican integración de donación/funding.

## 🧯 Solucion de problemas

- `Input file not found: domain_and_ips.txt`
  - Ejecuta `python3 code/unique_sort.py -i <ruta> -o <ruta>` con una ruta de entrada válida, o asegúrate de que exista `domain_and_ips.txt` en la raíz del repositorio.
- Tiempos de espera o fallos en la consulta DNS
  - Verifica la conectividad de red y el acceso DNS, luego reintenta.
- La GUI no inicia en el puerto 5000
  - Confirma que `flask` esté instalado y que ningún proceso esté ocupando `127.0.0.1:5000`.
- Errores en la utilidad OCR
  - Verifica que `ffmpeg` y `tesseract` estén instalados y accesibles desde `PATH`.

## 🗺️ Hoja de ruta

- Añadir pruebas unitarias para parseado, aplicación de máscaras y utilidades de normalización.
- Añadir ayuda clara de CLI para todos los scripts y sus flags más comunes.
- Proveer un lockfile o definición de entorno reproducible para dependencias de Python.
- Añadir indicadores en la GUI para salidas fallidas de DNS y diferencias de salida fusionada.

## 🤝 Contribucion

Las contribuciones son bienvenidas. Flujo recomendado:

1. Abre una issue describiendo el problema o la solicitud de función.
2. Mantén los cambios enfocados y reproducibles.
3. Documenta el uso esperado de comandos y cambios de salida en la descripción del PR.
4. Actualiza `README.md` cuando cambie el comportamiento/comandos.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📬 Contacto

- Abre una issue en GitHub para reportar errores y solicitar funciones.
- Prefiere pasos de reproducción concisos, salida esperada y contexto del comando en los reportes.

## 📄 Licencia

En este momento no hay ningún archivo `LICENSE` rastreado en la raíz del repositorio.
