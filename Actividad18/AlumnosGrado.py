
#Crea/Presenta  la forma que creas más conveniente para describir 
#cuántos alumnos hay por grados. 

import pandas as pd

students = students = pd.read_csv("clean_students_complete.csv", index_col=0)
students.drop(students.columns[0], axis=1, inplace=True)

fig1 = students["grade"].value_counts().plot(kind="bar").get_figure()
fig1.savefig("Actividad18\\graficaPorGrado")
