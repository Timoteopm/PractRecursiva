Author = 'Timoteo'

a = [7, 5, 3, 1]
print(a)

def ordenarArreglo(arreglo):
        if (len(arreglo) == 1):
            return a[3], a[2], a[0], a[1]
        else:
            for x in range(len(arreglo)):
                if (arreglo[0] > arreglo[(x + 1)]):
                    temp = arreglo[1]
                    arreglo[1] = arreglo[x]
                    arreglo[x] = temp
                    return ordenarArreglo(arreglo[1:])



print(ordenarArreglo(a))