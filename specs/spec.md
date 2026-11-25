# Especificación: gestor de tareas

## Objetivo
Un módulo de Python para registrar pendientes, marcarlos como hechos y guardarlos en un archivo.

## Interfaz
Clase `GestorTareas` en `tareas/gestor.py`. Cada tarea tiene: `id`, `titulo`, `prioridad`, `completada`.
Si `id` no existe al completar o eliminar, se lanza la excepción `TareaNoEncontrada`, definida en el mismo archivo.

## Requisitos
1. `agregar(titulo, prioridad="media")` crea una tarea y la devuelve.
   - `id` incremental desde 1; no se reutiliza aunque se elimine una tarea.
   - `titulo`: se quitan espacios de los extremos; vacío o de más de 100 caracteres -> `ValueError`.
   - `prioridad`: "alta", "media" o "baja"; otro valor -> `ValueError`.
2. `listar(estado=None, prioridad=None)` devuelve una lista de tareas.
   - `estado`: `None` (todas), "pendientes" o "completadas".
   - `prioridad`: `None` (todas) o "alta", "media", "baja".
   - Orden: prioridad alta, luego media, luego baja; empates por `id`.
3. `completar(id)` marca la tarea como completada; si no existe -> `TareaNoEncontrada`.
4. `eliminar(id)` borra la tarea; si no existe -> `TareaNoEncontrada`.
5. `guardar(ruta)` escribe las tareas en un archivo JSON; `GestorTareas.cargar(ruta)` las recupera.

## Fuera de alcance
Interfaz gráfica, usuarios, fechas, base de datos.
