print("Hola mundo")
nombre = input("Ingresa tu nombre: ")
print("Hola " + nombre + ", como estás?")
estado = input("Ingresa tu estado de ánimo: ")
if estado == "Feliz":
    print("Me alegro por ti!")
if estado == "Triste":
    print("Oh, que pena :C ")
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Eres mayor de edad, ingresa")
if edad < 18:
    print("Eres menor de edad, vuelve cuando tengas +18")