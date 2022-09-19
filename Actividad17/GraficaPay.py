import pandas as pd
import numpy as np

datos1 = pd.read_csv("athlete_events.csv")
año=datos1["Year"].max()

paisesMedallistas = datos1[datos1["Medal"].notna()][datos1["Year"]==datos1["Year"].max()]
podio=paisesMedallistas["NOC"].value_counts().head(10).sort_values(ascending=True)

fig1 = podio.plot(kind="bar").get_figure()
fig1.savefig("Actividad17\\graficaPay")