import pandas as pd
import numpy as np

d1={"Nombre" : ["Sofía", "Memo", "Martha", "Alison", "Cosmo", "Wanda"],
   "Edad" : [23 , 38, 35, 23, 46, 42],
   "Salario" : [340.45, 381.23, 453.4, 234, 654, 999.99],
   "Genero" : ["F", "M", "F", "F", "M", "F"]}
data = pd.DataFrame(d1)

print("La diferencia entre el salario más alto y más bajo es: {0}".format(round(data["Salario"].max()-data["Salario"].min(),2)))
print("Los valores estadisticos de los salarios son:\n", data["Salario"].describe())