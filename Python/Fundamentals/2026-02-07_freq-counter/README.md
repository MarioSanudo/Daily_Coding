## 1) Python Fundamentals — (Easy)
**Ruta:** `python/01-fundamentals/2026-02-07_freq-counter/`

**Tarea:** Implementa `word_freq(text: str) -> dict[str, int]`  
- Convierte a minúsculas  
- Ignora puntuación básica `.,;:!?`  
- Colapsa espacios múltiples  
- Devuelve conteo de palabras

**Ejemplos**
- `"Hi hi, bye!"` → `{"hi": 2, "bye": 1}`
- `"  A  a, a. "` → `{"a": 3}`

**Tests mínimos (pytest)**
- 3–5 asserts con los ejemplos + un caso vacío `"" -> {}`

---