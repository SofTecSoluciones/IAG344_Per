# https://docs.python.org/es/3/library/tkinter.html
import tkinter as tk
from tkinter import filedialog,messagebox
from proccessor import process_excel_safe

def seleccionar_excel():
    return filedialog.askopenfilename(
    title="Seleccionar archivo Excel",
    filetypes=[("Archivo Excel","*.xlsx")]
    )
def on_clic_procesar():
    archivo = seleccionar_excel()
    exito,mensaje=process_excel_safe(archivo)
    if exito:
        messagebox.showinfo("Proceso completado",mensaje)
    else:
        messagebox.showerror("Error",mensaje)
def iniciar_app():
    root = tk.Tk()
    root.title("Procesador de archivos Excel")
    root.geometry("400x400")
    root.resizable(False,False)

    boton = tk.Button(
        root,
        text="Seleccionar archivo Excel",
        command=on_clic_procesar,
        width=30,
        height=2
    )
    boton.pack(pady=60)
    root.mainloop()