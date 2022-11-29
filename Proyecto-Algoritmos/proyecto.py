# from os import remove
# import requests
# import itertools
# from Equipos import equipos
# from partidos import partidos
# from Estadios import estadios
# from Restaurante import restaurante
# from Productos import productos
# from Cliente import *


# url_equipos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
# url_estadios= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
# url_partidos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json" 

# r = requests.get(url_equipos)
# r2 = requests.get(url_estadios)
# r3 = requests.get(url_partidos)

# equipos_lista = r.json()
# estadios_lista = r2.json()
# partidos_lista = r3.json()

# equipos_totales = [] #lista con objetos
# partidos_totales = [] #lista con objetos
# estadios_totales = [] #lista con objetos
# partidazos = []
# stadium_tot = []


# for n in range(0,len(equipos_lista)):
#     nombre = equipos_lista[n]["name"]
#     cod_FIFA = equipos_lista[n]["fifa_code"]
#     grupo = equipos_lista[n]["group"]
#     id = equipos_lista[n]["id"]
#     nuevo_equipo = equipos(nombre,cod_FIFA,grupo,id)
#     equipos_totales.append(nuevo_equipo)

# for n in range(0,len(estadios_lista)):
#     id = estadios_lista[n]["id"]
#     nombre = estadios_lista[n]["name"]
#     capacidad = estadios_lista[n]["capacity"]
#     ubicacion = estadios_lista[n]["location"]
#     restaurantsArray = estadios_lista[n]["restaurants"]

#     restaurants = []
#     products = []

#     for j in range(0,len(restaurantsArray)):
#         nameRestaurant = restaurantsArray[j]["name"]
#         productsArray = restaurantsArray[j]["products"]
#         restaurantes = restaurante(nameRestaurant, products)
#         restaurants.append(restaurantes)

#         for k in range(0,len(productsArray)):
#             name = productsArray[k]["name"]
#             quantity = productsArray[k]["quantity"]
#             price = productsArray[k]["price"]
#             type = productsArray[k]["type"]
#             adicional = productsArray[k]["adicional"]
#             productos_tot = productos(name, quantity, price, type, adicional)
#             products.append(productos_tot)
    
#     estadios_tot = estadios(id,nombre,capacidad,ubicacion, restaurants)
#     estadios_totales.append(estadios_tot)
    

# for n in range(0,len(partidos_lista)):
#     equipo_local = partidos_lista[n]["home_team"]
#     equipo_visitante = partidos_lista[n]["away_team"]
#     fecha_hora = partidos_lista[n]["date"]
#     estadio_id = partidos_lista[n]["stadium_id"]
#     id = partidos_lista[n]["id"]
#     matches = partidos(equipo_local, equipo_visitante, fecha_hora, estadio_id, id)
#     partidos_totales.append(matches)


# partidazos2 = []

# for i in partidos_lista:
#     for x in equipos_totales:
#         if x.nombre == i["home_team"]:
#             equipo_local = x
#         elif x.nombre == i["away_team"]:
#             equipo_visitante = x
#     fecha_hora = i["date"]
#     for estadio in estadios_totales:
#         if estadio.id == i["stadium_id"]:
#             estadio_valido = estadio
#             id = i["id"]
#             partidos_tot = partidos(equipo_local, equipo_visitante, fecha_hora, estadio_valido, id)
#             partidazos.append(partidos_tot)
#             view_local = partidos_tot.equipo_local.nombre
#             view_away = partidos_tot.equipo_visitante.nombre
#             date = partidos_tot.fecha_hora
#             view_estadio = partidos_tot.estadio.nombre
#             view_id = partidos_tot.id
#             partidazo_tot = f"{view_local} contra {view_away} el {date} en el {view_estadio} codigo {view_id}"
#             partidazos2.append(partidazo_tot)



# def colmillos(numero):
#     numero_permutado = itertools.permutations(numero, len(numero))
#     for lista_numeros in numero_permutado:
#         pegado = ''.join(lista_numeros)
#         x , y = pegado[:int(len(pegado)/2)], pegado[int(len(pegado)/2):]
#         if x[-1] == '0' and y[-1] == '0':
#             continue
#         if int(x) * int(y) == int(numero):
#             return x,y
#     return False

# def vampiro(n):
#     prueba_string = str(n)
#     if len(prueba_string) % 2 == 1:
#         return False
#     colmillos_prueba = colmillos(prueba_string)
#     if not colmillos_prueba:
#         return False
#     return True

