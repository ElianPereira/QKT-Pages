#!/usr/bin/env bash
# Extrae texto plano de un PDF con pdftotext (poppler) para que Claude lo
# lea como texto en vez de como tokens de imagen por página. Este repo no
# agrega dependencias de Python/Node (ver AGENTS.md), así que no hay
# fallback en Python: si pdftotext no está instalado, se pide instalarlo
# como herramienta de sistema.
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Uso: $0 <archivo.pdf> [rango_paginas ej. 1-3]" >&2
  exit 1
fi

archivo="$1"
rango="${2:-}"

if [ ! -f "$archivo" ]; then
  echo "No existe: $archivo" >&2
  exit 1
fi

if ! command -v pdftotext >/dev/null 2>&1; then
  echo "Falta 'pdftotext'. Instálalo como herramienta de sistema:" >&2
  echo "  Linux:  sudo apt install poppler-utils" >&2
  echo "  macOS:  brew install poppler" >&2
  exit 1
fi

if [ -n "$rango" ]; then
  inicio="${rango%-*}"
  fin="${rango#*-}"
  exec pdftotext -layout -f "$inicio" -l "$fin" "$archivo" -
fi

exec pdftotext -layout "$archivo" -
