import os

base = "proyecto_demo"
subcarpetas = ["entrada", "salida", "temporal"]

if not os.path.exists(base):
    os.mkdir(base)
    print(f"Carpeta '{base}' creada.")

for sub in subcarpetas:
    ruta = os.path.join(base, sub)
    if not os.path.exists(ruta): 
        os.mkdir(ruta)
    print(f"Subcarpeta '{sub}' creada.")

# Crear archivos temporales
for i in range(3):
    ruta_archivo = os.path.join(base, "temporal", f"archivo{i}.tmp")
    with open(ruta_archivo, "w") as f:
        f.write("Este es un archivo temporal. \n")