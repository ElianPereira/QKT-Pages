#!/usr/bin/env python3
"""
Verificación de seguridad de la landing estática (QKT-Pages).

Se ejecuta en CI para que un cambio futuro no elimine sin querer las
protecciones de seguridad de la página. No necesita dependencias externas.

Reglas:
  1. El HTML debe parsear sin errores.
  2. Debe existir un meta Content-Security-Policy con las directivas clave.
  3. Debe existir un meta referrer.
  4. Todo enlace target="_blank" debe llevar rel con "noopener".
  5. Ningún recurso (src/href) debe cargarse por http:// inseguro.

Sale con código != 0 si alguna regla falla, imprimiendo el motivo.
"""
import os
import re
import sys
from html.parser import HTMLParser

ARCHIVO = "index.html"
HEADERS_FILE = "_headers"


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.metas = []            # lista de dicts de atributos de <meta>
        self.blank_links = []      # (rel_value_or_None) por cada <a target=_blank>

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta":
            self.metas.append(d)
        if tag == "a" and d.get("target", "").lower() == "_blank":
            self.blank_links.append(d.get("rel"))


def main():
    errores = []
    with open(ARCHIVO, encoding="utf-8") as f:
        html = f.read()

    p = Parser()
    try:
        p.feed(html)
        p.close()
    except Exception as e:  # noqa: BLE001
        print(f"[FAIL] El HTML no parsea: {e!r}")
        return 1

    # 2. CSP
    csp = None
    referrer_ok = False
    for m in p.metas:
        equiv = m.get("http-equiv", "").lower()
        if equiv == "content-security-policy":
            csp = m.get("content", "")
        if m.get("name", "").lower() == "referrer":
            referrer_ok = True

    if not csp:
        errores.append("Falta el meta Content-Security-Policy.")
    else:
        requeridas = ["default-src 'self'", "frame-ancestors", "object-src 'none'"]
        for directiva in requeridas:
            if directiva not in csp:
                errores.append(f"La CSP no contiene la directiva requerida: {directiva}")

    # 3. Referrer
    if not referrer_ok:
        errores.append("Falta el meta name=\"referrer\".")

    # 4. target=_blank sin rel=noopener
    for rel in p.blank_links:
        if rel is None or "noopener" not in rel.lower():
            errores.append(
                'Hay un <a target="_blank"> sin rel="noopener" (riesgo de reverse tabnabbing).'
            )
            break

    # 5. Recursos por http:// inseguro (no confundir con xmlns dentro de data: URIs)
    inseguros = re.findall(r'(?:src|href)\s*=\s*["\']http://[^"\']+', html, re.IGNORECASE)
    if inseguros:
        errores.append(f"Recurso(s) cargado(s) por http:// inseguro: {inseguros[:3]}")

    # 6. _headers de Cloudflare Pages con las cabeceras de seguridad reales.
    if not os.path.exists(HEADERS_FILE):
        errores.append(
            f'Falta el archivo "{HEADERS_FILE}" con las cabeceras de seguridad HTTP (Cloudflare Pages).'
        )
    else:
        with open(HEADERS_FILE, encoding="utf-8") as f:
            headers = f.read()
        requeridas = [
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Referrer-Policy",
        ]
        for h in requeridas:
            if h not in headers:
                errores.append(f'El archivo "{HEADERS_FILE}" no incluye la cabecera requerida: {h}')

    if errores:
        print("Verificación de seguridad de la página: FALLÓ")
        for e in errores:
            print(f"  [FAIL] {e}")
        return 1

    print("Verificación de seguridad de la página: OK")
    print("  - CSP presente con directivas clave")
    print("  - meta referrer presente")
    print(f"  - {len(p.blank_links)} enlace(s) target=_blank, todos con rel=noopener")
    print("  - sin recursos http:// inseguros")
    print("  - _headers con cabeceras de seguridad HTTP (Cloudflare Pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
