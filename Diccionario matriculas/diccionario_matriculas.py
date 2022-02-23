matricula1 = ["SEAT", "ibiza", "negro"]
matricula2 = ["AUDI", "Q5", "azul"]
matricula3 = ["BMW", "A3", "blanco"]
vehiculos = {"6677jkz":matricula1, "8899hbc":matricula2, "3399bwc":matricula3}
matricula = input("Dime una matricula: ")
if matricula in vehiculos:
    print ("El vehiculo es", vehiculos[matricula])
else:
    print("no tengo este vehículo")