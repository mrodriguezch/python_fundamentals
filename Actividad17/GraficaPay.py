import pandas as pd
import numpy as np

datos1 = pd.read_csv("athlete_events.csv")
año=datos1["Year"].max()

paisesMedallistas = datos1[datos1["Medal"].notna()]

olimpics = paisesMedallistas[["Year","Season","Medal","NOC"]]#dataframe solo con las columnas seleccionadas
dummies=pd.get_dummies(olimpics["Medal"])#pivot de valores distintos 

concatenado=pd.concat([olimpics,dummies], axis=1) #concatenacion de 2 datasets en el eje x (axis=1)
lastYear=concatenado[concatenado["Year"]==año]

agrupadoLY=lastYear.groupby(["Medal", "Season"]).sum()#agrupamiento, cada columna es un nivel
agrupadoLY["Total_Medals"]=agrupadoLY["Bronze"]+agrupadoLY["Silver"]+agrupadoLY["Gold"]

nombres=["Bronze", "Gold", "Silver"]
pie3=agrupadoLY["Total_Medals"][:3].plot.pie(figsize=(10,8), labels=nombres, autopct="%0.1f%%")

fig1 = pie3.get_figure()
fig1.savefig("Actividad17\\graficaPay")
print(agrupadoLY)