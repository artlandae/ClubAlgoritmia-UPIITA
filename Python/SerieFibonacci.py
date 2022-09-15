tamano=int(input(f"Cantidad de sucesiones que desea obtener de la serie de Fibonacci: "))
fibonacci=[0]*(tamano+2)
fibonacci[0]=0
fibonacci[1]=1

for i in range(tamano):
    fibonacci[i+2]=fibonacci[i]+fibonacci[i+1]

print(fibonacci)
