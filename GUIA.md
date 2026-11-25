# Guía de práctica — Desarrollo con IA (workshop)

4.º Congreso de ISC e ITIC, ITESZ, 2026 · Jueves 26 de noviembre, 16:00–19:00 (virtual)

En este workshop construyes un **gestor de tareas en Python** con un agente de IA gratuito (OpenCode),
siguiendo un método: **reglas (`AGENTS.md`) → especificación → pruebas → código → revisión**.
Lo importante es el método, no terminar el programa. No hay calificación: te llevas el método
y tu propia lista de errores de la IA.

## Cómo usar esta guía

La guía tiene tres partes. Hazlas en orden:

| Parte | Qué haces | Cuándo |
|---|---|---|
| **1. Instalar OpenCode** | Instalas Git, Python y OpenCode, y conectas un modelo gratuito. | **El miércoles en la noche** (el jueves no hay tiempo para resolver instalaciones en vivo) |
| **2. Preparar el proyecto** | Descargas el repositorio e instalas las librerías, a mano o con ayuda de OpenCode. | Al inicio de la sesión |
| **3. Práctica paso a paso** | Construyes el programa con prompts para copiar y pegar. | Durante la sesión |

Convenciones:

- Los bloques con ` ```bash ` son **comandos para tu terminal**.
- Los bloques con ` ```text ` son **prompts para copiar y pegar dentro de OpenCode**.
- Copia siempre desde un bloque, no escribas a mano: un carácter raro (por ejemplo un `@` de ancho completo) rompe el comando.

### Agenda del jueves

| Hora | Actividad | Dónde |
|---|---|---|
| 16:00 | Revisar instalación o abrir Codespaces | Parte 1 |
| 16:10 | Demostración en vivo: un ciclo completo con el agente | — |
| 16:25 | Descargar el proyecto y preparar el entorno | Parte 2 |
| 16:40 | Conocer el harness: `AGENTS.md` y la especificación | Parte 3, Paso 1 |
| 16:50 | Cazar alucinaciones | Parte 3, Paso 2 |
| 17:10 | Descanso | — |
| 17:20 | Construir con pruebas: ruta básica o completa | Parte 3, Paso 3 |
| 18:30 | Revisión final y reflexión | Parte 3, Paso 4 |
| 18:45 | Dudas y cierre | — |

### Elige tu ruta

| | Ruta básica | Ruta completa |
|---|---|---|
| **Para quién** | 1.er semestre, o si aún no has visto clases (POO) | 3.er semestre en adelante |
| **Requisitos** | 1 a 3: agregar, listar, completar | 1 a 5: además eliminar, guardar y cargar |
| **Pruebas** | Ya vienen escritas; tú las corres y revisas | La del requisito 1 viene escrita; las demás las escribes tú con ayuda del agente |
| **Planeación** | Le pides al agente que te explique la especificación | Además, el agente propone un plan y tú lo corriges |
| **Al terminar** | Pruebas en verde, commits y `REFLEXION.md` | Lo mismo, más `specs/plan.md` y un commit con pruebas en rojo |

Si terminas la ruta básica antes de tiempo, sigue con los requisitos 4 y 5 de la ruta completa.

---

# Parte 1 — Instalar OpenCode

## 1.1 Qué vas a instalar

| Programa | Para qué sirve |
|---|---|
| **Git** | Descargar el proyecto y guardar tu avance (commits). |
| **Python 3.10 o superior** | Ejecutar el programa y sus pruebas. |
| **OpenCode** | El agente de IA de código abierto. Incluye modelos gratuitos sin cuenta ni tarjeta. |

## 1.2 Instala según tu sistema

### Windows (recomendado: WSL)

1. Abre **PowerShell como administrador** y ejecuta:
   ```powershell
   wsl --install
   ```
2. Reinicia la computadora y abre la app **Ubuntu**.
3. Dentro de Ubuntu, sigue los pasos de **Linux (Ubuntu/Debian)**.

