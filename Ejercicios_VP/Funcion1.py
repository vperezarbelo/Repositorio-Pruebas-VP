def cuadrado_de_par(numero):
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
