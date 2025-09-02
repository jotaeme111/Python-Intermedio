import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title("Utilizando el Pack Geometry")
style = ttk.Style()
style.theme_use('clam')
style.configure('frame', background = 'green')


root.configure(bg="lightblue")

root.geometry("600x400")

background_frame = tk.Frame(root, bg="blue")
background_frame.pack(fill=tk.BOTH, expand=True)

btn1 = tk.Button(background_frame, text = 'Botón 1 (superior)')
btn1.pack(padx=10)

btn2 = tk.Button(background_frame, text = 'Botón 2 (Izquierda)')
btn2.pack(side=tk.LEFT, padx=10, pady=10)

btn3 = tk.Button(background_frame, text = 'Botón 3 (Derecha)')
btn3.pack(side=tk.RIGHT, padx=10)

label_fill = tk.Label(background_frame, text="Esta etiquea esta llenando un espacio",bg="blue")
label_fill.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

btn4 = tk.Button(background_frame, text='Botón 4 (Abajo)')
btn4.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()

