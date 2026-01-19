# src/ui.py
# Este módulo maneja la INTERFAZ GRÁFICA DE USUARIO (GUI).
# Utiliza la librería estándar 'tkinter'.

import tkinter as tk  # Importamos tkinter y lo renombramos como 'tk' para escribir menos
from tkinter import messagebox, filedialog  # Importamos submódulos específicos para mensajes emergentes y selección de archivos
from src.controller import procesar_instruccion  # Importamos la función del controlador que conecta la UI con la lógica

def iniciar_app():
    """
    Función principal que construye y lanza la ventana de la aplicación.
    Aquí se definen todos los botones, etiquetas y campos de texto.
    """
    
    # Creamos la ventana principal (la raíz de la interfaz)
    root = tk.Tk()
    
    # Le ponemos un título a la ventana
    root.title("Procesador Excel Inteligente")
    
    # Configuramos el tamaño inicial de la ventana (ancho x alto)
    root.geometry("600x400")

    # --- Variables de control ---
    # Variable de tipo StringVar de Tkinter para almacenar la ruta del archivo seleccionado.
    # Usar StringVar permite que si cambia el valor, se actualice automáticamente cualquier etiqueta vinculada.
    file_path_var = tk.StringVar()

    # --- Funciones internas de la UI ---

    def seleccionar_archivo():
        """
        Abre una ventana nativa del sistema operativo para buscar un archivo.
        """
        # filedialog.askopenfilename abre el explorador de archivos.
        # Filtramos para mostrar archivos Excel (.xlsx) o todos (*.*).
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")]
        )
        
        # Si el usuario seleccionó algo (no canceló), guardamos la ruta en nuestra variable.
        if ruta:
            file_path_var.set(ruta)  # Esto actualizará automáticamente la etiqueta lbl_ruta

    def ejecutar():
        """
        Función que se llama cuando se presiona el botón 'EJECUTAR'.
        Recoge los datos de la interfaz y llama al controlador.
        """
        # Obtenemos el valor actual de la ruta del archivo desde la variable de control
        ruta = file_path_var.get()
        
        # Obtenemos el texto que el usuario escribió en el campo de instrucción
        instruccion = entrada_instruccion.get()
        
        # --- Llamada a la Lógica ---
        # Pasamos la instrucción y la ruta al 'controlador'.
        # El controlador se encargará de entender qué hacer (IA) y hacerlo (Procesador).
        # Nos devuelve 'exito' (True/False) y un 'mensaje' descriptivo.
        exito, mensaje = procesar_instruccion(instruccion, ruta)
        
        # --- Respuesta Visual ---
        if exito:
            # Si todo salió bien, mostramos un mensaje de información (icono azul de 'i')
            messagebox.showinfo("Éxito", mensaje)
        else:
            # Si hubo error, mostramos un mensaje de error (icono rojo de 'X')
            messagebox.showerror("Error", mensaje)

    # --- Construcción del Diseño (Layout) ---

    # 1. SECCIÓN DE ARCHIVO
    # LabelFrame crea un marco con un título ("Archivo") para agrupar elementos visualmente.
    frame_archivo = tk.LabelFrame(root, text="Archivo", padx=10, pady=10)
    # .pack() coloca el elemento en la ventana. 'fill="x"' hace que se estire horizontalmente.
    frame_archivo.pack(fill="x", padx=10, pady=5)

    # Botón para abrir el explorador de archivos
    btn_archivo = tk.Button(frame_archivo, text="Seleccionar Archivo", command=seleccionar_archivo)
    # Lo ponemos a la izquierda dentro del marco
    btn_archivo.pack(side="left")

    # Etiqueta que muestra la ruta seleccionada.
    # 'textvariable=file_path_var' conecta esta etiqueta con la variable; si la variable cambia, el texto cambia.
    lbl_ruta = tk.Label(frame_archivo, textvariable=file_path_var, fg="blue")
    lbl_ruta.pack(side="left", padx=10)

    # 2. SECCIÓN DE INSTRUCCIÓN
    # Otro marco agrupador para la instrucción
    frame_instruccion = tk.LabelFrame(root, text="Instrucción", padx=10, pady=10)
    frame_instruccion.pack(fill="x", padx=10, pady=5)

    # Etiqueta de ayuda estática
    lbl_inst = tk.Label(frame_instruccion, text="Escriba su instrucción (ej: 'Une columna A y columna B en columna C')")
    lbl_inst.pack(anchor="w") # anchor="w" alinea a la izquierda (West)

    # Campo de entrada de texto (Entry)
    entrada_instruccion = tk.Entry(frame_instruccion, width=70)
    entrada_instruccion.pack(fill="x", pady=5)

    # 3. BOTÓN PRINCIPAL
    # Botón grande para ejecutar la acción
    btn_ejecutar = tk.Button(
        root, 
        text="EJECUTAR", 
        bg="#4CAF50", fg="white", # Colores personalizados (Verde fondo, Blanco texto)
        font=("Arial", 12, "bold"), # Fuente más grande y negrita
        command=ejecutar # Vinculamos con la función 'ejecutar' definida arriba
    )
    btn_ejecutar.pack(pady=20) # pady=20 deja espacio vertical alrededor

    # Iniciar el bucle de eventos
    # Esto mantiene la ventana abierta y esperando clics o teclas del usuario.
    root.mainloop()
