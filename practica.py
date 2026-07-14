#Clase 1 Imprimir frase
print("Aguante River")

#Clase 2 Almacenamiento de datos en variables

nombre = str(input("Ingrese su nombre: "))

apellido = str(input("Ingrese su apellido: "))

edad = int(input("Ingrese su edad: "))

correo = str(input("Ingrese su correo electronico: ").strip())

#Clasificacion de la persona por rango etario

if edad < 15:
    categoria = "Niño/a"
elif edad <= 18:
    categoria = "Adolescente"
else:
    categoria = "Adulto/a"

#Clase 3 Comprobacion de errores con condicionales

if (nombre == ("") or apellido == ("") or edad < 18 or correo.count("@") != 1 or " " in correo):    #Clase 4 Validacion de variables entre ellas correo con un @
    print("ERROR!")
else: 
        print("---Tarjeta de Presentacion---")      #Clase 2 Muestreo en forma de tarjeta de presentacion
        print("Nombre completo:", nombre.title(), apellido.title())     #Clase 4 Formateo de nombre y apellido
        print("Edad:", edad, "años")
        print(f"u rango etario es: {categoria}")    #Clase 4 Uso de f-Strings
        print(f"Correo electronico: {correo}")










