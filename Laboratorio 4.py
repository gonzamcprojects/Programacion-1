#Ejercicio 1:
# def verificarNota (nota):
#     if nota >= 10.5 :
#         return "Aprobó"
#     else:
#         return "No abrobó"
#
# x = float(input("Digite la nota del alumno: "))
# print(verificarNota(x))

#Ejercicio 2:
# def verificarEstacion (estacion):
#     if estacion == 1:
#         return "Verano"
#     if estacion == 2:
#         return "Otoño"
#     if estacion == 3:
#         return "Invierno"
#     if estacion == 4:
#         return "Primavera"
#     else:
#         return "No corresponde"
#
# estacion = int(input("Ingrese el número de la estacion (1 al 4): "))
# print(verificarEstacion(estacion))

#Ejercicio 3
# def verificarEdad (edad):
#     if edad >= 0 and edad <= 17:
#         return "15 soles"
#     if edad >= 18 and edad <= 30:
#         return "25 soles"
#     if edad >= 31 and edad <= 45:
#         return "30 soles"
#     else:
#         return "10 soles"
#
# edad = int(input("Ingrese edad: "))
# print(verificarEdad(edad))

#Ejercicio 4
# def verificarDenominacion (denominacion: int):
#     if denominacion == 1:
#         return "George Washington"
#     if denominacion == 2:
#         return "Thomas Jefferson"
#     if denominacion == 5:
#         return "Abraham Lincoln"
#     if denominacion == 10:
#         return "Alexander Hamilton"
#     if denominacion == 20:
#         return "Andrew Jackson"
#     if denominacion == 50:
#         return "Ulysses S. Grant"
#     if denominacion == 100:
#         return "Benjamin Franklin"
#     if denominacion == 500 or denominacion == 1000 or denominacion == 5000 or denominacion == 10000:
#         return "Denominacion descontinuada"
#     else:
#         return "No existe esa denominacion"
#
# x = int(input("Ingrese la denominacion: "))
# print(verificarDenominacion(x))

#Ejercicio 5:
# def verificarLongDeOnda(longitud):
#     if longitud >= 380 and longitud<= 427:
#         return "Violeta"
#     if longitud >= 427 and longitud<= 476:
#         return "Azul"
#     if longitud >= 477 and longitud<= 497:
#         return "Cian"
#     if longitud >= 498 and longitud<= 570:
#         return "Verde"
#     if longitud >= 571 and longitud<= 581:
#         return "Amarillo"
#     if longitud >= 582 and longitud<= 618:
#         return "Naranja"
#     if longitud >= 619 and longitud<= 780:
#         return "Rojo"
#     else:
#         return "No corresponde al espectro visible"
#
# x = int(input("Ingrese el valor de la longitud: "))
# print(verificarLongDeOnda(x))

#Ejercicio 6:
# def verificacionDeMonedasyBilletes (monybilletes):
#     if monybilletes == 1 or monybilletes == 2 or monybilletes == 5:
#         return "Es una moneda"
#     if monybilletes == 10:
#         return "Es un billete y aparece Machu Picchu"
#     if monybilletes == 20:
#         return "Es un billete y aparece la Ciudad de Chan Chan"
#     if monybilletes == 50:
#         return "Es un billete y aparece el templo de Chavin de Huantar"
#     if monybilletes == 100:
#         return "Es un billete y aparece el sitio Arqueologico del Gran Pajaten"
#     if monybilletes == 200:
#         return "Es un billete y aparece la Ciudad Sagrada de Caral"
#     else:
#         return "La denominación no existe"
#
# x = int(input("Ingrese el dinero en soles: "))
# print(verificacionDeMonedasyBilletes(x))

#Ejercicio 7:
# def verificarAñoBisiesto (anobis):
#     if anobis % 4 == 0 and anobis % 100 != 0 or anobis % 400 == 0:
#         return "Es año bisiesto"
#     else:
#         return "No es bisiesto"
#
# x = int(input("Ingrese el año: "))
# print(verificarAñoBisiesto(x))

#(SEGUNDA SOLUCIÓN, AGREGANDO UN IF MAS)
# def verificarAñoBisiesto (anobis):
#     if anobis % 4 == 0 and anobis % 100 != 0:
#         return "Es año bisiesto"
#     if anobis % 400 == 0:
#         return "Es año bisiesto"
#     else:
#         return "No es bisiesto"
#
# x = int(input("Ingrese el año: "))
# print(verificarAñoBisiesto(x))

#Ejercicio 8:
# from datetime import date
# def dia_semana(dia, mes):
#     año = 2026
#     fecha = date(año, mes, dia)
#     num = fecha.weekday()
#
#     if num == 0:
#         return "lunes"
#     if num == 1:
#         return "martes"
#     if num == 2:
#         return "miercoles"
#     if num == 3:
#         return "jueves"
#     if num == 4:
#         return "viernes"
#     if num == 5:
#         return "sabado"
#     else:
#         return "domingo"
#
# x = int(input("Escriba el día: "))
# y = int(input("Escriba el mes: "))
# print(dia_semana(x, y))

# (SOLUCIÓN 2, USANDO DÍAS ACUMULADOS)
#
# def dia_semana(dia, mes):
#
#     # Días por mes en 2026 (no es bisiesto)
#     if mes == 1:
#         dias_acumulados = 0
#     elif mes == 2:
#         dias_acumulados = 31
#     elif mes == 3:
#         dias_acumulados = 59
#     elif mes == 4:
#         dias_acumulados = 90
#     elif mes == 5:
#         dias_acumulados = 120
#     elif mes == 6:
#         dias_acumulados = 151
#     elif mes == 7:
#         dias_acumulados = 181
#     elif mes == 8:
#         dias_acumulados = 212
#     elif mes == 9:
#         dias_acumulados = 243
#     elif mes == 10:
#         dias_acumulados = 273
#     elif mes == 11:
#         dias_acumulados = 304
#     else:
#         dias_acumulados = 334
#
#     # 1 de enero de 2026 fue jueves (3)
#     total_dias = dias_acumulados + dia - 1
#     num = (3 + total_dias) % 7
#
#     if num == 0:
#         return "lunes"
#     elif num == 1:
#         return "martes"
#     elif num == 2:
#         return "miercoles"
#     elif num == 3:
#         return "jueves"
#     elif num == 4:
#         return "viernes"
#     elif num == 5:
#         return "sabado"
#     else:
#         return "domingo"
#
# # Ejemplo
# x = int(input("Ingrese el día: "))
# y = int(input("Ingrese el mes: "))
# print(dia_semana(x, y))