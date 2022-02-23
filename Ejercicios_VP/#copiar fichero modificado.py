#copiar fichero modificado
def escribir_fichero_texto(nombre_fichero, texto):
    with open(nombre_fichero,"w",encoding="UTF-8") as fichero:
        fichero.write(texto)

def leer_fichero_texto(nombre_fichero):
    with open(nombre_fichero, "r", encoding="UTF-8") as fichero:
        contenido = fichero.read()
    return contenido

def copiar_fichero_texto(fichero_origen, fichero_destino):
    contenido = leer_fichero_texto(fichero_origen)
    escribir_fichero_texto(fichero_destino, contenido)

#Copiar un fichero convertido el contenido a maýusculas o a minúsculas
def copiar_fichero_texto_convertido(fichero_origen, fichero_destino, accion):
    leer_fichero_texto(fichero_origen)
    if accion = 1:
        #probar este método
        contenido_o = contenido.upper()
        #probar este metodo
    elif accion = 2:
        contenido_o = contenido.lower()
    else:
        continue
    escribir_fichero_texto(nombre_fichero, contenido_o)


    



#escribir_fichero_texto("juanluis.txt","Esto es el contenido del fichero de Juan Luis.\nLeña y cáspitas")
#todo_el_contenido = leer_fichero_texto("juanluis.txt")
#print(todo_el_contenido)
copiar_fichero_texto("juanluis.txt","copia_jl.txt")
