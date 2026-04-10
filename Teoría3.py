# #Función "round"
# numero = 12.58962145
# print(numero)
# print(round(numero, 2))
import math
from pprint import saferepr


#Función "max"
# a = (1, 2, 3, 4, 5, 6, 7, 8)
# print(max(a))

#Función "min"
# a = (1, 2, 3, 4, 5, 6, 7, 8)
# print(min(a))

#Ejercicio 1
# n1 = int(input("n1: "))
# n2 = int(input("n2: "))
# n3 = int(input("n3: "))
# menor = min(n1, n2, n3)
# mayor = max(n1, n2, n3)
# print("El menor es: ", menor)
# print("El mayor es: ", mayor)

#Funciones matemáticas
#Raiz

#Ejercicio 2:
# from math import sqrt
#
# numero = float(input("Número: "))
# raiz = sqrt(numero)
# print("La raiz cuadrada es: ", raiz)

#Ejercicio 3: Creando nuestra propia funcion, a diferencia de laboratorio 2 (Ejercicio 4)
# from math import sqrt
# def hallarDistancia(x1 , y1 , x2 , y2):
#     d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
#     return d
#
# x1 = float(input("Ingrese el primer punto en el eje x: "))
# x2 = float(input("Ingrese el segundo punto en el eje x: "))
# y1 = float(input("Ingrese el primer punto en el eje y: "))
# y2 = float(input("Ingrese el segundo punto en el eje y: "))
#
# distancia = hallarDistancia(x1 , y1 , x2 , y2)
# print("""La distancia entre el punto "P" y "Q" es: """, round(distancia, 2))

#Ejercicio 4:
# def sumarDigitos(n):
#     u = numero % 10
#     d = numero // 10 % 10
#     c = numero // 100 % 10
#     m = numero // 1000
#     s = u + d + c + m
#     return s
#
# numero = int(input("Ingrese un numero: "))
# print("La suma de los dígitos es: ", sumarDigitos(numero))
#
# def invertirDigitos(numerito):
#     u = numero % 10
#     d = numero // 10 % 10
#     c = numero // 100 % 10
#     m = numero // 1000
#     ni = u * 1000 + d * 100 + c * 10 + m
#     return ni
#
# numeroparainv = int(input("Ingrese un numero para invertirlo: "))
# print("El número invertido es: ", invertirDigitos(numeroparainv))

#Ejercicio 5: (Usando el if, elif, else)

# def analizaNumero(numero):
#     if numero % 2 == 0:
#         return "El número es par"
#     else:
#         return "El número es impar"
#
# numero = int(input("Número: "))
# print(analizaNumero(numero))

#Ejercicio 6:

# def analizarNumero(numero):
#     if numero == 0:
#         return "El número es 0"
#     elif numero > 0:
#         return "El número es positivo"
#     else:
#         return "El numero es negativo"
#
# numero = int(input("Número: "))
# print( analizarNumero(numero) )