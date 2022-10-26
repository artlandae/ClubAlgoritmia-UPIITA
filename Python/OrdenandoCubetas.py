N = int(input(f"Cantidad de pelotas: "))
M = int(input(f"Cantidad de colores: "))
pelotas=[]
for i in range(N):
    pelotas.append(int(input(f"Colores: ")))
salida=[]
contador=0
for i in range(M):
    for j in range(N):
        if pelotas[j]==i+1:
            contador+=1
    salida.append(contador)
    contador=0

for i in range(M):
    print(i+1,": ",salida[i])

        
