---
name: extraer-pdf
description: Extrae el texto plano de un PDF (documento legal de referencia, copy fuente, evidencia adjunta a un Issue) antes de analizarlo, en vez de cargar el binario completo como tokens de imagen por página. Úsalo cuando la tarea sea leer o resumir el contenido de un PDF.
tools: Bash, Read
disable-model-invocation: true
---

# Extraer PDF (QKT-Pages)

Subir un PDF directo al contexto (`Read` sobre el binario) lo convierte en
tokens de imagen por página — caro y no hace falta cuando lo que se
necesita es el texto. Este proyecto no tiene dependencias de Python ni
Node (ver `AGENTS.md`), así que este skill usa solo `pdftotext` (poppler),
una herramienta de sistema, no un paquete que haya que agregar al repo.

## Uso

```bash
bash ${CLAUDE_SKILL_DIR}/extraer_pdf.sh <ruta.pdf> [rango_paginas]
```

Ejemplo:

```bash
bash ${CLAUDE_SKILL_DIR}/extraer_pdf.sh referencia_copy.pdf 1-2
```

La salida es texto plano por stdout — léela directamente, no vuelvas a
abrir el PDF con `Read`.

## Si `pdftotext` no está instalado

El script falla con instrucciones (`apt install poppler-utils` en Linux,
`brew install poppler` en macOS). No se agrega ninguna dependencia al
repo para resolverlo — es una herramienta de sistema, igual que
`python3 -m http.server` ya usado para desarrollo local.

## Imágenes

Este repo no tiene un paso de build ni Pillow/ImageMagick como
dependencia. Si una captura de pantalla es innecesariamente grande para
lo que la tarea requiere (confirmar layout, no leer texto fino), usa una
herramienta ya presente en el sistema antes de leerla —
`sips -Z 1568 entrada.png --out salida.png` en macOS o
`convert entrada.png -resize 1568x1568 salida.png` si hay ImageMagick—
en vez de instalar algo nuevo. La mayoría de las imágenes de este
proyecto (fotos de landing) no necesitan leerse en absoluto salvo que la
tarea sea literalmente sobre esa imagen.
