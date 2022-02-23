https://haveibeenpwned.com/
candidatas = ["baseball","football","shadow","mustang","superman","jordan","soccer"]
import hashlib
def obtener_hash(password):
    encoded=password.encode()
    resumen=hashlib.sha256(encoded)
    return resumen.hexdigest()
nombreFichero = input("Introduce le nombre del fichero:")
fichero = open(nombreFichero, "r")
linea = fichero.read()
while linea:
    print(linea)
    linea = fichero.read()
else:
    fichero.close()

