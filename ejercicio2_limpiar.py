import os

ruta_temporal = os.path.join("proyecto_demo", "temporal")

for archivo in os.listdir(ruta_temporal) :
    if archivo.endswith(".tmp"):
        ruta = os.path.join(ruta_temporal, archivo)
        os.remove(ruta)
        print(f"Eliminado: {archivo}")