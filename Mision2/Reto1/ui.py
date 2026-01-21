# ui.py
# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
from tkinter import messagebox,filedialog
from controller import procesar_instruccion


def iniciar_app():
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")
    # Etiqueta
    tk.Label(root, text="Escriba una instrucción en lenguaje natural").pack(pady=10)
    
    def seleccionar_excel():
        path= filedialog.askopenfilename(
        title="Seleccionar archivo Excel",
        filetypes=[("Archivo Excel","*.xlsx")]
        )
        if path:
           #messagebox.showinfo("Resultado", path)
           path_label.config(text=path)
    
    boton=tk.Button(
        root,
        text="Seleccionar archivo Excel",
        command=seleccionar_excel,
        width=30,
        height=2
    )
    path_label=tk.Label(root,
                         text="sin archivo",
                         width=30,
                         height=2
                         )
    path_label.pack(pady=10)
    
    boton.pack(pady=15)
     # Etiqueta path
    

    # Campo de texto
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)

    # Acción del botón
    def ejecutar():
        texto = entrada.get()
        path=path_label.cget("text")
        exito, mensaje = procesar_instruccion(texto,path)

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    # Botón
    tk.Button(root, text="Ejecutar instrucción", command=ejecutar).pack(pady=20)

    root.mainloop()
