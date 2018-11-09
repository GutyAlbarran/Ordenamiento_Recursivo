__author__='Agustin Albarran Delgado'

n=int(input("ingresar cantidad de numeros a ingresar: "))
A=[0 for i in range(n)]
#bucle for para ingresar valores de la matriz
for i in range(n):
    A[i]=int(input("ingresar valor: "))
#2 bucles for
for i in range(n-1):
    for j in range(n-1):
        if(A[j]>A[j+1]):
            aux=A[j]
            A[j]=A[j+1]
            A[j+1]=aux
#bucle for pra ordenar
print("ORDENAR DE MAYOR A MENOR...")
for i in range (n):
    print(A[i])