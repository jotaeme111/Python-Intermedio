import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Frames")
root .geometry("600x400")

#Creando un Frame superior.
frame_superior = tk.Frame(root, borderwidth=2, relief="groove", bg="lightblue")
frame_superior.pack(padx=10, pady=10, fill=tk.X)

label_titulo = tk.Label(frame_superior, text="Este es el Frame Superior", font=("Arial", 16))
label_titulo.pack(pady=10)

boton_a = tk.Button(frame_superior, text="Botón A", font=("Arial", 12))
boton_a.pack(side="right", padx=10, pady=5)
boton_b = tk.Button(frame_superior, text="Botón B", font=("Arial", 12))
boton_b.pack(side="left", padx=10, pady=5)

frame_inferior = tk.Frame(root, borderwidth=2, relief="groove", bg="lightgreen")
frame_inferior.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

label_info = tk.Label(frame_inferior, text="Este es el Frame Inferior", font=("Arial", 16))
label_info.pack(pady=10)

root.mainloop()
