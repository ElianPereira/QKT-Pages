# Responsabilidades de Claude Code

**Ya no se usa Codex** (decisión del propietario, 2026-08-17: "ya de plano no
lo vamos a utilizar para nada, no me gustó, se quedó muy corto"). Claude
implementa directo, tras planificar — no hay hand-off a otro ejecutor. El
"Contrato Issue → plan → implementación" de `AGENTS.md` sigue vigente en su
disciplina (investigar antes de tocar código, plan claro, alcance
incluido/excluido, criterios de aceptación, validaciones), pero léelo
sustituyendo "Codex" por "Claude" en cada mención: quien confirma que el
plan es ejecutable e implementa es la misma sesión, no dos agentes distintos.

Para cambios de contenido/copy chicos y acotados, sigue aplicando el
requisito de `AGENTS.md`: "todo cambio de texto, datos de contacto, enlaces
externos o afirmaciones comerciales requiere respaldo explícito en el
Issue" — eso no cambió, solo quién ejecuta.

Claude Code actúa como responsable de análisis, planificación e implementación. Durante la fase de planificación debe:

1. Investigar el problema y reproducirlo o confirmar la necesidad antes de proponer una solución.
2. Leer `AGENTS.md`, inspeccionar la arquitectura y los controles existentes e identificar los archivos, páginas y flujos relevantes.
3. Tomar y explicar las decisiones arquitectónicas necesarias, priorizando el enfoque mínimo compatible con el repositorio.
4. Publicar en el GitHub Issue un plan ordenado, concreto y ejecutable, con archivos y pasos claramente identificados.
5. Definir el alcance incluido y excluido, criterios de aceptación verificables, validaciones técnicas y, cuando corresponda, validaciones visuales con viewports y estados relevantes.
6. Registrar riesgos, restricciones, dependencias, supuestos y cualquier aspecto de seguridad, accesibilidad o compatibilidad que deba preservarse.

Para cambios grandes o ambiguos, sigue valiendo la pena publicar el plan en el Issue antes de tocar código, y esperar a que el propietario confirme decisiones no obvias en los comentarios. Para cambios chicos y ya autorizados explícitamente por el propietario en la conversación, implementar directo es válido. Si la investigación no permite un plan seguro y verificable, Claude debe documentar las preguntas o bloqueos en el Issue (o preguntar directo) en lugar de inventar requisitos.
