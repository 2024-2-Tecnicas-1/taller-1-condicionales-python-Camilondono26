def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    return evaluar_triangulo(a, b, c)
 
def es_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a
 
def determinar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "El triángulo es equilátero"
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles"
    else:
        return "El triángulo es escaleno"
 
def evaluar_triangulo(a, b, c):
    if es_triangulo(a, b, c):
        return determinar_tipo_triangulo(a, b, c)
    else:
        return "No es un triángulo válido"

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
