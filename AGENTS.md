# AGENTS.md — Gestor de tareas (taller Desarrollo con IA, ITESZ)

## Qué es este proyecto
Un módulo de Python llamado `tareas` para registrar pendientes, marcarlos como hechos y guardarlos en un archivo.
La especificación está en `specs/spec.md`. Lo que no esté en la especificación no se construye.

## Estructura
- `tareas/gestor.py`: código del módulo (todavía no existe; lo crearás tú, agente).
- `tests/`: pruebas con pytest. Las escribe o aprueba la persona, no el agente.
- `specs/`: especificación (`spec.md`) y lista de tareas (`tasks.md`).

## Reglas del proyecto
- Python 3.10+. El código usa solo la biblioteca estándar; pytest es solo para pruebas.
- Las pruebas se ejecutan con: `python -m pytest -q`
- Nunca modifiques ni borres archivos de `tests/` para que las pruebas pasen.
  Si crees que una prueba está mal, detente y explícame por qué.
- No instales dependencias nuevas sin preguntarme.
- Trabaja una sola tarea de `specs/tasks.md` a la vez y márcala con [x] al terminar.
- Antes de decir "listo", ejecuta las pruebas y muestra el resultado real.
- Explica cada cambio en 2 o 3 líneas, en español y con palabras sencillas:
  quien te usa puede ser estudiante de primer semestre.
