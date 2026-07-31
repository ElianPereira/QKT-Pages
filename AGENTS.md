# Guía de trabajo para agentes

## Arquitectura y tecnologías

QKT-Pages es una landing institucional estática, sin framework, gestor de paquetes ni proceso de compilación. `index.html` contiene el marcado semántico, los estilos CSS y el JavaScript del navegador. Cloudflare Pages publica directamente los archivos del repositorio y aplica las cabeceras declaradas en `_headers`.

Las únicas automatizaciones del proyecto usan Python 3.12 y la biblioteca estándar: `.github/scripts/check_page_security.py` comprueba invariantes de seguridad del HTML y de las cabeceras. No hay dependencias de Python ni de Node que instalar.

## Estructura

- `index.html`: página completa; incluye contenido, CSS responsive y comportamiento del menú, navegación y animaciones.
- `_headers`: cabeceras HTTP para Cloudflare Pages, incluida la Content Security Policy (CSP).
- `.github/scripts/`: validaciones locales reutilizadas por CI.
- `.github/workflows/`: integración continua y controles de seguridad.
- `.github/ISSUE_TEMPLATE/`: formulario con el contrato de planificación para una implementación.
- `.github/pull_request_template.md`: evidencia que Codex debe entregar al solicitar revisión.
- `CLAUDE.md`: responsabilidades de Claude durante la fase de análisis y planificación.
- `README.md`: identificación breve del sitio.

## Comandos reales

Ejecuta los comandos desde la raíz del repositorio.

| Tarea | Comando | Notas |
| --- | --- | --- |
| Instalación | No aplica | No existe `package.json`, archivo de bloqueo ni dependencia externa. No generes uno salvo que el Issue lo requiera expresamente. |
| Desarrollo local | `python3 -m http.server 8000` | Visita `http://localhost:8000/`; detén el servidor con `Ctrl+C`. |
| Seguridad/prueba automatizada | `python3 .github/scripts/check_page_security.py` | Es la validación automatizada existente y no instala paquetes. |
| Lint | No disponible | El repositorio no define un linter. No inventes un comando. |
| Pruebas funcionales | No disponibles | No existe suite adicional; realiza comprobación manual cuando corresponda. |
| Comprobación de tipos | No disponible | El proyecto no usa TypeScript ni otro verificador de tipos. |
| Build | No aplica | Cloudflare Pages sirve los archivos estáticos directamente; no se genera un artefacto. |

## Convenciones de código y diseño

- Mantén HTML, CSS y JavaScript nativos, sin introducir frameworks o dependencias salvo decisión explícita del Issue.
- Conserva el idioma español, la semántica y la accesibilidad: etiquetas adecuadas, textos alternativos o nombres accesibles y navegación por teclado.
- Sigue el formato compacto ya usado en `index.html`; usa clases en kebab case y reutiliza las clases y variables CSS existentes.
- Conserva el sistema visual definido en `:root`, las familias Cormorant Garamond e IBM Plex Sans, los breakpoints existentes y el comportamiento responsive.
- Prefiere las variables CSS a colores duplicados. No cambies contenido, enlaces, identidad visual, espaciado o interacciones fuera del alcance aprobado.
- Mantén el JavaScript pequeño y sin dependencias, al final del documento. Comprueba la existencia y accesibilidad de los elementos que agregues.

## Componentes, estilos y contenido

- Este proyecto no tiene componentes desacoplados: cada sección de la landing funciona como una unidad lógica dentro de `index.html`.
- Modifica solo la sección necesaria. Evita refactorizaciones, reordenamientos o reformateos globales que oculten el cambio funcional.
- Reutiliza botones, títulos, divisores, cuadrículas e iconos existentes antes de crear nuevas variantes.
- Todo cambio de texto, datos de contacto, enlaces externos o afirmaciones comerciales requiere respaldo explícito en el Issue.
- Conserva las vistas de escritorio y móvil. Cualquier elemento nuevo debe revisarse al menos a anchos representativos de móvil y escritorio.

## Seguridad

- No elimines ni debilites la CSP, las cabeceras de `_headers` ni las reglas de `.github/scripts/check_page_security.py`.
- No agregues secretos, tokens, credenciales, datos personales ni valores sensibles al repositorio, al HTML, a los logs o a las capturas.
- Usa HTTPS para recursos externos. Todo enlace con `target="_blank"` debe incluir al menos `rel="noopener"` (preferiblemente `noopener noreferrer`).
- Evalúa cualquier dominio o tipo de recurso nuevo y actualiza la CSP solo con el permiso mínimo necesario; documenta el motivo y el riesgo en el PR.
- Evita HTML inseguro, ejecución dinámica (`eval`, `new Function`), manejadores construidos con datos no confiables y dependencias de terceros innecesarias.
- Ejecuta siempre `python3 .github/scripts/check_page_security.py` antes de solicitar revisión.

## Contrato Issue → plan → implementación

- El GitHub Issue y el plan publicado por Claude son la fuente de verdad. Respeta estrictamente su alcance incluido y excluido, criterios de aceptación y validaciones.
- Antes de editar, confirma que el Issue contiene un plan ejecutable e identifica los archivos afectados. No amplíes el alcance por conveniencia.
- Si el plan resulta incompleto, inseguro o incompatible con el repositorio, detén esa parte y deja constancia; no improvises cambios de producto.
- Documenta en el Pull Request toda desviación del plan, su causa, impacto y decisión tomada. Si no hubo desviaciones, indícalo expresamente.
- Relaciona el PR con el Issue, enumera los archivos modificados y registra cada comando ejecutado con su resultado.

## Validación visual

Cuando un cambio pueda percibirse en la página:

1. Inicia `python3 -m http.server 8000` y revisa la página servida, no solo el archivo abierto directamente.
2. Compara antes y después en escritorio y móvil; verifica layout, tipografía, colores, estados hover/focus, menú, enlaces y ausencia de desbordamiento horizontal.
3. Captura evidencia antes y después con el mismo viewport y estado. Adjúntala al PR; si no es posible, explica la limitación.
4. Revisa la consola del navegador y documenta errores o advertencias relevantes.
5. Ejecuta además la comprobación automatizada de seguridad.