# def estadio_modelo():
#     print("""
#         ______________________________________________
#        /                                              \                  
#       /                                                \                          
#      /                                                  \
#     /                                                    \
#    /                                                      \
#   /                                                        \
#   \                                                        /
#    \                                                      /
#     \                                                    /
#      \                                                  /
#       \                                                /
#        \                                              /
#         ---------------------|  |---------------------
#     """)

# asientos_ocupado = []
# clientes = []
# vip_tot = 0
# vip_gastado = 0
# boleto_lista = []
# boleto_cantidad_lista = []

# while True:

#     opcion = input("\n***BIENVENIDO***\n Que desea ver?\n 1. Gestion de partidos y estadios\n 2. Gestion de venta de entradas\n 3. Gestion de restaurantes\n 4. Gestion de venta de restaurantes \n 5. Gestion de asistencia de partidos\n 6. Indicadores de gestión (Estadísticas)\n >>> ")
#     while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
#         opcion = input("\n***BIENVENIDO***\n Que desea ver?\n 1. Gestion de partidos y estadios\n 2. Gestion de venta de entradas\n 3. Gestion de restaurantes\n 4. Gestion de venta de restaurantes \n 5. Gestion de asistencia de partidos\n 6. Indicadores de gestión (Estadísticas)\n >>> ")
   
#     # Gestión de partidos y estadios
#     if opcion == "1":
#         print("***Bienvenido a la gestion de partidos y estadios!***".upper())
#         opcion1 = input(" 1. Buscar todos los partidos de un país\n 2. Buscar todos los partidos que se jugarán en un estadio específico\n 3. Buscar todos los partidos que se jugarán en una fecha determinada\n >>> ")
#         while opcion1 != "1" and opcion1 != "2" and opcion1 != "3":
#             opcion1 = input("ERROR!!! Seleccione una opcion valida\n 1. Buscar todos los partidos de un país\n 2.Buscar todos los partidos que se jugarán en un estadio específico\n 3. Buscar todos los partidos que se jugarán en una fecha determinada\n >>> ")

#         if opcion1 == "1":
#             pais = input("ingrese el pais para ver todos los partidos disponibles: ")
#             for x in partidos_totales:
#                 if x.equipo_local == pais or x.equipo_visitante == pais:
#                     mostrar_local = x.equipo_local
#                     mostrar_visitante = x.equipo_visitante
#                     mostrar_fecha = x.fecha_hora
#                     mostrar_estadio = x.estadio
#                     mostrar_id = x.id
#                     for i in estadios_totales:
#                         if mostrar_estadio == i.id:
#                             mostrar_estadio = i.nombre

#                     print(f"\n * {mostrar_local} contra {mostrar_visitante} el {date} en el {mostrar_estadio} con el codigo {mostrar_id}\n")
#                     #VALIDAR

#         elif opcion1 == "2":
#             stadium_id = input("ingrese el id del estadio para ver los partidos que se jugaran en el\n >>> ")
#             for x in partidos_totales:
#                 if x.estadio == int(stadium_id):
#                     print("holaa")
#                     mostrar_local = x.equipo_local
#                     mostrar_visitante = x.equipo_visitante
#                     mostrar_fecha = x.fecha_hora
#                     mostrar_estadio = x.estadio
#                     mostrar_id = x.id
#                     for i in estadios_totales:
#                         if mostrar_estadio == i.id:
#                             mostrar_estadio = i.nombre
#                     print(f"\n * {mostrar_local} contra {mostrar_visitante} el {date} en el {mostrar_estadio} codigo {mostrar_id}\n")
        
        
#         elif opcion1 == "3":
#             fecha = input("ingrese la fecha para ver que partidos hay en esta\n >>> ")
#             for x in partidos_totales:
#                 if x.fecha_hora == fecha:
#                     mostrar_local = x.equipo_local
#                     mostrar_visitante = x.equipo_visitante
#                     mostrar_fecha = x.fecha_hora
#                     mostrar_estadio = x.estadio
#                     mostrar_id = x.id
#                     for i in estadios_totales:
#                         if mostrar_estadio == i.id:
#                             mostrar_estadio = i.nombre
#                     print(f"\n * {mostrar_local} contra {mostrar_visitante} el {date} en el {mostrar_estadio} codigo {mostrar_id}\n")
#         # AGREGAR TXT

