a = []
b = []
cantidad = int(input(f"Ingresa el tamaño de los vectores: "))
for i in range(cantidad):
    # Recuerda que range comenzará desde 0, así que imprimimos el número solicitado pero + 1
    numero = input(f"Ingresa el número {i + 1} del vector a: ")
    # Convertir a entero, pues input regresa una cadena
    numero = int(numero)
    # Lo agregamos al arreglo con append
    a.append(numero) 

for i in range(cantidad):
    # Recuerda que range comenzará desde 0, así que imprimimos el número solicitado pero + 1
    numero = input(f"Ingresa el número {i + 1} del vector b: ")
    # Convertir a entero, pues input regresa una cadena
    numero = int(numero)
    # Lo agregamos al arreglo con append
    b.append(numero) 

print(a,b)

productoPunto=[0]*cantidad
for i in range(cantidad):
    productoPunto[i]=a[i]*b[i]

print(sum(productoPunto))