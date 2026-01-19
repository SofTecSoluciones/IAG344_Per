# src/ia_service.py
# Este módulo simula la "INTELIGENCIA ARTIFICIAL".
# En realidad, usa expresiones regulares (Regex) para entender patrones en el texto del usuario.

import re  # Librería estándar para manejo de expresiones regulares

def interpretar_texto(texto):
    """
    Analiza una frase en lenguaje natural y la convierte en un diccionario de comandos.
    
    Args:
        texto (str): Frase del usuario (ej: "Limpia la columna A").
        
    Returns:
        dict: Diccionario con la acción y parámetros (ej: {"action": "clean...", "column": "A"}).
    """
    # Convertimos todo a minúsculas para facilitar la búsqueda (así "Limpia" o "limpia" es igual).
    texto = texto.lower()

    # --- 1. DETECCIÓN DE LIMPIEZA ---
    # Buscamos frases como "Limpia columna A", "Borra columna B", "Vacia columna C".
    # Regex: (limpia|borra|vacia) -> busca cualquiera de estas palabras (verbo).
    #        .* -> cualquier cosa en medio.
    #        columna\s+([a-z]+) -> la palabra "columna" espacio y luego letras (captura la letra de la columna).
    match_clean = re.search(r"(limpia|borra|vacia).*columna\s+([a-z]+)", texto)
    
    if match_clean:
        action_verb = match_clean.group(1) # El verbo que usó (limpia, borra, vacia)
        column = match_clean.group(2).upper() # La letra de la columna (convertida a MAYÚSCULAS)
        
        # Comportamiento por defecto: "smart_clean".
        # Limpia basura pero mantiene datos útiles (letras y números).
        mode = "smart_clean"
        
        # --- SUB-MODOS DE LIMPIEZA ---
        # Analizamos si el usuario fue más específico con keywords como "numeros" o "letras".
        
        if "numero" in texto or "número" in texto:
             # Si menciona "numeros"...
             if "quita" in texto or "elimina" in texto or "borra" in texto:
                 # Ej: "Quita los numeros" -> Queremos borrar dígitos -> Mode: keep_text (mantener solo texto)
                 mode = "keep_text" 
             elif "solo" in texto or "deja" in texto:
                 # Ej: "Deja solo numeros" -> Queremos mantener dígitos -> Mode: keep_digits
                 mode = "keep_digits" 
                 
        elif "letra" in texto or "texto" in texto:
             # Si menciona "letras"...
             if "quita" in texto or "elimina" in texto or "borra" in texto:
                 # Ej: "Quita letras" -> Queremos borrar texto -> Mode: keep_digits
                 mode = "keep_digits"
             elif "solo" in texto or "deja" in texto:
                 # Ej: "Deja solo texto" -> Queremos mantener texto -> Mode: keep_text
                 mode = "keep_text"

        # --- CASO ESPECIAL: BORRADO TOTAL ---
        # Si el usuario dijo "Borra columna" o "Vacia columna" (sin especificar "numeros" o "limpia"),
        # asumimos que quiere borrar TODO el contenido de la columna.
        # Pero solo si seguimos en el modo por defecto (smart_clean), para no interferir con "borra numeros".
        if action_verb in ["borra", "vacia"] and mode == "smart_clean":
             return {"action": "clean_column", "column": column, "mode": "empty"}

        # Devolvemos la orden estructurada
        return {
            "action": "clean_column",
            "column": column,
            "mode": mode
        }

    # --- 2. DETECCIÓN DE UNIÓN ---
    # Buscamos frases que contengan "une" o "unir".
    if "une" in texto or "unir" in texto:
        # Paso A: Encontrar TODAS las columnas mencionadas.
        # Dividimos el texto en la parte de origen y la de destino (si existe "en columna").
        parts = texto.split("en columna")
        source_part = parts[0]
        
        # re.findall busca todas las apariciones de "columna X" en la primera parte.
        sources = re.findall(r"columna\s+([a-z])", source_part)
        
        # Paso B: Encontrar el destino (si existe).
        # Buscamos si después de "en columna" hay una letra.
        match_target = re.search(r"en\s+columna\s+([a-z])", texto)
        target = match_target.group(1).upper() if match_target else None

        # Si encontramos al menos 2 columnas para unir...
        if len(sources) >= 2:
            return {
                "action": "merge_columns", # Acción de unir
                "sources": [c.upper() for c in sources], # Lista de columnas origen (A, B...)
                "target": target # Columna destino (puede ser None, el procesador lo manejará)
            }

    # Si no coincide con ningún patrón conocido, lanzamos error.
    raise ValueError("No se pudo interpretar la instrucción. \nFormatos soportados:\n- 'Limpia columna A'\n- 'Une columna A y columna B en columna C'")
