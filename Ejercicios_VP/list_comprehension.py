lista = [numero for numero in 
            [numero**2 for numero in range(0,11)] 
                if numero % 2 == 0 ]
print(lista)

lista2 = [(numero**2, numero) for numero in range(0,11) if numero%2 == 0]
print(lista2)

print(type(lista2[0]))