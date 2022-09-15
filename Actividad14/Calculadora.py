class Calculadora():
    """"""
    def setValores(self, a, b, operador):
        """"""
        self.a = a
        self.b = b
        self.operador = operador
    
    def getResultado(self):
        """"""
        if self.operador == '-':
            return self.a-self.b
        elif self.operador == '+':
            return self.a+self.b
        elif self.operador == 'x':
            return self.a*self.b
        elif self.operador == '/':
            return self.a/self.b
        else:
            return None

calculadora = Calculadora();
while True:
    a=float(input("Ingrese el numero: "))
    operador = input("Ingrese el operador (-,+,x,/): ")
    b=float(input("Ingrese el numero: "))

    calculadora.setValores(a,b,operador)
    print("Resultado: ", calculadora.getResultado())

    continuar = input("Presione c+Enter para continuar o Enter para salir: ")
    if continuar != "c":
        break