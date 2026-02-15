Python Fundamentals - Viernes 14 Feb 2025
Ejercicio: Sistema de Gestión de Usuarios con Validaciones
Dificultad: Media
Tiempo estimado: 30-45 minutos
Conceptos: Clases, validaciones, métodos, propiedades, manejo de errores

Contexto
Vas a construir un sistema básico de gestión de usuarios que incluya validaciones propias de un SaaS real. Este ejercicio te prepara para manejar datos de usuarios en tu aplicación de análisis biomecánico.

Objetivos de aprendizaje

Diseñar clases con validaciones robustas
Implementar propiedades con getters/setters
Manejar errores de forma controlada
Aplicar lógica de negocio en métodos de clase
Pensar en casos edge que pueden romper tu sistema


Especificaciones
Parte 1: Clase User (20 min)
Crea una clase User con las siguientes características:
Atributos privados:

_email (str)
_subscription_tier (str): "free", "pro", "enterprise"
_created_at (datetime)
_is_active (bool)

Validaciones obligatorias:

Email debe contener "@" y "."
Email debe tener al menos 5 caracteres
Subscription tier solo puede ser uno de los 3 valores permitidos
Email no puede cambiarse después de creación (inmutable)