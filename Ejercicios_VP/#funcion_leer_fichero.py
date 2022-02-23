#funcion_leer_fichero
def leer_fichero_texto(nombre_fichero):
    open(nombre_fichero, "r", encoding="UTF-8")
    contenido = nombre_fichero.read()
    return contenido


