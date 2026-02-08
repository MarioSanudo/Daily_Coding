## 5) SaaS-applied (Python) — (Hard pero corto)
**Ruta:** `python/03-saas-applied/2026-02-07_safe-next/`

**Tarea:** Implementa `is_safe_next(next_url: str) -> bool` para evitar open-redirect.
Bloquea:
- `http://`, `https://`, `//`
- `javascript:`
- `\n` o `\r`
Permite rutas internas tipo `/dashboard`, `/perfil?tab=1`

**Tests mínimos**
- 8–10 asserts: 4 permitidos, 6 bloqueados (incluye `None`, `""`, `"//evil.com"`, `"https://evil.com"`, `"javascript:..."`, `"/ok\nx"`).

---