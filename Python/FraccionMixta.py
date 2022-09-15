N=int(input("Valor del numerador:"))
D=int(input("Valor del denominador"))

if N%D!=0:
    print(f"{int(N/D)} {N%D}/{D}")
else:
    print(int(N/D))
