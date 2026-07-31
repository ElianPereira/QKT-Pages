# Responsabilidades de Claude Code

Claude Code actúa como responsable de análisis y planificación. Durante esta fase debe:

1. Investigar el problema y reproducirlo o confirmar la necesidad antes de proponer una solución.
2. Leer `AGENTS.md`, inspeccionar la arquitectura y los controles existentes e identificar los archivos, páginas y flujos relevantes.
3. Tomar y explicar las decisiones arquitectónicas necesarias, priorizando el enfoque mínimo compatible con el repositorio.
4. Publicar en el GitHub Issue un plan ordenado, concreto y ejecutable por Codex, con archivos y pasos claramente identificados.
5. Definir el alcance incluido y excluido, criterios de aceptación verificables, validaciones técnicas y, cuando corresponda, validaciones visuales con viewports y estados relevantes.
6. Registrar riesgos, restricciones, dependencias, supuestos y cualquier aspecto de seguridad, accesibilidad o compatibilidad que Codex deba preservar.

Durante la planificación, Claude no debe implementar código, modificar archivos, crear commits ni abrir un Pull Request. La implementación comienza únicamente después de que el plan esté publicado en el Issue y corresponde a Codex. Si la investigación no permite un plan seguro y verificable, Claude debe documentar las preguntas o bloqueos en el Issue en lugar de inventar requisitos.
