#Preguntar el nombre 
nombre = input("Por favor, ingresa tu nombre: ")
print("Hola", nombre, ", bienvenido al sistema de vuelos de Volaris.")
#Destinos disponibles y sus precios
print("Destinos disponibles:")
print("1. Ciudad de México - Precio: 1200 pesos")
print("2. Guadalajara - Precio: 1000 pesos")
print("3. Monterrey - Precio: 1500 pesos")
print("4. Cancún - Precio: 1800 pesos")
print("5. Tijuana - Precio: 1300 pesos")
TUA = 200  
ejecutar = True
while ejecutar:
    destino = int(input("Selecciona tu destino escribiendo el número que corresponda (1-5): "))
    if destino == 1:
        precio_base = 1200
        ciudad = "Ciudad de México"
    elif destino == 2:
        precio_base = 1000
        ciudad = "Guadalajara"
    elif destino == 3:
        precio_base = 1500
        ciudad = "Monterrey"
    elif destino == 4:
        precio_base = 1800
        ciudad = "Cancún"
    elif destino == 5:
        precio_base = 1300
        ciudad = "Tijuana"
    else:
        print("Destino no válido. El programa ha terminado.")
        ejecutar = False
        break
# Selección de tipo de equipaje
    print("Selecciona el tipo de equipaje:")
    print("1. Equipaje pequeño (incluido en el precio base)")
    print("2. Equipaje grande (añade 500 pesos)")
    equipaje = int(input("Elige una opción escribiendo el número que corresponda (1 o 2): "))
    if equipaje == 1:
        costo_equipaje = 0
        tipo_equipaje = "pequeño"
    elif equipaje == 2:
        costo_equipaje = 500
        tipo_equipaje = "grande"
    else:
        print("Opción de equipaje no válida. El programa ha terminado.")
        ejecutar = False
        break
# Aplicar descuento
    print("¿Tienes un código de descuento?")
    respuesta_descuento = input("Escribe si para aplicar descuento o no para continuar sin promoción: ")
    if respuesta_descuento == "si":
        descuento = precio_base * 0.20
        print("Tu promoción a sido aplicada y el descuento es de", int(descuento), "pesos")
    elif respuesta_descuento == "no":
        descuento = 0
    else:
        print("Respuesta no válida. El programa ha terminado.")
        ejecutar = False
        break
# Calcular precio total
    precio_total = precio_base + costo_equipaje + TUA - descuento
# Mostrar resumen de su vuelo
    print("Resumen de tu vuelo:")
    print("Destino:", ciudad)
    print("Equipaje:", tipo_equipaje)
    print("Precio total (incluye TUA):", int(precio_total), "pesos")
# Preguntar si se desea realizar otro vuelo
    otra_reservacion = input("¿Deseas realizar otra reservación? Escribe si o no: ")
    if otra_reservacion == "si":
        ejecutar = True
    elif otra_reservacion == "no":
        print("Gracias por usar el sistema de vuelos de Volaris. Buen viaje")
        ejecutar = False
