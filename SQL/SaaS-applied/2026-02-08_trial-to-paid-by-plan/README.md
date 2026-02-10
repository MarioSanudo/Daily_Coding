# Trial → Paid Conversion by Plan (PostgreSQL)

## 📌 Descripción
Ejercicio de **SQL aplicado a un SaaS realista**.  
El objetivo es analizar la conversión de usuarios desde **trial** a **plan de pago**, agrupado por tipo de plan.

Este tipo de query es muy común en dashboards de producto, métricas de negocio y análisis de crecimiento.

---

## 🎯 Objetivo del ejercicio
Escribir una consulta SQL que muestre **por cada plan**:

- Número de usuarios que iniciaron un **trial**
- Número de usuarios que **convirtieron a pago**
- **Ratio de conversión** (`converted / trial`), redondeado a 2 decimales

---

## 🧠 Reglas / criterios de aceptación

La consulta debe cumplir:

- Una fila por cada `plan`
- `trial_users`:
  - Cuenta **usuarios distintos**
  - Basta con que exista una fila de suscripción (trial iniciado)
- `converted_users`:
  - Cuenta **usuarios distintos**
  - `paid_at IS NOT NULL`
- `conversion_rate`:
  - `converted_users::numeric / NULLIF(trial_users, 0)`
  - Redondeado a **2 decimales**
- Orden:
  - Primero por `conversion_rate` DESC
  - Luego por `plan` ASC

---

## 🗂️ Estructura del ejercicio

```text
sql/
└── 03-saas-applied/
    └── 2026-02-08_trial-to-paid-by-plan/
        ├── README.md
        ├── schema.sql
        └── solution.sql   (opcional)



