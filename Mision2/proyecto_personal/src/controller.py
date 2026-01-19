# src/controller.py
# El CONTROLADOR actúa como intermediario.
# Recibe las peticiones de la UI, coordina la "inteligencia" (ver qué hacer) y la "acción" (hacerlo).

# Importamos las funciones de nuestros otros módulos:
# 'interpretar_texto' analiza el lenguaje natural (IA).
# 'ejecutar_accion' realiza los cambios físicos en el Excel.
from src.ia_service import interpretar_texto
from src.processor import ejecutar_accion

def procesar_instruccion(texto, file_path):
    """
    Función central que orquesta el proceso.
    
    Args:
        texto (str): La instrucción escrita por el usuario (ej: "Limpia columna A").
        file_path (str): La ruta completa del archivo Excel a modificar.
        
    Returns:
        tuple: (bool, str) -> (Éxito?, Mensaje de respuesta)
    """
    try:
        # 1. Validación básica: ¿El usuario seleccionó un archivo?
        if not file_path:
            return False, "Por favor seleccione un archivo Excel primero."
            
        # 2. Interpretación (Capa de IA)
        # Le damos el texto crudo y recibimos un diccionario con la orden estructurada.
        # Ej: "Limpia col A" -> {"action": "clean_column", "column": "A", "mode": "smart_clean"}
        instruccion = interpretar_texto(texto)
        
        # 3. Ejecución (Capa de Procesamiento)
        # Le damos la orden estructurada y el archivo. La función abre el Excel, lo modifica y lo guarda.
        # Nos devuelve un mensaje de texto confirmando qué hizo.
        mensaje = ejecutar_accion(instruccion, file_path)
        
        # Si llegamos aquí sin errores, devolvemos True y el mensaje de éxito.
        return True, mensaje
        
    except Exception as e:
        # Manejo de ERRORES:
        # Si algo falla en cualquier paso (archivo no encontrado, orden no entendida, error de excel),
        # capturamos la excepción (e) y devolvemos False junto con la descripción del error.
        # Esto evita que el programa se cierre de golpe y le muestra el error al usuario.
        return False, str(e)
