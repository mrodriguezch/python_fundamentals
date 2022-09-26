import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Velocidades:
    def __init__(self, datos, setpoints):
        """Constructor para datos"""   
        datosCeldas = pd.read_csv("Proyecto\\"+datos)
        self.setpoints = pd.read_csv("Proyecto\\"+setpoints)
        self.entrada = self.getVelocidad(datosCeldas, "Header_Speed", 100)
        self.salida = self.getVelocidad(datosCeldas, "Robot_Speed", 100)
        #renombrar a velocidad
        self.entrada.rename( columns={'Header_Speed' :'Velocidad'}, inplace=True)
        self.salida.rename( columns={'Robot_Speed' :'Velocidad'}, inplace=True)
        
    
    def getVelocidad(self, datos, columna, limite):
        datos = datos[datos[columna].notna()]
        datos = datos.loc[(datos[columna]>limite)]
        datos = datos[["IdCelda", columna]]
        return datos
            
    def printDF(self,df):
        # pandas settings are local to with statement.
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 0,
                                'display.width', 150
                               ):
            print(df)
    
    def getSummary(self):
        summaryEntrada = self.entrada.groupby("IdCelda").median().reset_index()
        summarySalida = self.salida.groupby("IdCelda").median().reset_index()
        
        summaryEntrada["Velocidad"] = round(summaryEntrada["Velocidad"], 0)
        summarySalida["Velocidad"] = round(summarySalida["Velocidad"], 0)
        
        summaryEntrada["Velocidad"] = pd.to_numeric(summaryEntrada["Velocidad"], downcast='signed')
        summarySalida["Velocidad"] = pd.to_numeric(summarySalida["Velocidad"], downcast='signed')
        
        summary = self.setpoints.merge(summaryEntrada, on='IdCelda', how="left").merge(summarySalida, on="IdCelda", how="left", suffixes=(' Inicio', ' Salida'))
        
        print("Concentrado")
        print("=========================================")
        self.printDF(summary)
            
    
    def isValid(self, linea):
        #print ("Valido? ", linea in self.setpoints.IdCelda.unique())
        return linea in self.setpoints.IdCelda.unique()

    def getSetpoint(self, linea):
        setpoint = self.setpoints[self.setpoints["IdCelda"]==linea].Setpoint.squeeze()
        
        print("=========================================")
        print("La velocidad establecida en esta linea es: ", setpoint, " clavos por minuto")
        print("=========================================\n")
        
    def compare(self, linea, opcion):
        entrada = self.entrada[self.entrada["IdCelda"]==linea]["Velocidad"]
        salida = self.salida[self.salida["IdCelda"]==linea]["Velocidad"]
        if opcion == "text":
            e=entrada.describe()
            s=salida.describe()
            print("Velocidad primera maquina")
            print("=========================================")
            self.printDF(e)
            
            print("\nVelocidad última maquina")
            print("=========================================")
            self.printDF(s)
            
        elif opcion == "graf":            
            fig = plt.figure()
            ax = fig.add_subplot(111)

            ax.hist(entrada, bins=10, edgecolor='None', alpha = 0.8, label="entrada")
            ax.hist(salida, bins=10, edgecolor='None', alpha = 0.8, label="salida")

            plt.legend(prop ={'size': 10})
            
            
            print("\nHistograma combinado")
            print("=========================================")
            plt.show()
        else:
            print("Opcion incorrecta. Las opciones disponibles son: text, graf")

#Datos de entrada
velocidades=Velocidades("Datos_Celdas.csv", "SetPoints.csv")

#Instrucciones iniciales
print("===================================================")
print("Ingrese el id de la línea para ver su informacion")
print("Ingrese 'sum' para ver el resumen")
print("Ingrese 0 para salir")
print("===================================================")
while True:

    opcion = str(input("Ingrese la opcion seleccionada: "))

    if opcion == 'sum':
        velocidades.getSummary()
    elif opcion.isnumeric():
        opcion = int(opcion)
        if opcion > 0:
            if velocidades.isValid(opcion):
                velocidades.getSetpoint(opcion)
                velocidades.compare(opcion, "text")
                velocidades.compare(opcion, "graf")
            else:
                print("Línea no disponible para análisis. Use la opcion 'sum' para ver las lineas disponibles.")
        else:
            break
    else:
        print("Opciona no valida.")

