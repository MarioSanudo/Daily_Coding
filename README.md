# saas-practice-lab

Repo de práctica para mantener rutina en los lenguajes y habilidades que uso (o usaré) en mi SaaS:
**Python + SQL (PostgreSQL) + HTML/CSS** (y más adelante **JavaScript**).

Objetivo: ejercicios cortos, frecuentes y con verificación (tests o checks), organizados por nivel:
- **Fundamentals**: lógica, bucles, funciones, estructuras básicas.
- **Advanced**: herramientas/idiomas del lenguaje (decoradores, generators, tests, etc.).
- **SaaS-applied**: utilidades directamente aplicables a una web (Flask/DB/UI).

---

## Estructura del repo

saas-practice-lab/
├─ python/
│ ├─ 01-fundamentals/
│ ├─ 02-advanced/
│ └─ 03-saas-applied/
├─ sql/
│ ├─ 01-fundamentals/
│ ├─ 02-advanced/
│ └─ 03-saas-applied/
├─ web/
│ ├─ html/
│ ├─ css/
│ └─ saas-applied/
└─ templates/
└─ exercise_README.md


---

## Plantilla por ejercicio (carpeta)
Cada ejercicio es una carpeta con:

- `README.md` → resumen del enunciado + link a la fuente (si existe) + ejemplos
- `solution.*` → mi solución final
- `test_solution.py` o `tests/` → tests cuando tenga sentido
- `notes.md` → aprendizajes y edge cases (opcional)

Ejemplo:
`python/01-fundamentals/2026-02-07_freq-counter/`

---

## Dificultad
- **Easy (5–15 min)**: un concepto + 2–3 casos.
- **Medium (15–40 min)**: varios casos borde + tests.
- **Hard (45–120 min)**: mini-problemas tipo SaaS o SQL más serio.

Voy alternando dificultad con el tiempo (no siempre “easy”).

---

## Cómo ejecutar

### Python
- Ejecutar solución:
  ```bash
  python solution.py
  
Tests (si existen):
  pytest -q

Instalar pytest (una vez, en tu venv):¡
pip install pytest

SQL (PostgreSQL)
Normalmente en DBeaver:
Ejecuta schema.sql (si el ejercicio trae esquema/datos)
Ejecuta query.sql

HTML/CSS
Abre index.html en el navegador o usa Live Server (VS Code).


Convención de nombres
Carpetas: YYYY-MM-DD_nombre-corto/
