def evaluar(numero1, numero2, numero3, numero4):
    # TODO: Coloca aquí el código del ejercicio 5: Ordenamiento
    numeros = [numero1, numero2, numero3, numero4]
    n = len(numeros)
    intercambio = True
 
    while intercambio:
        intercambio = False
        for i in range(n - 1):
            if numeros[i] > numeros[i + 1]:
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                intercambio = True
    respuesta = ' '.join(map(str, numeros))
    return respuesta

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
