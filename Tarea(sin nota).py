#Pregunta 1
def pregunta_1(arista:  float) -> float:
    volumen = 1/4 * (15 + 7 * (5 ** 0.5)) * arista ** 3
    return round(volumen, 3)

print(pregunta_1(7.5))
print(pregunta_1(12.0))
print(pregunta_1(8.0))

#Pregunta 2
def pregunta_2(lado1: float, lado2: float, lado3: float, lado4:float) ->float:
    s = (lado1 + lado2 + lado3 + lado4) / 2
    area = ((s - lado1) * (s - lado2) * (s - lado3) * (s - lado4)) ** 0.5
    return round(area, 3)

print(pregunta_2(23, 25, 27, 29))
print(pregunta_2(4, 6, 5, 9))
print(pregunta_2(10, 10, 10, 10))

#Pregunta 3
def pregunta_3(numero : int)->str:
    unidades = numero % 10

    numero = numero // 10
    decenas = numero % 10

    numero = numero // 10
    centenas = numero % 10
    if unidades == decenas == centenas:
        return "Tiene tres digitos iguales"
    elif unidades == decenas or unidades == centenas or decenas == centenas:
        return "Tiene solo dos digitos iguales"
    else:
        return "Tiene tres digitos diferentes"

print(pregunta_3(335))
print(pregunta_3(333))
print(pregunta_3(112))
print(pregunta_3(466))
print(pregunta_3(124))

#Pregunta 4
def pregunta_4( rango :  int) -> str:
    if rango <= 69:
        return "Deficiente"
    elif rango >= 70 and rango <= 79:
        return "Inferior"
    elif rango >= 80 and rango <= 89:
        return "Abajo del Promedio"
    elif rango >= 90 and rango <= 109:
        return "Promedio"
    elif rango >= 110 and rango <= 119:
        return "Arriba del Promedio"
    elif rango >= 120 and rango <= 129:
        return "Superior"
    elif rango >= 130:
        return "Muy Superior"

print(pregunta_4(66))
print(pregunta_4(109))
print(pregunta_4(118))
print(pregunta_4(133))
print(pregunta_4(75))