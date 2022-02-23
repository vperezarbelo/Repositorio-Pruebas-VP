#funcion copiar fichero
def copiar_texto_fichero (fichero_origen, fichero_destino)
    with open(fichero_origen, "r", encoding="UTF-8") as origen
    contenido_origen = origen.read()
    with open(fichero_destino, "w", encoding="UTF-8") as destino
    destino.write(contenido_origen)
    return fichero_destino


