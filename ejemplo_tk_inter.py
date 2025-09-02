import tkinter as tk 
from tkinter import messagebox #Caja de mensajes para mostrar alertas o información al usuario.

def saludar():
    messagebox.showinfo("Saludo", "¡Hola, bienvenido a la aplicación!") #Muestra un mensaje de saludo.

def mostrar_saludo():
    nombre = entry_nombre.get() #Obtiene el texto ingresado en la entrada de texto.
    if nombre:
        messagebox.showinfo("Saludo", f"¡Hola, {nombre}!") #Muestra un mensaje de saludo personalizado.
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")

root = tk.Tk() #creando una instacia de tkinter. En root se puede poner cualquier nombre, pero es una convención usar root.
root.title("Este es el titulo que le pongo a la ventana") #titulo de la ventana
root.geometry("400x300") #dimensiones de la ventana

label_pregunta = tk.Label(root, text="¿Cuál es tu nombre?", font=("Arial", 12)) #Etiqueta para preguntar el nombre.
label_pregunta.pack(pady=10) #Empaqueta la etiqueta en la ventana con un margen vertical de 10 píxeles.

entry_nombre = tk.Entry(root, width=30, font=("Arial", 12)) #Entrada de texto para que el usuario ingrese su nombre.
entry_nombre.pack(pady=10) #Empaqueta la entrada de texto en la ventana 

boton_saludar = tk.Button(root, text="Saludar", command=mostrar_saludo, font=("Arial", 12), fg="white", bg="green") #Botón que al hacer clic llama a la función mostrar_saludo.
boton_saludar.pack(pady=10) #Empaqueta el botón en la ventana

#Crear una etiqueta (label) para mostrar texto en la ventana.
label = tk.Label(root, text="¡Hola, Bienvenido a mi app!", font=("Arial", 16), fg="blue", bg="white") #Creando una etiqueta. #root es el padre de la etiqueta, lo envia a la etiqueta principal.
label.pack(pady=20) #Empaqueta la etiqueta en la ventana con un margen vertical de 20 píxeles.

#Crear un botón que al hacer clic llame a la función saludar.
button = tk.Button(root, text="Haz clic para saludar", command=saludar, font=("Arial", 12), fg="white", bg="blue") #Creando un botón. Al hacer clic en el botón, se ejecuta la función saludar.
button.pack(pady=10) #Empaqueta el botón en la ventana con un margen vertical de 10 píxeles.

root.mainloop() #Para mostrar la ventana. Es un bucle infinito que mantiene la ventana abierta hasta que se cierre.

