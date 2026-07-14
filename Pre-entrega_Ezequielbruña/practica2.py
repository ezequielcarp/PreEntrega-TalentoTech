#Clase 5 Registro de ingresos mensuales utilizando ciclo while devolviendo el total y su promedio

mes = 1
ingreso_total = 0

while  mes <= 6: 
    ingreso = int(input(f"Ingreso del mes {mes}: $"))

    if ingreso > 0:
        ingreso_total += ingreso
        mes += 1
    else:
        print("Ingrese valores positivos")



print(f"Total acumulado en 6 meses: ${ingreso_total}")
print(f"Promedio mensual: ${ingreso_total // 6}")

#Clase 6 Limpiar y mostrar lista de nombres
print("--------------------------------------")
print("Clase 6 Lista de nombres")

nombres = ["MATEO", "Valentina", "AlEjAnDro", "", " DIEGO", "SOFia", "Lucas ", " ", "Javier", "Martina"]

nombres_validos = 0
num = 1

for nombre in nombres:
    if nombre.strip() == "":
        continue

    nombre_corregido = nombre.strip().title()
    print(f"Nombre valido {num}: {nombre_corregido}")
    num +=1
    nombres_validos += 1

print(f"Total de nombres validos: {nombres_validos}")





