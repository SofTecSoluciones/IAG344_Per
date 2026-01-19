# main.py
# Este archivo es el PUNTO DE ENTRADA de la aplicación.
# Su única responsabilidad es iniciar la interfaz gráfica.

# Importamos la función 'iniciar_app' del módulo 'ui' que se encuentra en la carpeta 'src'.
# Esta función contiene el bucle principal de la ventana (Tkinter).
from src.ui import iniciar_app

# Este bloque verifica si el script se está ejecutando directamente (no importado como módulo).
# Es una buena práctica en Python para evitar que el código se ejecute accidentalmente si se importa este archivo.
if __name__ == "__main__":
    # Llamamos a la función que construye y muestra la ventana de la aplicación.
    # El programa se quedará "bloqueado" aquí hasta que el usuario cierre la ventana.
    iniciar_app()
