from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from flask import Flask, jsonify, request, send_from_directory
import dns.resolver

from list_utils import load_lists, load_mask, unique_preserve, write_output

APP_ROOT = Path(__file__).resolve().parents[1]
GUI_DIR = APP_ROOT / "gui"
DATA_DIR = APP_ROOT / "data"

DEFAULT_MASKS: Dict[str, str] = {
    "ai": "32",
    "gfw": "32",
    "ai_gfw": "32",
    "gfw_wo_ai": "32",
    "default": "24",
}

app = Flask(__name__, static_folder=str(GUI_DIR), static_url_path="/")


def run_lookup(list_key: str) -> List[str]:
    mask = load_mask(list_key, DEFAULT_MASKS.get(list_key, "32"))
    domains, custom_ips, cidr = load_lists(list_key)
    domains = unique_preserve(domains)

    def get_ips(domain: str) -> List[str]:
        try:
            answers = dns.resolver.resolve(domain, "A")
            return [answer.to_text() for answer in answers]
        except dns.resolver.NoAnswer:
            return ["No A record found"]
        except dns.resolver.NXDOMAIN:
            return ["No such domain"]
        except Exception as exc:
            return [f"Error obtaining IPs for domain {domain}: {exc}"]

    results: List[str] = []
    for domain in domains:
        ips = get_ips(domain)
        results.append(domain)
        results.extend([ip + f"/{mask}" for ip in ips])

    for ip in custom_ips:
        results.append(ip + f"/{mask}")

    results.extend(cidr)

    seen = set()
    output_lines = [x for x in results if not (x in seen or seen.add(x) or x.startswith("No"))]
    write_output(output_lines, f"gui_{list_key}")
    return output_lines


@app.get("/")
def index():
    return send_from_directory(GUI_DIR, "index.html")


@app.get("/api/list")
def api_get_list():
    list_key = request.args.get("key", "ai_gfw")
    list_type = request.args.get("type", "domains")
    path = DATA_DIR / f"{list_key}_{list_type}.txt"
    if not path.exists():
        return jsonify({"lines": []})
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()]
    return jsonify({"lines": lines})


@app.post("/api/list")
def api_save_list():
    payload = request.get_json(force=True)
    list_key = payload.get("key", "ai_gfw")
    list_type = payload.get("type", "domains")
    lines = payload.get("lines", [])
    path = DATA_DIR / f"{list_key}_{list_type}.txt"
    path.write_text("\n".join(lines).strip() + ("\n" if lines else ""), encoding="utf-8")
    return jsonify({"ok": True})


@app.get("/api/mask")
def api_get_mask():
    list_key = request.args.get("key", "ai_gfw")
    mask = load_mask(list_key, DEFAULT_MASKS.get(list_key, "32"))
    return jsonify({"mask": mask})


@app.post("/api/mask")
def api_save_mask():
    payload = request.get_json(force=True)
    list_key = payload.get("key", "ai_gfw")
    mask = str(payload.get("mask", "")).strip()
    if not mask:
        mask = DEFAULT_MASKS.get(list_key, "32")
    path = DATA_DIR / f"{list_key}_mask.txt"
    path.write_text(mask + "\n", encoding="utf-8")
    return jsonify({"ok": True, "mask": mask})


@app.post("/api/run")
def api_run():
    payload = request.get_json(force=True)
    list_key = payload.get("key", "ai_gfw")
    output_lines = run_lookup(list_key)
    return jsonify({"lines": output_lines})


@app.get("/app.js")
def app_js():
    return send_from_directory(GUI_DIR, "app.js")


@app.get("/styles.css")
def styles_css():
    return send_from_directory(GUI_DIR, "styles.css")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
