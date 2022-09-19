import pandas as pd
import numpy as np

datos1 = pd.read_csv("athlete_events.csv")
paisesMedallistas = datos1[datos1["Medal"].notna()]
podio=paisesMedallistas["NOC"].value_counts().head(10)

fig1 = podio.plot(kind="bar").get_figure()
fig1.savefig("Actividad16\\paisesMedallistas")
