from time import localtime
 
def calcular_edad(dia_nacimiento, mes_nacimiento, anno_nacimiento):
    t = localtime()
    dia_actual = t.tm_mday
    mes_actual = t.tm_mon
    anno_actual = t.tm_year
 
    edad = anno_actual - anno_nacimiento
 
    if (mes_actual < mes_nacimiento) or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
        edad -= 1
 
    return edad
 
def evaluar(dia, mes, anno):
    edad = calcular_edad(dia, mes, anno)
    return f"Usted tiene {edad} años"
if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
