class Transferencia:
    #ATRIBUTOS ESTÁTICOS
    COMISION = 0.01

    #CONSTRUCTOR / ATRIBUTOS DE INSTANCIA
    def __init__(self, cco, ccd, importe, emisor, receptor):
        self.cco = str(cco)
        self.ccd = str(ccd)
        self.importe = int(importe)
        self.emisor = str(emisor)
        self.receptor = str(receptor)

    #METODOS
    #Calcular comisión
    def calcular_comision(self):
        comision = self.importe * COMISION 
    def mostrar_datos(self):
        print(f" EMISOR: {self.emisor}. RECEPTOR: {self.emisor}. IMPORTE: {self.importe}. COMISION: {comision}")
    def generar_pdf(self):
        pass
Transferencia.mostrar_datos(a, b)

