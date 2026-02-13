🎯 Ejercicio de Hoy - Jueves 13/02/2026
Python Advanced — Context Manager para DB Connection
Ruta: Python/Advanced/2026-02-13_db-context-manager/

📝 Objetivo
Implementar un context manager (with statement) que simule la gestión de una conexión a base de datos.
Este patrón es fundamental en Flask/SQL para:

Abrir conexión automáticamente
Cerrar conexión aunque haya errores
Evitar leaks de recursos


🧠 Descripción
Crea una clase DBConnection que:

Al entrar al contexto (__enter__):

Imprime "Conexión abierta"
Retorna self


Al salir del contexto (__exit__):

Imprime "Conexión cerrada"
Si hubo excepción, imprime "Error capturado: {excepción}"
Retorna True para suprimir la excepción (no la propague)


Método auxiliar execute(query):

Si query contiene la palabra "ERROR", lanza ValueError("Query inválida")
Sino, imprime "Ejecutando: {query}"