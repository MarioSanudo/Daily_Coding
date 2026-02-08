## 3) SQL Fundamentals — (Easy)
**Ruta:** `sql/01-fundamentals/2026-02-07_users-orders-summary/`

Crea `schema.sql` (si no tienes uno común aún) con algo así:

**Tarea:** Mostrar por usuario: `name`, número de pedidos, gasto total.  
- Incluye usuarios sin pedidos (que salgan con 0 y 0).  
- Ordena por gasto total desc.

**Esquema mínimo**
- `users(id, name)`
- `orders(id, user_id, total)`

**Aceptación**
- Usa `LEFT JOIN` + `COUNT` + `COALESCE(SUM(...), 0)`
- Los usuarios sin pedidos aparecen igualmente.