#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

REQ_HASH_FILE="$VENV_DIR/.requirements_hash"
REQ_HASH=""
if command -v shasum >/dev/null 2>&1; then
  REQ_HASH="$(shasum -a 256 "$ROOT_DIR/requirements.txt" | awk '{print $1}')"
elif command -v sha256sum >/dev/null 2>&1; then
  REQ_HASH="$(sha256sum "$ROOT_DIR/requirements.txt" | awk '{print $1}')"
fi

NEED_INSTALL=1
if [[ -n "$REQ_HASH" && -f "$REQ_HASH_FILE" ]]; then
  if [[ "$(cat "$REQ_HASH_FILE")" == "$REQ_HASH" ]]; then
    NEED_INSTALL=0
  fi
fi

if [[ $NEED_INSTALL -eq 1 ]]; then
  python -m pip install --upgrade pip
  python -m pip install -r "$ROOT_DIR/requirements.txt"
  if [[ -n "$REQ_HASH" ]]; then
    echo "$REQ_HASH" > "$REQ_HASH_FILE"
  fi
fi

exec python "$ROOT_DIR/code/gui_app.py"
