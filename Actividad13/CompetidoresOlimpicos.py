import pandas as pd
import numpy as np

print("="*50,"\nBásica\n","="*50)
print("="*50)

datos1 = pd.read_csv("athlete_events.csv")
#Crear un programa en Visual Studio que me permita saber cuál es el competidor más veterano que ha recibido medalla (oro, plata o bronce)
medallistas=datos1[datos1["Medal"].notna()]
veterano = medallistas["Age"].max()
print("El medallista más veterano es:\n", medallistas[medallistas["Age"] == veterano]["Name"])

print("="*50)
#Crear un programa en Visual Studio que me permita saber cuál es el competidor más joven que ha recibido medalla de oro
oros=datos1[datos1["Medal"]=="Gold"]
novato = oros["Age"].min()
oros[oros["Age"] == novato]
print("El medallista más joven con oro es:\n", oros[oros["Age"] == novato]["Name"])

#Encuentra al competidor más ganador de la historia y crea un csv con toda su información.
ganador = medallistas.groupby(["Name"]).count().sort_values(["Medal"], ascending=False).head(1)
ganador.to_csv("Actividad13\\MasGanador.csv", header=True, index=True)
print(ganador)