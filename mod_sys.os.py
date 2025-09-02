import sys 

print("Argumentos recibidos: ")
for i, arg in enumerate(sys.argv):
    print(f"Argumento {i}: {arg}")

respuesta = input("¿Deseas continuar? (s/n): ")
if respuesta.lower() == 's':
    print("Saliendo del programa...")
    sys.exit(0)
print("Continuando...")

for ruta in sys.path:
    print(f"Rutas de busqueda de modulos : ")
    for ruta in sys.path:
        print(f"Ruta: {ruta}")
    print(sys.version)

import os 

directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")
os.chdir('. .')
print(f"El directorio actual es: {directorio_actual}")

archivos = os.listdir("..")
print("Archivos en este directorio: ")
for archivo in archivos:
    print(archivo)  

usuario = os.environ.get('USER') or os.environ.get('USERNAME')
print(f"Usuario actual: {usuario}")

if not os.path.exists("Nueva carpeta"):
    os.mkdir("Nueva carpeta")
    print("Carpeta creada.")
else:
    os.rmdir("Nueva carpeta")
    print("Carpeta eliminada.")
print(os.listdir("."))  

