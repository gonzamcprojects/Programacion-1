# False = 0
# True = 1
from unicodedata import digit

# Ejercicio 1
# edad = int(input("Digite su edad: "))
#
# es_mayor = edad >= 18
# es_menor = not es_mayor
#
# print("Es mayor de edad" * es_mayor)
# print("Es menor de edad" * es_menor)


# Ejercicio 2
# consumo = float(input("Ingrese el consumo eléctrico de la persona: "))
#
# es_menor = consumo <= 100
# es_mayor = not es_menor
#
# kWmenor = consumo * 0.4522
# kWmayor = 100 * 0.4522 + (consumo - 100) * 0.7
#
# print("El monto a pagar es: ", es_menor * kWmenor + es_mayor * kWmayor)


# Ejercicio 3
# numero = int(input("Ingrese un numero par o impar: "))
# par = numero % 2 == 0
# impar = not par
#
# print("El numero es par " * par)
# print("El numero es impar " * impar)


# Ejercicio 4
# s1 = int(input("Ingrese el valor del lado 1: "))
# s2 = int(input("Ingrese el valor del lado 2: "))
# s3 = int(input("Ingrese el valor del lado 3: "))
#
# operacion = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)
# no_operacion = not operacion
#
# print("El triángulo es válido " * operacion)
# print("El triángulo no es válido " * no_operacion)


# Ejercicio 5
# consumo = float (input("Ingrese el valor del consumo: "))
#
# propina = 0.05
# igv = 0.18
#
# monto_pagar = consumo * (propina + igv) + consumo
# print("El monto pagar es: ", monto_pagar)


# Ejercicio 6
# botella1l = int(input("Ingrese el valor de las botellas de 1 l: "))
# botellamasde1l= int(input("Ingrese el valor de las botellas de mas de 1 l: "))
#
# pago_1l = botella1l * 1.25
# pago_masde1l = botellamasde1l * 3.75
#
# pago_total = pago_1l + pago_masde1l
# print("El pago total por las botellas es: ", pago_total, " soles")


# Ejercicio 7
# numero = int(input("Ingrese un numero entero de 4 dígitos: "))
# uni = numero // 1000
# dec = (numero % 1000) // 100
# cent = (numero % 100) // 10
# mil = numero % 10
#
# suma = uni + dec + cent + mil
# print(uni, "+",dec, "+", cent, "+", mil, "=", suma)


# Ejercicio 8
# num = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))
# num3 = int(input("Ingrese otro numero: "))
#
# pequeno = (min(num,num2,num3))
# mayor = (max(num,num2,num3))
# mediano = (num + num2 + num3) - (mayor + pequeno)
#
# print(pequeno, mediano, mayor)