# Gestor de tareas con un agente de IA

Proyecto inicial del taller **Desarrollo con IA** (4.º Congreso de ISC e ITIC, ITESZ, 2026).
Vas a construir un módulo de Python con un agente de IA gratuito (OpenCode), siguiendo un método:
**reglas (AGENTS.md) → especificación → pruebas → código → revisión**.

## Qué trae
| Archivo | Para qué sirve |
|---|---|
| `AGENTS.md` | Las reglas que el agente debe seguir (el *harness*). |
| `specs/spec.md` | Qué debe hacer el programa. Lo que no está aquí no se construye. |
| `specs/tasks.md` | La lista de tareas, una a la vez. |
| `tests/test_agregar.py` | Pruebas del requisito 1. Hoy fallan: el código aún no existe. |
| `ruta-basica/` | Pruebas listas de los requisitos 2 y 3 para la ruta básica. |
| `REFLEXION.md` | Lo que llenas al final. |

## Empezar
**Opción A — en tu computadora** (necesitas Git, Python 3.10+ y OpenCode):
```bash
git clone <URL-de-este-repositorio> tareas-ia
cd tareas-ia
python3 -m venv .venv
source .venv/bin/activate        # Windows sin WSL: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q              # debe FALLAR: así empieza TDD
opencode
```

**Opción B — sin instalar nada (GitHub Codespaces):** con tu cuenta de GitHub, en esta página pulsa
**Code → Codespaces → Create codespace on main**. Espera a que termine de preparar el entorno,
abre una terminal nueva y escribe `opencode`.

La guía completa del workshop (instalación, preparación del proyecto y práctica con prompts para copiar y pegar) está en [GUIA.md](GUIA.md).
