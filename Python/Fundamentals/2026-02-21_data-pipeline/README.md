# Python Fundamentals — Mini Pipeline de Datos

**Fecha:** 2026-02-21  
**Dificultad:** Medium (20–35 min)  
**Conceptos:** Funciones puras, list comprehensions, dicts, filtros, transformaciones

---

## Objetivo

Construir un pipeline de transformación de datos en pasos encadenados,
sin clases ni decoradores. Solo funciones puras bien definidas.

Este patrón aparece constantemente al procesar datos biomecánicos:
recibir datos brutos → limpiar → filtrar → transformar → resumir.

---

## Contexto

Recibes una lista de sesiones de análisis en bruto desde un formulario.
Algunas tienen datos incompletos o inválidos. Tu tarea es procesarlas.

---

## Datos de entrada
```python
raw_sessions = [
    {"user": "mario", "duration_min": 45, "avg_power": 210, "valid": True},
    {"user": "ana",   "duration_min": 0,  "avg_power": 180, "valid": True},
    {"user": "luis",  "duration_min": 30, "avg_power": None, "valid": True},
    {"user": "mario", "duration_min": 60, "avg_power": 250, "valid": True},
    {"user": "ana",   "duration_min": 20, "avg_power": 195, "valid": False},
    {"user": "luis",  "duration_min": 55, "avg_power": 230, "valid": True},
    {"user": "mario", "duration_min": 10, "avg_power": 170, "valid": True},
]
```

---

## Funciones a implementar

### 1. `filter_valid(sessions)`
Devuelve solo las sesiones donde `valid=True` Y `duration_min > 0`
Y `avg_power` no es `None`.

### 2. `normalize_session(session)`
Recibe una sesión válida y devuelve un dict nuevo con:
- `user`: igual que antes
- `duration_min`: igual
- `avg_power`: igual
- `intensity`: `"high"` si avg_power >= 220, `"medium"` si >= 180,
  `"low"` en cualquier otro caso

### 3. `group_by_user(sessions)`
Recibe la lista ya normalizada y devuelve un dict agrupado por usuario:
```python
{
  "mario": [session1, session2, ...],
  "luis":  [session1, ...],
}
```

### 4. `summarize_user(sessions_list)`
Recibe la lista de sesiones de UN usuario y devuelve:
```python
{
  "total_sessions": int,
  "total_minutes": int,
  "avg_power": float,   # media redondeada a 1 decimal
  "top_intensity": str  # la intensidad más frecuente
}
```

### 5. `run_pipeline(raw_sessions)`
Encadena todo:
1. Filtra con `filter_valid`
2. Normaliza cada sesión con `normalize_session`
3. Agrupa con `group_by_user`
4. Resume cada usuario con `summarize_user`
5. Devuelve un dict `{user: summary, ...}`

---

## Resultado esperado con los datos de entrada
```python
{
  "mario": {
    "total_sessions": 3,
    "total_minutes": 115,
    "avg_power": 210.0,
    "top_intensity": "medium"
  },
  "luis": {
    "total_sessions": 1,
    "total_minutes": 55,
    "avg_power": 230.0,
    "top_intensity": "high"
  }
}
# ana queda fuera: valid=False en una, duration=0 en otra
```

---

## Entregables

- `solution.py` con las 5 funciones
- `test_pipeline.py` con tests para al menos:
  - `filter_valid`: que elimina correctamente los 3 casos inválidos
  - `normalize_session`: que asigna bien la intensidad
  - `run_pipeline`: resultado final completo

---

## Criterios de evaluación

- Ninguna función modifica los datos originales (sin mutación)
- `normalize_session` devuelve un dict nuevo, no modifica el de entrada
- `summarize_user` calcula `top_intensity` con lógica real
  (no hardcodeada)
- Los tests cubren casos borde (lista vacía, un solo usuario)

---

## Pista para top_intensity

Usa `max()` con una función `key`. Investiga cómo contar frecuencias
con un dict o con `collections.Counter`.