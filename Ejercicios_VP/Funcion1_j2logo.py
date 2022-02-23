'''def cuadrado_de_par(numero):
    if not numero % 2 == 0:
       return
    else:
        print(numero ** 2)

cuadrado_de_par(10)

cuadrado_de_par(5)

print("===============================================")

def cuadrado_y_cubo(n):
    return n ** 2, n ** 3

cuad, cubo = cuadrado_y_cubo(4)
print(cuad, type(cuad))
print(cubo, type(cubo))
print("===============================================")

def saludo(nombre):
    print(f'Hola {nombre}')

saludo('j2logo')'''
print("===============================================")
'''def doblar_valor(numero):
  return (numero * 2)

n = 10
doblar_valor(n)
print(n)
print("===============================================")
def inmutable(string):
    return print(string*2)

string = "Soy yo"
inmutable(string)
print(string)'''
def doblar_valor(numero):
    return(numero * 2)
#n = doblar_valor(10)
n = 20
print(f"El valor de n es {doblar_valor(n)}") #El valor de n es 20, se ha ejecutado la función con argumento 10
print("Ahora n es.....")
print(doblar_valor(n)) #Ejecuta la función con el valor de 20, resultando 40
print("Imprime el valor de n")
print(n) #n vuelve a ser 20
