🎯 Objetivo

Implementar un decorador en Python llamado:

@retry(max_tries=3, exceptions=(Exception,))

que permita reintentar la ejecución de una función cuando esta lanza una excepción permitida.

🧠 Descripción

El decorador debe envolver una función y:

Ejecutarla

Si lanza una excepción incluida en exceptions, volver a intentarlo

Repetir hasta un máximo de max_tries

Si se agotan los intentos, relanzar la excepción

🔁 Comportamiento esperado
Caso 1: la función falla algunas veces y luego funciona

La función falla 2 veces

En el 3er intento funciona

El decorador devuelve el valor correctamente

Resultado esperado:

✔️ No se lanza excepción

✔️ Se devuelve el resultado ("OK" por ejemplo)

Caso 2: la función falla siempre

La función falla en los 3 intentos

El decorador relanza la excepción

Resultado esperado:

✔️ Se lanza una excepción tras el último intento

🧩 Decorador retry

El decorador añade lógica adicional a la función original:

Control de intentos

Manejo de excepciones con try / except

Decisión de reintento o fallo definitivo

Esquema conceptual:

retry
└── función original
    ├── intento 1 → excepción
    ├── intento 2 → excepción
    └── intento 3 → éxito o excepción final

🧪 Tests

Se deben implementar 2 tests.

Los tests deben usar funciones con un contador interno, que:

Fallen un número determinado de veces

Luego devuelvan un valor correcto

Esto permite verificar que:

El decorador reintenta correctamente

Se respeta max_tries

La excepción se relanza cuando corresponde

✅ Criterios de aceptación

Si falla 2 veces y a la 3ª funciona → devuelve el resultado

Si falla siempre → lanza excepción tras max_tries

No reintenta infinitamente

Solo captura las excepciones indicadas

⚠️ Errores comunes

Reintentar sin límite

No relanzar la excepción final

Ignorar el parámetro max_tries

Capturar excepciones no incluidas en exceptions