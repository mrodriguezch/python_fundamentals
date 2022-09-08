#actividad básica
print("="*50,"\nBásica\n","="*50)

diccionario = {"Ale":34,"Beto":5,"Jose":-9,"Roberto":12,"Nelson":24}

for i,j in diccionario.items():
    print("{0} dijo: {1}".format(i,j))
    
print("el número más grande es {0}".format(max(diccionario.values())))
print("el número más pequeño es {0}".format(min(diccionario.values())))

#actividad avanzada
print("="*50,"\nAvanzada\n","="*50)

import numpy as np

nombres=["Ale","Beto","Jose","Roberto","Nelson"]
diccionario=dict.fromkeys(nombres)

for n in nombres:
    diccionario[n] = np.random.randint(1000)

min=list(diccionario.values())[0]
max=list(diccionario.values())[0]

for i,j in diccionario.items():
    print("{0} dijo: {1}".format(i,j))
    if max<j:
        max=j
    if min>j:
        min=j

print("el número más grande es {0}".format(max))
print("el número más pequeño es {0}".format(min))