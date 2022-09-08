#actividad básica
diccionario = {"Ale":34,"Beto":5,"Jose":-9,"Roberto":12,"Nelson":24}
for i,j in diccionario.items():
    print("{0} dijo: {1}".format(i,j))
print("el número más grande es {0}".format(max(diccionario.values())))
print("el número más pequeño es {0}".format(min(diccionario.values())))