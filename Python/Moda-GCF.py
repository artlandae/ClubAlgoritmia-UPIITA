cantidad=int(input("Cantidad de muestras: "))
numeros=[]

for i in range(cantidad):    
    numeros.append(int(input(f"numero :")))

diccionario = {}
for i in numeros:    
    diccionario.setdefault(i,0)
    diccionario[i]+=1

mayor=0
for key in diccionario:
    if mayor<diccionario.get(key):
        mayor=key

print(mayor)