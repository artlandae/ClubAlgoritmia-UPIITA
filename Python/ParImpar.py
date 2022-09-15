
N=int(input("Valor de N: "))
a=int(input("Valor de a: "))
b=int(input("Valor de b: "))

while N<=1000:
    if (N%2)==0:
        for j in range(a):
            N+=j
    else:
        for h in range(a):
            N+=h

print(N)