#     # GESTION DE ENTRADAS
#     elif opcion == "2":
#         print("\n***BIENVENIDO A LA GESTION DE ENTRADAS!***\n".upper())
#         nombre = input("Ingrese su nombre: ")
#         while not nombre.isalpha():
#             nombre = input("ERROR! Ingrese su nombre: ")
#         cedula = input("Ingrese su cedula: ")
#         while not cedula.isnumeric():
#             cedula = input("ERROR! Ingrese su cedula: ")
#         edad = input("Ingrese su edad: ")
#         while not edad.isnumeric():
#             edad = input("ERROR! Ingrese su edad: ")
#         for x in partidazos2:
#             print(x)
#         comprar_partido = input("\nIngrese el codigo del partido del que desea comprar su entrada: ")
#         while not comprar_partido.isnumeric() or not int(comprar_partido) > 0 or not int(comprar_partido) <= 48:
#             comprar_partido = input("ERROR! Ingrese el codigo del partido del que desea comprar su entrada: ")
        
#         for x in partidos_totales:
#             if x.id == comprar_partido:
#                 mostrar_local = x.equipo_local
#                 mostrar_visitante = x.equipo_visitante
#                 mostrar_fecha = x.fecha_hora
#                 mostrar_estadio = x.estadio
#                 mostrar_id = x.id
#                 for i in estadios_totales:
#                     if mostrar_estadio == i.id:
#                         mostrar_estadio = i.nombre
#                 for j in estadios_totales:
#                     mostrar_capacidad = j.capacidad
#                 print(f"\n El partido que usted ha seleccionado es: {mostrar_local} contra {mostrar_visitante} el {mostrar_fecha} en el {mostrar_estadio} con una capacidad de {mostrar_capacidad}\n codigo {mostrar_id}\n")
#         cantidad_boleto = input("Que cantidad de boletos de ese partido desea?: ")
#         while not cantidad_boleto.isnumeric():
#             cantidad_boleto = input("ERROR! Que cantidad de boletos de ese partido desea?: ")

#         entrada = input("Desea que su entrada sea general o vip.\n 1. general(50$)\n 2. vip(120$)\n ")
#         while not entrada == "1" and not entrada == "2":
#             entrada = input("ERROR! Desea que su entrada sea general o vip.\n 1. general(50$)\n 2. vip(120$)\n ")

#         if entrada == "1":    
#             asiento = input(f"Seleccione un asiento entre 1 y {mostrar_capacidad[0]} (los asientos van por numero)\n ")
#             while not asiento.isnumeric() or f"{comprar_partido}-{asiento}" in asientos_ocupado or not int(asiento) >= 1 or not int(asiento) <= mostrar_capacidad[0]:
#                 asiento = input(f"ERROR/ASIENTO OCUPADO! Seleccione un asiento entre 1 y {mostrar_capacidad[0]} (los asientos van por numero)\n ")
#             precio = 50
#             IVA = 0.16
#             precio_tot = precio + (precio * IVA)
#             if vampiro(int(cedula)) == True:
#                 precio_tot = (precio + (precio * IVA))/2
#                 print("***FELICIDADES***, tiene un 50% de descuento en el precio total debido a que su cedula es un numero vampiro\n")
#             print(f"Su asiento es el: {asiento}, con un costo de: {precio} mas el IVA {precio * IVA} con un total de {int(cantidad_boleto) * precio_tot} codigo de boleto: {comprar_partido}-{asiento} cantidad de boletos {cantidad_boleto}")


#         elif entrada == "2":
#             asiento = input(f"Seleccione un asiento entre 1 y {mostrar_capacidad[1]} (los asientos van por numero)\n ")
#             while not asiento.isnumeric() or f"{comprar_partido}-{asiento}" in asientos_ocupado or not int(asiento) >= 1 or not int(asiento) <= mostrar_capacidad[1]:
#                 asiento = input(f"ERROR/ASIENTO OCUPADO! Seleccione un asiento entre 1 y {mostrar_capacidad[1]} (los asientos van por numero)\n ")
#             precio = 120
#             IVA = 0.16
#             precio_tot = precio + (precio * IVA)
#             if vampiro(int(cedula)) == True:
#                 precio_tot = (precio + (precio * IVA))/2
#                 print("\n***FELICIDADES***, tiene un 50% de descuento en el precio total debido a que su cedula es un numero vampiro\n")
#             print(f"Su asiento es el: {asiento}, con un costo de: {precio} mas el IVA {precio * IVA} con un total de {int(cantidad_boleto) * precio_tot} codigo de boleto: {comprar_partido}-{asiento} cantidad de boletos {cantidad_boleto}")
            
    
#         completar_pago = input("Desea completar su pago?\n 1. si\n 2. no\n ")
#         while not completar_pago == "1" and not completar_pago == "2":
#             completar_pago = input("ERROR! Desea completar su pago?\n 1. si\n 2. no\n ")

