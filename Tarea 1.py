#Pregunta 1
from math import pi
def pregunta_1 ( radio : float , angulo : float ) -> float :
    r = radio
    o = angulo
    l = r * o * (pi / 180)
    return round(l, 2)

print(pregunta_1 ( 10 , 90 ))
print(pregunta_1 ( 7 , 180 ))
print(pregunta_1 ( 5 , 45 ))
print(pregunta_1 ( 12 , 60 ))
print(pregunta_1 ( 8 , 30 ))

#Pregunta 2
def pregunta_2 (vx: float , vy: float , vz: float )-> float :
    vector = ((vx ** 2)+(vy ** 2)+(vz ** 2))**0.5
    return round(vector, 2)
print(pregunta_2 ( -1 , -2, 0 ))
print(pregunta_2 ( -2 , 5, 1 ))
print(pregunta_2 ( 4 , 8, 3 ))

#Pregunta 3
def pregunta_3 ( edad : int ) -> str :
    if edad < 13:
        return "Menor"
    elif edad >= 13 and edad < 18:
        return "Adolescente"
    elif edad >= 18 and edad < 65:
        return "Adulto"
    else:
        return "Adulto Mayor"

print(pregunta_3(10))
print(pregunta_3(15))
print(pregunta_3(30))
print(pregunta_3(70))

#Pregunta 4
def pregunta_4 ( peso : int , altura : float ) -> str :

    imc = peso / (altura * altura)
    if imc < 18.5:
        return "Bajo peso"
    elif imc >= 18.5 and imc < 25:
        return "Normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

print(pregunta_4 (50, 1.60))
print(pregunta_4 (45, 1.75))
print(pregunta_4 (80, 1.50))
print(pregunta_4 (70, 1.80))