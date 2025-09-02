import os
import subprocess

host = "google.com"
respuesta = os.system(f"ping -c 4 + {host})")
if respuesta == 0:
    print(f"{host} está accesible")
else:
    print(f"No se pudo acceder a {host}")


os.system('ipconfig')
os.system('route print')
os.system('netstat -an')


resultado = subprocess.run('ping', 'google.com', 'n', '-2')

host = "scamme.nmap.org"
resultado = subprocess.run(["nmap","-p", "80,443", host])
print(resultado.stdout)