#         if completar_pago == "1":
#             print("\n ******PAGO REALIZADO CON EXITO! GRACIAS POR SU COMPRA******\n")
#             if entrada == "2":
#                 vip_gastado += precio_tot
#                 vip_tot += 1
#             entrada = entradas(entrada, cantidad_boleto, comprar_partido, asiento)
            
#             clienteObjeto = cliente(nombre, edad, cedula, entrada)

#             clientes.append(clienteObjeto)

#             codigo = f"{comprar_partido}-{asiento}"
#             asientos_ocupado.append(codigo)
#             boleto_lista.append(codigo)
            
#         else:
#             print("\n Vuelva pronto :( ")
#             # HACER EL TXT

#     # GESTION DE RESTAURANTES
#     elif opcion == "3":
#         print("***Bienvenido a la gestion de productos en los restaurantes!***".upper())
#         for estadio in estadios_totales:
#             print(estadio.nombre + "\n")
#             for restaurant in estadio.restaurantes:
#                 print(restaurant.nombre + "\n")
#                 for producto in restaurant.productos:
#                     producto.mostrar()
#         opcion2 = input("\n Que opcion desea escoger para buscar productos?\n 1. Por nombre\n 2. Por tipo\n 3. Por rango de precio\n >>> ")
#         while not opcion2 == "1" and not opcion2 == "2" and not opcion2 == "3":
#             opcion2 = input("\n ERROR! Que opcion desea escoger para buscar productos?\n 1. Por nombre\n 2. Por tipo\n 3. Por rango de precio\n >>> ")

#         # por nombre
#         if opcion2 == "1":
#             producto_nombre = input("Ingrese el producto que desea ver por su nombre: ")
#             if producto_nombre != producto.nombre:
#                 print("\n**Lo siento el producto no fue encontrado, intente de nuevo!**")
#             for estadio in estadios_totales:
#                 for restaurant in estadio.restaurantes:
#                     for producto in restaurant.productos:
#                         if producto.nombre == producto_nombre:
#                             print("*** " + estadio.nombre)
#                             print(restaurant.nombre)
#                             producto.mostrar()
                            

#         # por tipo
#         elif opcion2 == "2":
#             producto_tipo = input("Ingrese el producto que desea ver por su tipo.\n *beverages\n *food\n >>> ")
#             while not producto_tipo == "beverages" and not producto_tipo == "food":
#                 producto_tipo = input("ERROR! Ingrese el producto que desea ver por su tipo.\n *beverages\n *food\n >>> ")

#             for estadio in estadios_totales:
#                 for restaurant in estadio.restaurantes:
#                     for producto in restaurant.productos:
#                         if producto.tipo == producto_tipo:
#                             print("*** " + estadio.nombre)
#                             print(restaurant.nombre)
#                             producto.mostrar()
        
#         # por rango de precio
#         elif opcion2 == "3":
#             precio_minimo = input("Ingrese un precio minimo para ver el rango de precio: ")
#             while not precio_minimo.isnumeric():
#                 precio_minimo = input("ERROR! Ingrese un precio minimo para ver el rango de precio: ")

#             precio_maximo = input("Ingrese un precio maximo para ver el rango de precio: ")
#             while not precio_maximo.isnumeric():
#                 precio_maximo = input("ERROR! Ingrese un precio minimo para ver el rango de precio: ")

#             for estadio in estadios_totales:
#                 for restaurant in estadio.restaurantes:
#                     for producto in restaurant.productos:
#                         if producto.precio >= int(precio_minimo) and producto.precio <= int(precio_maximo):
#                             print("*** " + estadio.nombre)
#                             print(restaurant.nombre)
#                             producto.mostrar()

#     # Gestion de venta de restaurantes
#     elif opcion == "4":
#         print("***Bienvenido a la gestion de venta de restaurantes!***\n".upper())
#         cedula = input("Ingrese su cedula para ver si puede entrar a los restaurantes: ")
#         while not cedula.isnumeric():
#             cedula = input("ERROR! Ingrese su cedula para ver si puede entrar a los restaurantes: ")
#         productoEscogido = ""
#         productoEscogidoNombre = ""
#         cantidadAPagar = 0

