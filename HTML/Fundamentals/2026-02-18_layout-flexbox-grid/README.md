# HTML/CSS Fundamentals — Layout con Flexbox y Grid

**Fecha:** 2026-02-18  
**Dificultad:** Medium (25–40 min)  
**Conceptos:** Flexbox, CSS Grid, responsive layout puro (sin Tailwind)

---

## Objetivo

Construir una página de esqueleto de dashboard con dos zonas de layout:
una barra lateral fija + área de contenido principal con tarjetas en grid.

Este patrón es la base visual de cualquier SaaS. Lo harás en CSS puro
(sin Tailwind) para entender el mecanismo antes de usar el framework.

---

## Estructura esperada

La página debe verse así (esquemático):

+------------------+-----------------------------+
|                  |  [Card 1]  [Card 2]         |
|   SIDEBAR        |  [Card 3]  [Card 4]         |
|   - Nav item 1   |                             |
|   - Nav item 2   |   (grid de tarjetas)        |
|   - Nav item 3   |                             |
+------------------+-----------------------------+

---

## Especificaciones

### Layout general (Flexbox)
- El body ocupa el 100% del viewport (altura completa)
- Sidebar a la izquierda: ancho fijo de 220px, fondo oscuro (#1e1e2e),
  texto claro
- Área principal a la derecha: ocupa el espacio restante (flex: 1),
  fondo gris claro (#f4f4f5)
- Sin scroll lateral, sin overflow raro

### Sidebar (HTML semántico + Flexbox vertical)
- Usa `<nav>` con una lista `<ul>` de 3-4 ítems
- Título/logo arriba: texto "BikeAnalytics" en blanco
- Ítems de navegación: "Dashboard", "Análisis", "Historial", "Ajustes"
- El último ítem ("Ajustes") debe pegarse al fondo del sidebar
  → Pista: flex-direction: column + margin-top: auto

### Área principal (CSS Grid)
- Padding interno de 32px
- Título "Panel de control" en la parte superior
- Debajo, un grid de tarjetas: 2 columnas en desktop,
  1 columna en móvil (< 768px)
- 4 tarjetas con: título, valor numérico y etiqueta de estado
  Ejemplos:
  - "Sesiones analizadas" / 47 / badge verde "activo"
  - "Usuarios activos" / 12 / badge azul "online"
  - "Análisis pendientes" / 3 / badge amarillo "pendiente"
  - "Errores detectados" / 1 / badge rojo "alerta"

### Tarjetas (Card component en CSS puro)
- Fondo blanco, border-radius 8px, box-shadow suave
- Padding 24px
- El badge de estado es un `<span>` con colores según estado:
  verde, azul, amarillo, rojo

### Responsive
- En pantallas < 768px: sidebar se oculta (display: none)
  y las tarjetas pasan a 1 columna

---

## Entregables

- `solution.html` — un único fichero HTML con `<style>` interno
  (sin ficheros .css externos, sin Tailwind)

---

## Criterios de evaluación

- El layout no se rompe al redimensionar la ventana
- El sidebar tiene el ítem "Ajustes" pegado al fondo
- El grid de tarjetas es realmente un CSS Grid (no Flexbox)
- El layout general sidebar+main es realmente Flexbox
- Los badges tienen colores distintos según estado
- Media query funcional para móvil
- HTML semántico: `<nav>`, `<main>`, `<section>`, `<header>`

---

## Pistas si te quedas trabado

- Para la estructura raíz: `display: flex` en el contenedor padre
- Para las tarjetas: `display: grid; grid-template-columns: repeat(2, 1fr)`
- Para el ítem pegado al fondo: `margin-top: auto` dentro de un flex column
- `height: 100vh` en el wrapper principal para ocupar toda la pantalla

---

## Después de entregarlo, reflexiona

1. ¿Cuándo usarías Flexbox vs Grid en un componente real?
2. ¿Qué ventaja te da entender esto antes de usar Tailwind?