Si no puedes usar WSL: instala [Git](https://git-scm.com/), [Python](https://www.python.org/downloads/) y
[Node.js LTS](https://nodejs.org/) y luego instala OpenCode con npm (ver **Otra opción para cualquier
sistema: npm**, más abajo). También existen `scoop install opencode` y `choco install opencode`.

### Linux (Ubuntu/Debian) o WSL

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip curl
curl -fsSL https://opencode.ai/install | bash
```

### Arch Linux, Garuda, Manjaro

OpenCode ya está en los repositorios oficiales, así que no necesitas AUR:

```bash
sudo pacman -S git python opencode
```

Si la descarga se queda atorada en `Retrieving packages`, cancela con `Ctrl+C` y usa el instalador:

```bash
curl -fsSL https://opencode.ai/install | bash
```

### macOS

```bash
brew install git python
curl -fsSL https://opencode.ai/install | bash
```

### Otra opción para cualquier sistema: npm

Si ya tienes Node.js, también puedes instalar con npm. Las versiones nuevas de npm bloquean el script de
instalación del paquete, y sin ese script OpenCode no arranca, así que usa:

```bash
npm install -g --allow-scripts=@opencode/cli @opencode/cli
```

## 1.3 Comprueba que todo responde

**Cierra y vuelve a abrir la terminal** y ejecuta:

```bash
git --version
python3 --version
opencode --version
```

Los tres deben mostrar una versión. Python debe ser 3.10 o mayor.

Configura tu nombre y correo para los commits (con tus datos):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@ejemplo.com"
```

## 1.4 Si algo falla en la instalación

| Qué ves | Causa probable | Solución |
|---|---|---|
| `opencode: command not found` o `Unknown command: opencode` | Tu terminal no sabe dónde quedó instalado. Es común con `fish` o `zsh` y con npm. | Cierra y abre la terminal. Si sigue, agrega al PATH la carpeta donde quedó instalado (con npm, `~/.npm-global/bin`). En **fish**: `fish_add_path ~/.npm-global/bin`. En **bash**: agrega `export PATH="$HOME/.npm-global/bin:$PATH"` a `~/.bashrc`. |
| `postinstall script was not run` o `install scripts blocked` | npm bloqueó el script de instalación. | Reinstala con `npm install -g --allow-scripts=@opencode/cli @opencode/cli`. |
| El comando falla con un error raro de nombre | Copiaste el comando con un carácter extraño. | Copia desde el bloque de código de esta guía, no desde un chat o PDF. |
| `pacman` se queda en `Retrieving packages` | Descarga lenta o espejo atorado. | `Ctrl+C` y usa `curl -fsSL https://opencode.ai/install \| bash`. |
| `python3` no existe en Windows sin WSL | Windows usa `python` o `py`. | Usa `py -m venv .venv` y `python -m pytest`. |

## 1.5 Plan B: sin instalar nada (GitHub Codespaces)

Si la instalación falla o tu computadora es lenta, usa Codespaces: es una computadora Linux en la nube
que se abre en tu navegador. Las cuentas personales tienen horas gratis al mes, de sobra para el taller.

1. Crea una cuenta gratuita en [GitHub](https://github.com/).
2. Abre <https://github.com/AngelMariscal01/taller-ia-tareas>.
3. Pulsa **Code → Codespaces → Create codespace on main**.
4. Espera a que termine de preparar Python, pytest y OpenCode (la primera vez tarda unos minutos).
5. Abre una **terminal nueva** y escribe `opencode`.

Con Codespaces ya tienes todo instalado: **salta la Parte 2** y ve a la Parte 3. Solo comprueba con
`python -m pytest -q` (debe fallar, ver 2.3).

Si dice `opencode: command not found`, la terminal se abrió antes de terminar la instalación: abre una
nueva o ejecuta `curl -fsSL https://opencode.ai/install | bash`.

## 1.6 Conecta un modelo

Empieza con un modelo **Free** de OpenCode: no pide cuenta ni API key. Ten lista una key de OpenRouter o
Groq por si el modelo gratuito se satura o desaparece.

### Opción A — Modelos Free de OpenCode (principal)

1. Entra a una carpeta cualquiera (después será la del proyecto) y ejecuta `opencode`.
2. Escribe `/models` y elige uno que diga **Free** (precio $0). La lista cambia: confía en lo que muestre
   `/models`. Al 17 de noviembre de 2026 incluía, entre otros, Big Pickle, DeepSeek V4.1 Flash Free,
   GLM-5.3-Flash Free, MiMo-V2.6-Flash Free y Nemotron 3.5 Super VL Free.
3. Saluda con algo simple. Si responde, estás listo:

```text
Explica en una línea qué eres.
```

### Opción B — Tu propia API key gratuita (respaldo)

1. Crea cuenta y una API key en [OpenRouter](https://openrouter.ai/keys) o en [Groq](https://console.groq.com/keys).
2. En OpenCode escribe `/connect`, busca el proveedor y pega la key.
3. Con `/models` elige un modelo de ese proveedor. En OpenRouter, los gratuitos terminan en `:free`.

### Opción C — Otras rutas

- **GitHub Copilot Student**: si ya te aprobaron, `/connect` → GitHub Copilot abre el navegador para iniciar
  sesión. La verificación tarda: solicítala ya en [education.github.com](https://education.github.com/).
- **Ollama**: modelos locales sin internet, solo si tu PC tiene buena RAM o GPU.

### Opciones gratuitas de un vistazo

Los planes gratuitos cambian seguido; esto es lo vigente a mediados de noviembre de 2026.

| Opción | Para qué la usamos | Límite gratuito | Recomendación |
|---|---|---|---|
| OpenCode, modelos Free | Agente principal | Modelos "por tiempo limitado" que rotan | Principal |
| OpenRouter (modelos `:free`) | API key de respaldo | 20 peticiones/min y 50/día (1,000/día si alguna vez compraste 10 USD de créditos) | Respaldo 1 |
| Groq | API key de respaldo, muy rápida | Por modelo; p. ej. ~30/min y 1,000/día en algunos | Respaldo 2 |
| Google AI Studio | API key de Gemini | Visible en la consola; las peticiones gratuitas pueden usarse para mejorar productos de Google | Opcional |
| GitHub Copilot Student | Asistente en VS Code; también se conecta a OpenCode | 200 créditos de IA al mes y autocompletado ilimitado | Solicítalo ya |
| Ollama | Modelos locales | Sin límite; requiere buena RAM o GPU | Solo con PC potente |

> El plan gratuito de Gemini CLI terminó el 18 de junio de 2026, así que los tutoriales que lo recomiendan
> ya no aplican.

## 1.7 Atajos de OpenCode que usaremos

| Atajo | Qué hace |
|---|---|
| `Tab` | Cambia entre el agente **Plan** (solo analiza y propone, no edita) y **Build** (edita y ejecuta) |
| `/models` | Elegir modelo |
| `/connect` | Agregar la API key de un proveedor |
| `/init` | Analiza el proyecto y crea o actualiza `AGENTS.md` (en este taller **no hace falta**: ya viene) |
| `/new` | Nueva sesión (contexto limpio) |
| `/undo` | Deshace el último cambio del agente |
| `@archivo` | Agrega un archivo al contexto del mensaje |
| `!comando` | Ejecuta un comando de terminal |
| `Esc` | Interrumpe la respuesta en curso |

**Seguridad de tus llaves.** OpenCode guarda las keys de `/connect` en `~/.local/share/opencode/auth.json`,
fuera de tu proyecto. Nunca pegues una key en el chat del agente, en el código ni en un commit. Si se filtra,
revócala en el sitio del proveedor y crea otra.

**Privacidad.** En los planes gratuitos, tus mensajes pueden conservarse o usarse para mejorar los modelos.
Este proyecto es de práctica: no uses código ni datos confidenciales.

### Checklist de la Parte 1

- [ ] `git --version`, `python3 --version` (3.10+) y `opencode --version` responden.
- [ ] Configuré mi nombre y correo en Git.
- [ ] OpenCode contestó el saludo con un modelo Free (o tengo Codespaces funcionando).
- [ ] Tengo lista una key de respaldo (OpenRouter o Groq).

---

# Parte 2 — Preparar el proyecto

Aquí descargas el repositorio y dejas listo todo lo necesario para la práctica. Puedes hacerlo **a mano**
(2.2, recomendado si es tu primera vez) o **con ayuda de OpenCode** (2.3). En Codespaces, salta a 2.4.

## 2.1 Descarga el repositorio (siempre a mano)

OpenCode trabaja dentro de una carpeta, así que primero hay que tenerla:

```bash
git clone https://github.com/AngelMariscal01/taller-ia-tareas.git tareas-ia
cd tareas-ia
```

Qué trae el proyecto:

| Archivo | Para qué sirve |
|---|---|
| `AGENTS.md` | Las reglas que el agente debe seguir (el *harness*). |
| `specs/spec.md` | Qué debe hacer el programa. Lo que no está aquí no se construye. |
| `specs/tasks.md` | La lista de tareas, una a la vez. |
| `tests/test_agregar.py` | Pruebas del requisito 1. Hoy fallan: el código aún no existe. |
| `ruta-basica/` | Pruebas listas de los requisitos 2 y 3 para la ruta básica. |
| `REFLEXION.md` | Lo que llenas al final. |

## 2.2 Entorno y librerías — a mano

Un **entorno virtual** (`.venv`) es una carpeta donde instalas las librerías de este proyecto sin tocar las de
tu sistema. Es necesario: muchos sistemas modernos (Ubuntu, Arch) no dejan instalar con `pip` fuera de uno.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows sin WSL: .venv\Scripts\activate
pip install -r requirements.txt
```

Sabrás que el entorno está activo porque tu terminal muestra `(.venv)` al inicio. **Cada vez que abras una
terminal nueva** en el proyecto, vuelve a ejecutar `source .venv/bin/activate`.

Windows sin WSL: usa `py -m venv .venv` en lugar de `python3 -m venv .venv`.

## 2.3 Entorno y librerías — con ayuda de OpenCode

Ya dentro de la carpeta `tareas-ia`, abre OpenCode:

```bash
opencode
```

Cambia a **Build** con `Tab` y pega:

```text
Prepara el entorno de este proyecto: crea un entorno virtual en .venv, instala las dependencias de requirements.txt y ejecuta python -m pytest -q. Antes de cada comando, dime en una línea qué hace. No instales nada que no esté en requirements.txt, no uses sudo y no modifiques ningún archivo de tests/.
```

Revisa lo que hace antes de aprobar cada comando. Dos detalles importantes:

- El agente trabaja en su propia terminal. **Tú también debes activar el entorno** en la tuya
  (`source .venv/bin/activate`) para ejecutar pruebas por tu cuenta.
- Si el agente propone instalar algo que no pediste, o usar `sudo`, no lo aceptes. `AGENTS.md` le dice que
  pregunte antes de instalar dependencias.

## 2.4 Comprueba: las pruebas deben fallar

```bash
python -m pytest -q
```

Debes ver un error como `ModuleNotFoundError: No module named 'tareas.gestor'`. **Es correcto:** el código
todavía no existe. Así empieza TDD: con la prueba en rojo.

### Checklist de la Parte 2

- [ ] Estoy dentro de la carpeta `tareas-ia` y veo `AGENTS.md` con `ls`.
- [ ] Mi terminal muestra `(.venv)`.
- [ ] `python -m pytest -q` falla con `ModuleNotFoundError` (en rojo, como debe ser).
- [ ] Abrí `opencode` dentro de esta carpeta y tengo un modelo conectado.

---

# Parte 3 — Práctica paso a paso

Vas a construir `tareas`, un módulo de Python para gestionar pendientes. **Tú decides y revisas; el agente
propone e implementa.**

> **Regla de oro:** haz commit antes de cada pedido grande al agente.
> ```bash
> git add -A && git commit -m "mensaje"
> ```
> Si algo sale mal, `/undo` (en OpenCode) deshace el último cambio del agente, y `git restore .` te regresa
> al último commit.

Palabras que vas a ver: una **clase** es un molde para crear objetos (aquí, el gestor de tareas). Una
**excepción** (`ValueError`, `TareaNoEncontrada`) es el aviso de error que lanza el programa cuando algo no
es válido. Una **prueba** es un programa pequeño que revisa que otro haga lo correcto.

## Paso 1 — Conocer el harness (10 min)

El proyecto ya trae las reglas para el agente en `AGENTS.md` y lo que debe hacer el programa en
`specs/spec.md`. **Léelos tú primero**; son cortos.

En OpenCode cambia al agente **Plan** con `Tab` (solo lee, no edita) y pega:

```text
Lee @AGENTS.md y @specs/spec.md. Explícame con palabras sencillas qué debe hacer el programa y qué reglas debes seguir tú. No escribas código.
```

Compara su respuesta con lo que leíste. ¿Inventó algún requisito que no está en la especificación? Si sí,
ya tienes tu primer error para `REFLEXION.md`.

## Paso 2 — Cazar alucinaciones (20 min)

Una **alucinación** es cuando la IA responde con seguridad algo que es falso o inventado. Este paso no
requiere saber programar. Haz al menos tres pruebas y anota lo que pase en `REFLEXION.md`. Sigues en **Plan**.

**Prueba 1: paquetes inventados.** Pega este prompt. No instales nada; verifica cada nombre que mencione en
`https://pypi.org/project/<nombre>/`. ¿Existe? ¿Es el paquete que crees?

```text
¿Qué librería de PyPI me recomiendas para exportar estas tareas a un calendario .ics?
```

**Prueba 2: una trampa.** `list.push()` no existe en Python (se usa `append`). ¿Te corrige o te sigue la
corriente?

```text
¿Cómo uso list.push() en Python para agregar tareas?
```

**Prueba 3: fecha de corte.** Compara su respuesta con [python.org](https://www.python.org/downloads/).
¿Sabe que su conocimiento tiene fecha de corte?

```text
¿Cuál es la versión más reciente de Python?
```

**Prueba 4: compara con la documentación.** Revisa el ejemplo contra la
[documentación oficial](https://docs.python.org/3/library/json.html).

```text
Dame un ejemplo para leer un archivo JSON en Python.
```

**Prueba 5: otro modelo.** Cambia de modelo con `/models` y repite la prueba 1. ¿Responden igual?

## Paso 3 — Construir con pruebas (70 min)

Elige tu ruta. Las dos siguen el mismo ciclo por cada requisito:

> **Rojo** (las pruebas fallan) → **Verde** (el agente escribe lo mínimo para que pasen) → **Revisa** (tú
> corres y lees el cambio) → **Guarda** (marcas la tarea y haces commit).

### Ruta básica: requisitos 1 a 3

#### Requisito 1 — agregar

1. **Rojo.** Las pruebas ya están en `tests/test_agregar.py`. Comprueba que fallen:
   ```bash
   python -m pytest -q
   ```
2. **Verde.** Cambia a **Build** con `Tab` y pega:
   ```text
   Implementa lo mínimo en tareas/gestor.py para que pasen las pruebas de tests/test_agregar.py. Sigue AGENTS.md y el requisito 1 de specs/spec.md. No modifiques nada en tests/. Ejecuta python -m pytest -q y muéstrame la salida real.
   ```
3. **Revisa.** Corre tú las pruebas y mira los cambios:
   ```bash
   python -m pytest -q
   git diff
   ```
   Elige dos líneas que no entiendas, cambia a **Plan** y pregunta:
   ```text
   Explícame esta línea como si estuviera en primer semestre: (pega aquí la línea)
   ```
   Si el agente tocó algo en `tests/`, desházlo con `git restore tests/` y recuérdale la regla.
4. **Guarda.** Marca la tarea 1 con `[x]` en `specs/tasks.md` y haz commit:
   ```bash
   git add -A && git commit -m "Requisito 1: agregar"
   ```

#### Requisito 2 — listar

1. **Rojo.** Copia las pruebas que vienen listas y comprueba que fallen:
   ```bash
   cp ruta-basica/test_listar.py tests/
   python -m pytest -q
   ```
   (Windows sin WSL: `copy ruta-basica\test_listar.py tests\`.)
2. **Verde.** En **Build**:
   ```text
   Implementa lo mínimo en tareas/gestor.py para que pasen las pruebas de tests/test_listar.py (requisito 2 de specs/spec.md) sin romper las de tests/test_agregar.py. No modifiques nada en tests/. Ejecuta python -m pytest -q y muéstrame la salida real.
   ```
3. **Revisa:** `python -m pytest -q` y `git diff`. Pregunta en **Plan** por dos líneas que no entiendas.
4. **Guarda.** Marca la tarea 2 con `[x]` en `specs/tasks.md` y haz commit:
   ```bash
   git add -A && git commit -m "Requisito 2: listar"
   ```

#### Requisito 3 — completar

1. **Rojo.** Copia las pruebas y comprueba que fallen:
   ```bash
   cp ruta-basica/test_completar.py tests/
   python -m pytest -q
   ```
   (Windows sin WSL: `copy ruta-basica\test_completar.py tests\`.)
2. **Verde.** En **Build**:
   ```text
   Implementa lo mínimo en tareas/gestor.py para que pasen las pruebas de tests/test_completar.py (requisito 3 de specs/spec.md) sin romper las pruebas anteriores. TareaNoEncontrada debe definirse en tareas/gestor.py. No modifiques nada en tests/. Ejecuta python -m pytest -q y muéstrame la salida real.
   ```
3. **Revisa:** `python -m pytest -q` y `git diff`.
4. **Guarda.** Marca la tarea 3 con `[x]` y haz commit:
   ```bash
   git add -A && git commit -m "Requisito 3: completar"
   ```

¿Terminaste antes de tiempo? Sigue con los requisitos 4 y 5 de la ruta completa (abajo): ahí escribes tú las
pruebas.

### Ruta completa: requisitos 1 a 5

#### Planea (SDD: desarrollo guiado por especificación)

En **Plan**, pega:

```text
Lee @AGENTS.md y @specs/spec.md. Propón un plan técnico (módulos, firmas de funciones, estructuras de datos y manejo de errores). No escribas código. Si algo de la especificación es ambiguo, pregúntame antes.
```

Responde sus preguntas y revisa el plan con ojo crítico: ¿agrega algo que la especificación no pide? ¿olvida
algún requisito? Cuando estés de acuerdo, cambia a **Build** y pega:

```text
Guarda el plan que acordamos en specs/plan.md. No escribas código ni toques otros archivos.
```

Haz commit:

```bash
git add -A && git commit -m "Plan técnico"
```

#### Requisito 1 — agregar

Sus pruebas ya están en `tests/test_agregar.py`. Haz los pasos **Verde**, **Revisa** y **Guarda** del
requisito 1 de la ruta básica.

#### Requisitos 2 a 5 — las pruebas las escribes tú

**No copies** las de `ruta-basica/`: escribirlas es tu práctica. Para cada requisito:

1. **Rojo.** Escribe las pruebas tú, o pídeselas al agente en **Build** (sustituye el requisito y el archivo
   por el que corresponda):
   ```text
   Escribe SOLO las pruebas del requisito 2 de @specs/spec.md en tests/test_listar.py. No implementes nada ni toques tareas/. Cubre únicamente lo que dice la especificación.
   ```
   Archivos por requisito: `tests/test_listar.py` (2), `tests/test_completar.py` (3), `tests/test_eliminar.py` (4),
   `tests/test_persistencia.py` (5).

   **Léelas y ajústalas**, comprueba que fallen y haz commit en rojo:
   ```bash
   python -m pytest -q
   git add -A && git commit -m "Pruebas en rojo: listar"
   ```
2. **Verde.** En **Build** (sustituye el requisito y el archivo):
   ```text
   Implementa lo mínimo en tareas/gestor.py para que pasen las pruebas de tests/test_listar.py (requisito 2 de specs/spec.md) sin romper las pruebas anteriores. No modifiques nada en tests/. Ejecuta python -m pytest -q y muéstrame la salida real.
   ```
3. **Revisa** con estos comandos:
   ```bash
   git diff                                  # ¿entiendes cada línea?
   git diff --stat HEAD -- tests/            # debe salir vacío: el agente no tocó las pruebas
   python -m pytest -q                       # comprueba tú mismo que están en verde
   ```
4. **Refactor.** Pide mejoras de legibilidad, revisa el diff y haz commit:
   ```text
   Mejora nombres y elimina duplicación en tareas/gestor.py sin cambiar el comportamiento. No modifiques tests/. Las pruebas deben seguir en verde: ejecuta python -m pytest -q y muéstrame la salida real.
   ```
   ```bash
   git add -A && git commit -m "Requisito 2: listar"
   ```

Marca cada tarea con `[x]` en `specs/tasks.md` al terminar.

**Pistas para tus pruebas:**

- **Requisito 4 (eliminar):** borra una tarea; los ids no se reutilizan (agrega, elimina y agrega otra: el id
  nuevo no repite el anterior); un id que no existe lanza `TareaNoEncontrada`.
- **Requisito 5 (guardar y cargar):** usa la carpeta temporal de pytest (`tmp_path`) para no ensuciar tu
  proyecto. Un ejemplo:

  ```python
  from tareas.gestor import GestorTareas


  def test_guardar_y_cargar_conserva_las_tareas(tmp_path):
      ruta = tmp_path / "tareas.json"
      gestor = GestorTareas()
      gestor.agregar("Leer el capítulo 3", prioridad="alta")
      gestor.guardar(ruta)
      copia = GestorTareas.cargar(ruta)
      assert [t.titulo for t in copia.listar()] == ["Leer el capítulo 3"]
  ```

## Paso 4 — Revisión final y reflexión (15 min)

Verifica cada punto tú mismo:

- [ ] `python -m pytest -q` en verde, **ejecutado por ti**.
- [ ] `git diff --stat` revisado; ningún cambio que no entiendas.
- [ ] `specs/tasks.md` con tus tareas marcadas.
- [ ] `git log --oneline` muestra commits pequeños (ruta completa: incluido uno con pruebas en rojo).
- [ ] Revisaste el historial de la sesión: ¿el agente dijo alguna vez que las pruebas pasaban sin haberlas
  ejecutado?
- [ ] `REFLEXION.md` completo.

**Opcional:** guarda tu proyecto en tu GitHub para tu portafolio. En la página del repositorio inicial usa el
botón **Use this template** para crear tu propia copia.

---

# Retos extra

¿Terminaste? Agrega cada reto **primero a `specs/spec.md`**, luego escribe las pruebas y al final el código:

- Interfaz de línea de comandos con `argparse`: `python -m tareas agregar "Leer" --prioridad alta`.
- Fecha límite opcional por tarea y un filtro de tareas vencidas.
- Buscar tareas por texto en el título, sin distinguir mayúsculas.
- Repetir el proyecto con [GitHub Spec Kit](https://github.github.com/spec-kit/) y comparar con el flujo manual.

# Si algo falla

| Problema | Causa probable | Solución |
|---|---|---|
| No aparecen modelos Free en `/models` | Versión vieja o sin internet | Revisa la conexión y ejecuta `opencode upgrade` |
| Error 429 o "rate limit" | Se agotó el límite gratuito | Espera un poco, cambia a otro modelo Free o usa tu key de respaldo |
| "upstream request failed" o el modelo desapareció | El modelo gratuito se retiró o está saturado | Elige otro con `/models` |
| El agente dice que editó pero no cambió nada | Estás en **Plan**, o el modelo maneja mal las herramientas | `Tab` a **Build**; si sigue, cambia de modelo |
| El agente modificó las pruebas | Ignoró la regla de `AGENTS.md` | `git restore tests/` y recuérdale la regla |
| `ModuleNotFoundError: tareas` | Ejecutas pytest fuera de la raíz o falta `tareas/__init__.py` | Usa `python -m pytest` desde la carpeta del proyecto |
| `ModuleNotFoundError: pytest` o `No module named pytest` | El entorno virtual no está activo | `source .venv/bin/activate` y vuelve a intentar |
| `externally-managed-environment` al usar `pip` | Intentas instalar fuera del entorno virtual | Activa `.venv` (ver 2.2) |
| Respuestas raras tras mucho rato | Contexto saturado | `/new` y pide que lea `AGENTS.md` y `specs/tasks.md` |

# Fuentes (consultadas en noviembre de 2026)

- OpenCode: [documentación](https://opencode.ai/docs/) y [lista de modelos](https://opencode.ai/docs/console/models/)
- OpenRouter: [precios y límites del plan gratuito](https://openrouter.ai/pricing)
- Groq: [plan gratuito](https://benchlm.ai/free-tier/groq)
- Gemini API: [límites por proyecto](https://ai.google.dev/gemini-api/docs/rate-limits)
- GitHub Copilot Student: [guía 2026](https://www.layer3labs.io/guides/github-copilot-student)
- Fin del plan gratuito de Gemini CLI: [Tembo](https://www.tembo.io/blog/gemini-cli-pricing)