#         for clienteX in clientes:
#             if clienteX.cedula == cedula:
#                 if clienteX.entradas.tipo == "2":
#                         for partido in partidos_totales:
#                             if partido.id == clienteX.entradas.id_partido:
#                                 for estadio in estadios_totales:
#                                     if partido.estadio == estadio.id:
#                                         lista_productos_restaurantes_estadio = []
#                                         for restaurant in estadio.restaurantes:
#                                             print("\n" + restaurant.nombre + "\n")
#                                             for producto in restaurant.productos:
#                                                 if int(clienteX.edad) > 18:
#                                                     producto.mostrar()
#                                                     lista_productos_restaurantes_estadio.append(producto.nombre)
#                                                 else:
#                                                     if producto.adicional != "alcoholic":
#                                                         producto.mostrar()
#                                                         lista_productos_restaurantes_estadio.append(producto.nombre)

#                                         producto_escogido_nombre = input("\nIngrese el nombre del producto que desea comprar: ")
#                                         while not producto_escogido_nombre.isalpha() or not producto_escogido_nombre in lista_productos_restaurantes_estadio:
#                                             producto_escogido_nombre = input("\nERROR! Ingrese el nombre del producto que desea comprar: ")
#                                         for producto in restaurant.productos:
#                                             if producto_escogido_nombre == producto.nombre:
#                                                 producto_escogido_nombre = producto
#                                         cantidad = input("\nQue cantidad de ese producto desea comprar: ")
#                                         while not cantidad.isnumeric():
#                                             cantidad = input("ERROR! Que cantidad desea comprar: ")

#                                         lista_productos_restaurantes_estadio = []

#                                         num_cedula = int(clienteX.cedula)
#                                         sum_v = 0  
#                                         for i in range(1,num_cedula):  
#                                             if (num_cedula % i == 0):  
#                                                 sum_v=sum_v + i  
#                                         if(sum_v==num_cedula):  
#                                             print("\n***Su cedula es un numero perfecto. Tiene un descuento de 15%***\n")
#                                             cantidadAPagar = int(cantidad)*(producto_escogido_nombre.precio - (producto_escogido_nombre.precio * 0.15))
#                                         else:  
#                                             print("\nSu cedula no es un numero perfecto. No obtiene el descuento :( ")
#                                             cantidadAPagar = int(cantidad) * producto_escogido_nombre.precio

#                                         print(f"     ***FACTURA***\n Producto escogido: {producto_escogido_nombre.nombre}\n subtotal: {int(cantidad)*(producto_escogido_nombre.precio)}\n Descuento(en caso de que lo tenga, en caso de no tenerlo se mostrara el descuento pero no se restara al total): {(int(cantidad) * producto_escogido_nombre.precio) * 0.15}\n TOTAL: {cantidadAPagar}")

#                                         continuar = input("\nDesea continuar con su compra?\n 1. Si\n 2. No\n")
#                                         while not continuar == "1" and not continuar == "2":
#                                             continuar = input("ERROR! Desea continuar con su compra?\n 1. Si\n 2. No\n")


#                                         if continuar == "1":
#                                             print("\n ******PAGO REALIZADO CON EXITO! GRACIAS POR SU COMPRA******\n")
#                                             vip_gastado += cantidadAPagar

#                                         else:
#                                             if continuar == "2":
#                                                 pass
#                                                 print("Vuelva pronto :( ")

#                                         # intento de restar el producto del inventario
#                                         # for producto in range(1,restaurant.productos):
#                                         #     if restaurant.productos[producto] == producto_escogido_nombre:
#                                         #         remove(restaurant.producots[producto])
    

#     # Gestión de asistencia a partidos    
#     elif opcion == "5":
#         print("***Bienvenido a la gestión de asistencia a partidos!***".upper())
#         verificar_boleto = input("Ingrese el codigo de su boleto: ")
#         for boletos in boleto_lista:
#             if verificar_boleto == boletos:
#                 ver_partido = comprar_partido
#                 for partido in partidos_totales:
#                     if ver_partido == str(partido.id):
#                         ""
#                 print("\n***Boleto valido*** Bienvenido!")
#                 boleto_lista.remove(boletos)
#             else:
#                 print("Boleto no valido :( ")                    

#     # Indicadores de gestión (Estadísticas)
#     elif opcion == "6":
#         print("\n***Bienvenido a las estadisticas!***".upper())
#         if vip_tot == 0:
#             print("No hay nada que promediar :( ")
#         else:
#             print(f"\n*El gasto promedio de un cliente vip es: {vip_gastado/vip_tot}\n")
        
#         for x in partidos_totales:
#             if comprar_partido == x.id:
#                 boleto_cantidad_lista.append(int(cantidad_boleto))
#                 max_boleto = max(boleto_cantidad_lista)
#                 print(f"*El partido con mayor asistencias fue el {x.id} con {max_boleto} boletos vendidos")
      






        