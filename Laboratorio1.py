print("Hola mundo")
nombre = input("Ingresa tu nombre: ")

print("Hola " + nombre + ", como estás?")
estado = input("Ingresa tu estado: ")
if estado == "Feliz":
    print("Me alegro por ti")
if estado == "Triste":
    print("Todo va a mejorar")

edad = int(input("Ingresa tu edad: "))
print("Tienes ", edad, " años")
print("En 10 años tendrás: ", (edad + 10) )

edad = 34
#edad = int( input("Edad: "))
num = 0b1011
print(num, bin(num) )
num = 0x019AF
print(num, hex(num))

# float = Almacenar números decimales
peso = 34.56
#peso = float (input("Peso: "))

# bool = Almacenar verdadero o falso
bandera = True
es_mayor_edad = edad >= 18
resp = bool("")
print("Resp: ", resp)

# str = "String" (Sirve para guardar texto)
# cad = Variable donde se almacena el texto
cad = "Hola \"mundo\" como están"
print( cad )
cad = "Hola mundo como \'están\'"
print( cad )
cad = "Hola \n mundo como estan"
print( cad )
cad = """Hola
mundo "como"
'estan' """
print( cad )

# Adelanto de cadenas usando "len"
cad = "Hola mundo"
len( cad )
print( cad[5] )

#operadores matemáticos
print("Suma:", 17 + 3)
print("Resta:", 17 - 3)
print("Multiplicación:", 17 * 3)
print("División:", 17 / 3)
print("División entera:", 17 // 3)
print("Módulo (residuo):", 17 % 3)
print("Potencia:", 17 ** 3)

# Ejercicio 1
import math
radio = float(input("Ingrese el radio de la esfera: "))

area = 4 * math.pi * radio ** 2
volumen = 4 / 3 * math.pi * radio ** 3

print("El volumen:", volumen)
print("El area:", area)

# Ejercicio 2
soles = float(input("Ingrese el monto en soles: "))

dolares = soles / 3.46
euros = soles / 4.01

print ("El cambio en dolares es:", dolares)
print ("El cambio en euros es:", euros)

#Ejercicio 3
