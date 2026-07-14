#Clase 7 Lista ordenada metodo append y remove

nombres = []
entradas = 0
nombre = str

print("Escriba 'Fin' para salir")

while nombre != "fin":

    nombre = input(f"Ingresá el nombre {entradas + 1}: ").strip()

    if nombre == "":
        print("ERROR! COMPLETÁ EL CAMPO")
        continue
  
    nombres.append(nombre.title())
    entradas += 1


nombres.sort()
nombres.remove("Fin")

print("Lista ordenada de clientes:")
for nombre in nombres:
    print(nombre)







#Clase 8 Diccionarios

productos = {}

while True:
    nombre = input("Ingrese el nombre del producto: ")

    precio = float(input("Ingrese el precio del producto: "))

    productos[nombre] = precio

    print("Los productos son: \n")
    print(productos)

    continuar = input("Desea continuar: (s/n)")

    if continuar == "n":
        break
    
    while continuar == "":
        input("Desea continuar: (s/n)")
