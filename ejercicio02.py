import tkinter as tk
from tkinter import messagebox, ttk

def procesar_texto(): # Función para procesar el texto. 
    texto = entrada_texto.get()

    if not texto:
        messagebox.showwarning("Campo vacío", "Por favor ingrese el texto para poder procesarlo.")
        return
    if texto.isnumeric():
        messagebox.showwarning("Entrada inválida", "Por favor ingrese solo texto (No ingresar números).")
        return

    longitud = len(texto)
    texto_mayusculas = texto.upper()

    label_longitud.config(text = f"Longitud: {longitud}")
    label_mayus.config(text = f"Texto en mayúsculas: {texto_mayusculas}")

# Ventana principal de la app:
root = tk.Tk()
root.title("Contador y manipulador de texto simple")
root.geometry("450x450")
root.configure(bg="gray10")

style = ttk.Style()
style.theme_use('clam')
style.configure('Dark.TLabel', background = "grey10", foreground = "white", font = ("Arial", 12)) # Etiquetas.
style.configure('Dark.TButton', foreground = "white", background = "gray30") # Botones.
style.map('Dark.TButton', background = [('active', 'gray40')])
style.configure('Dark.TEntry', foreground = "white", background = "gray30", fieldbackground = "gray30", insertcolor = "white") # Entrada de texto.

entrada_texto = ttk.Entry(root, width = 40, style = 'Dark.TEntry')
entrada_texto.grid(row = 1, column = 0, padx = 10, pady = 20)

label_instruccion = ttk.Label(root, text = "Ingrese el texto aquí:", style = 'Dark.TLabel')
label_instruccion.grid(row = 0, column = 0, padx = 10, pady = 20)
label_longitud = ttk.Label(root, text = "Longitud: 0", style = 'Dark.TLabel') # Etiqueta para la longitud del texto.
label_longitud.grid(row = 3, column = 0, padx = 10, pady = 20)
label_mayus = ttk.Label(root, text = "Texto en mayúsculas:", style = 'Dark.TLabel')
label_mayus.grid(row = 4, column = 0, padx = 10, pady = 20) # Etiqueta para el texto en mayúsculas.

boton_procesar = ttk.Button(root, text = "Procesar Texto", command = procesar_texto, style = 'Dark.TButton') # Botón para procesar el texto.
boton_procesar.grid(row=2, column=0, padx=10, pady=30)
boton_salir = ttk.Button(root, text = "Salir", command = root.quit, style = 'Dark.TButton') # Botón para salir.
boton_salir.grid(row = 5, column = 0, padx = 10, pady = 30)

root.grid_columnconfigure(0, weight=1)
root.mainloop()