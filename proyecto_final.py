import sys
import os
from datetime import datetime

def log(mensaje):
    with open("log. txt", "a") as f:
        f.write(f"[{datetime.now()}] {mensaje} \n")

if len(sys.argv) < 2:
    print("Uso: python mantenimiento.py <carpeta_base>")
    sys.exit(1)

base = sys.argv[1]
subcarpetas = ["entrada", "salida", "temporal"]

if not os.path.exists(base):
    os.mkdir(base)
    log(f"Carpeta base '{base} ' creada.")

for sub in subcarpetas:
    ruta = os.path.join(base, sub)
    if not os.path.exists(ruta):
        os.mkdir(ruta)
        log (f"Subcarpeta ' {sub}' creada.")

# Eliminar archivos temporales
ruta_temporal = os.path.join(base, "temporal")
for archivo in os.listdir(ruta_temporal) :
    if archivo.endswith(".tmp"):
        ruta = os.path.join(ruta_temporal, archivo)
        os.remove(ruta)
        log(f"Archivo temporal eliminado: {archivo}")
        
print("Mantenimiento completado. Revisa 'log. txt' .")