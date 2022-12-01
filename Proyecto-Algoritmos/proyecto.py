#importaciones de todas las clases usadas 
from os import remove
import requests
import itertools
from Equipos import equipos
from partidos import partidos
from Estadios import estadios
from Restaurante import restaurante
from Productos import productos
from Cliente import *


#traer la informacion de la api
url_equipos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
url_estadios= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
url_partidos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json" 

r = requests.get(url_equipos)
r2 = requests.get(url_estadios)
r3 = requests.get(url_partidos)

#asignarle una variable a cada json para despues iterarlo etc
equipos_lista = r.json()
estadios_lista = r2.json()
partidos_lista = r3.json()


equipos_totales = [] #lista con objetos 
partidos_totales = [] #lista con objetos
estadios_totales = [] #lista con objetos
partidazos = []
stadium_tot = []


for n in range(0,len(equipos_lista)): #for iterando la lista de los equipos traida de la api y usando el constructor
    nombre = equipos_lista[n]["name"]
    cod_FIFA = equipos_lista[n]["fifa_code"]
    grupo = equipos_lista[n]["group"]
    id = equipos_lista[n]["id"]
    nuevo_equipo = equipos(nombre,cod_FIFA,grupo,id)
    equipos_totales.append(nuevo_equipo)

for n in range(0,len(estadios_lista)): #for iterando la lista de los estadios traida de la api y usando el constructor para obtener los objetos de esa lista
    id = estadios_lista[n]["id"]
    nombre = estadios_lista[n]["name"]
    capacidad = estadios_lista[n]["capacity"]
    ubicacion = estadios_lista[n]["location"]
    restaurantsArray = estadios_lista[n]["restaurants"]

    restaurants = [] #lista para guardar los objetos de restaurantes
    products = []   #lista para guardar los objetos de productos

    for j in range(0,len(restaurantsArray)): #for iterando la lista de los restaurantes dentro de los estadios traida de la api y usando el constructor para obtener los objetos de esa lista
        nameRestaurant = restaurantsArray[j]["name"]
        productsArray = restaurantsArray[j]["products"]
        restaurantes = restaurante(nameRestaurant, products)
        restaurants.append(restaurantes)

        for k in range(0,len(productsArray)): #for iterando la lista de los productos en los restaurantes dentro de los estadios traida de la api y usando el constructor para obtener los objetos de esa lista
            name = productsArray[k]["name"]
            quantity = productsArray[k]["quantity"]
            price = productsArray[k]["price"]
            type = productsArray[k]["type"]
            adicional = productsArray[k]["adicional"]
            productos_tot = productos(name, quantity, price, type, adicional)
            products.append(productos_tot)
    
    estadios_tot = estadios(id,nombre,capacidad,ubicacion, restaurants)
    estadios_totales.append(estadios_tot)
    

for n in range(0,len(partidos_lista)): #for iterando la lista de los partidos traida de la api y usando el constructor para obtener los objetos de esa lista
    equipo_local = partidos_lista[n]["home_team"]
    equipo_visitante = partidos_lista[n]["away_team"]
    fecha_hora = partidos_lista[n]["date"]
    estadio_id = partidos_lista[n]["stadium_id"]
    id = partidos_lista[n]["id"]
    matches = partidos(equipo_local, equipo_visitante, fecha_hora, estadio_id, id)
    partidos_totales.append(matches)


partidazos2 = [] #lista con todos los partidos impresos por orden 

for i in partidos_lista:
    for x in equipos_totales: # for para ingresar a los objetos de todo lo que tiene equipos totales traido de la api y transformado a objeto anteriormente
        if x.nombre == i["home_team"]:
            equipo_local = x
        elif x.nombre == i["away_team"]:
            equipo_visitante = x
    fecha_hora = i["date"]
    for estadio in estadios_totales: #for para ingresar a los estadios totales traido de la api 
        if estadio.id == i["stadium_id"]:
            estadio_valido = estadio
            id = i["id"]
            partidos_tot = partidos(equipo_local, equipo_visitante, fecha_hora, estadio_valido, id)
            partidazos.append(partidos_tot)
            view_local = partidos_tot.equipo_local.nombre
            view_away = partidos_tot.equipo_visitante.nombre
            date = partidos_tot.fecha_hora
            view_estadio = partidos_tot.estadio.nombre
            view_id = partidos_tot.id
            partidazo_tot = f"{view_local} contra {view_away} el {date} en el {view_estadio} codigo {view_id}"
            partidazos2.append(partidazo_tot) #append a la lista partidazos 2 despues de haber obetinido todos los valores de los partidos que antes eran objetos


#Funcion para calcular los colmillos del numero vampiro
def colmillos(numero):
    numero_permutado = itertools.permutations(numero, len(numero))
    for lista_numeros in numero_permutado:
        pegado = ''.join(lista_numeros)
        x , y = pegado[:int(len(pegado)/2)], pegado[int(len(pegado)/2):]
        if x[-1] == '0' and y[-1] == '0':
            continue
        if int(x) * int(y) == int(numero):
            return x,y
    return False

#Funcion para calcular si el numero es o no vampiro
def vampiro(n):
    prueba_string = str(n)
    if len(prueba_string) % 2 == 1:
        return False
    colmillos_prueba = colmillos(prueba_string)
    if not colmillos_prueba:
        return False
    return True

def estadio_modelo(): #funcion para imprimir el estadio
    print("""
        -------------------------------------------------
       /  x-1 x-2 x-3 x-4 x-5 x-6 x-7 x-8 x-9 x-10       \                          
      /                                                   \                 
     /              x-11 x-12 x-13 x-14 x-15               \                        
    /                                                       \                       
   /         VIP      x-1 x-2 x-3 x-4 x-5                    \                      
  /                                                           \ 

  \          VIP      x-6 x-7 x-8 x-9 x-10                    /
   \                                                         /
    \               x-16 x-17 x-18 x-19 x-20                /
     \                                                     /
      \ x-21 x-22 x-23 x-24 x-25 x-26 x-27 x-28 x-29 x-30 /
       \                                                 /
        ---------------------|  |------------------------
    """)
asientos_ocupado = []
clientes = []
vip_tot = 0
vip_gastado = 0
boleto_lista = []
boleto_cantidad_lista = []
lista_clientes = []

while True:

    opcion = input("\n***BIENVENIDO! AL PROYECTO: QATAR 2022 ⚽***\n Que desea ver?\n 1. Gestion de partidos y estadios\n 2. Gestion de venta de entradas\n 3. Gestion de restaurantes\n 4. Gestion de venta de restaurantes \n 5. Gestion de asistencia de partidos\n 6. Indicadores de gestión (Estadísticas)\n >>> ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
        opcion = input("\n***BIENVENIDO***\n Que desea ver?\n 1. Gestion de partidos y estadios\n 2. Gestion de venta de entradas\n 3. Gestion de restaurantes\n 4. Gestion de venta de restaurantes \n 5. Gestion de asistencia de partidos\n 6. Indicadores de gestión (Estadísticas)\n >>> ")
   
    # Gestión de partidos y estadios
    if opcion == "1":
        #if si el usuario desea entrar a la gestion de partidos y estadios
        print("***Bienvenido a la gestion de partidos y estadios!***".upper())
        opcion1 = input(" 1. Buscar todos los partidos de un país\n 2. Buscar todos los partidos que se jugarán en un estadio específico\n 3. Buscar todos los partidos que se jugarán en una fecha determinada\n >>> ")
        while opcion1 != "1" and opcion1 != "2" and opcion1 != "3": #validacion para que escoja la opcion deseada 
            opcion1 = input("ERROR!!! Seleccione una opcion valida\n 1. Buscar todos los partidos de un país\n 2.Buscar todos los partidos que se jugarán en un estadio específico\n 3. Buscar todos los partidos que se jugarán en una fecha determinada\n >>> ")

        if opcion1 == "1":
            pais = input("ingrese el pais para ver todos los partidos disponibles: ")
            for x in partidos_totales: #for para ingresar a los partidos totales
                if x.equipo_local == pais or x.equipo_visitante == pais: #if para que si la opcion que ingresa el usuario es igual a un equipo local o visitante pueda ingresar al if y al final imprimir lo que se desea
                    mostrar_local = x.equipo_local
                    mostrar_visitante = x.equipo_visitante
                    mostrar_fecha = x.fecha_hora
                    mostrar_estadio = x.estadio
                    mostrar_id = x.id
                    for i in estadios_totales: #for para ingresar a los estadios y a sus valores 
                        if mostrar_estadio == i.id:
                            mostrar_estadio = i.nombre

                    print(f"\n * {mostrar_local} contra {mostrar_visitante} el {date} en el {mostrar_estadio} con el codigo {mostrar_id}\n")
                    #VALIDAR

        elif opcion1 == "2":
            stadium_id = input("ingrese el id del estadio para ver los partidos que se jugaran en el\n >>> ") #ingresar el id del estadio para mostrar el estadio
            for x in partidos_totales:
                if x.estadio == int(stadium_id): #if para verificar si el id del estadio es igual al id ingresado por el usuario
                    mostrar_local = x.equipo_local
                    mostrar_visitante = x.equipo_visitante
                    mostrar_fecha = x.fecha_hora
                    mostrar_estadio = x.estadio
                    mostrar_id = x.id
                    for i in estadios_totales:
                        if mostrar_estadio == i.id:
                            mostrar_estadio = i.nombre
                    print(f"\n * {mostrar_local} contra {mostrar_visitante} el {date} en el {mostrar_estadio} codigo {mostrar_id}\n")
        
        
        elif opcion1 == "3":
            fecha = input("ingrese la fecha para ver que partidos hay en esta\n >>> ") #ingresar la fecha en la que quiere ver un partido
            for x in partidos_totales:
                if x.fecha_hora == fecha:
                    mostrar_local = x.equipo_local
                    mostrar_visitante = x.equipo_visitante
                    mostrar_fecha = x.fecha_hora
                    mostrar_estadio = x.estadio
                    mostrar_id = x.id
                    for i in estadios_totales:
                        if mostrar_estadio == i.id:
                            mostrar_estadio = i.nombre
                    print(f"\n * {mostrar_local} contra {mostrar_visitante} el {date} en el {mostrar_estadio} codigo {mostrar_id}\n")
        # AGREGAR TXT


    # GESTION DE ENTRADAS
    elif opcion == "2":
        #Validaciones para poder ingresar a la venta de entrada obetener los datos del usuario que desee
        print("\n***BIENVENIDO A LA GESTION DE ENTRADAS!***\n".upper()) 
        nombre = input("Ingrese su nombre: ")
        while not nombre.isalpha():
            nombre = input("ERROR! Ingrese su nombre: ")
        cedula = input("Ingrese su cedula: ")
        while not cedula.isnumeric():
            cedula = input("ERROR! Ingrese su cedula: ")
        edad = input("Ingrese su edad: ")
        while not edad.isnumeric():
            edad = input("ERROR! Ingrese su edad: ")
        for x in partidazos2:
            print(x)
        comprar_partido = input("\nIngrese el codigo del partido del que desea comprar su entrada: ") #ingresar el codigo del partido que quiere comprar
        while not comprar_partido.isnumeric() or not int(comprar_partido) > 0 or not int(comprar_partido) <= 48: # validar que ingrese los datos correctos acorde a lo que se necesita
            comprar_partido = input("ERROR! Ingrese el codigo del partido del que desea comprar su entrada: ")
        
        for x in partidos_totales: #for para ingresar a los partidos totales (obj)
            if x.id == comprar_partido: #if para comprobar si el id del partido (codigo) coincide con la respuesta del usuario
                mostrar_local = x.equipo_local
                mostrar_visitante = x.equipo_visitante
                mostrar_fecha = x.fecha_hora
                mostrar_estadio = x.estadio
                mostrar_id = x.id
                for i in estadios_totales:
                    if mostrar_estadio == i.id: 
                        mostrar_estadio = i.nombre
                for j in estadios_totales:
                    mostrar_capacidad = j.capacidad
                print(f"\n El partido que usted ha seleccionado es: {mostrar_local} contra {mostrar_visitante} el {mostrar_fecha} en el {mostrar_estadio} con una capacidad de {mostrar_capacidad}\n codigo {mostrar_id}\n")
        cantidad_boleto = input("Que cantidad de boletos de ese partido desea?: ")
        while not cantidad_boleto.isnumeric():
            cantidad_boleto = input("ERROR! Que cantidad de boletos de ese partido desea?: ")

        entrada = input("Desea que su entrada sea general o vip.\n 1. general(50$)\n 2. vip(120$)\n ")
        while not entrada == "1" and not entrada == "2":
            entrada = input("ERROR! Desea que su entrada sea general o vip.\n 1. general(50$)\n 2. vip(120$)\n ")

        if entrada == "1": 
            estadio_modelo()
            #si la opcion entrada es igual a 1 significa que su entrada es general por lo tanto entrara en este if   
            asiento = input(f"\nSeleccione un asiento entre 1 y {mostrar_capacidad[0]} (los asientos van por numero)\n ")
            while not asiento.isnumeric() or f"{comprar_partido}-{asiento}" in asientos_ocupado or not int(asiento) >= 1 or not int(asiento) <= mostrar_capacidad[0]:
                asiento = input(f"ERROR/ASIENTO OCUPADO! Seleccione un asiento entre 1 y {mostrar_capacidad[0]} (los asientos van por numero)\n ")
            precio = 50
            IVA = 0.16
            precio_tot = precio + (precio * IVA)
            if vampiro(int(cedula)) == True:
                precio_tot = (precio + (precio * IVA))/2
                print("***FELICIDADES***, tiene un 50% de descuento en el precio total debido a que su cedula es un numero vampiro\n")
            print(f"**Su asiento es el: {asiento}, con un costo de: {precio} mas el IVA {precio * IVA} con un total de {int(cantidad_boleto) * precio_tot} codigo de boleto: {comprar_partido}-{asiento} cantidad de boletos {cantidad_boleto}**")


        elif entrada == "2":
            estadio_modelo()
            #si la opcion entrada es igual a 1 significa que su entrada es vip por lo tanto entrara en este otro if 
            asiento = input(f"Seleccione un asiento entre 1 y {mostrar_capacidad[1]} (los asientos van por numero)\n ")
            while not asiento.isnumeric() or f"{comprar_partido}-{asiento}" in asientos_ocupado or not int(asiento) >= 1 or not int(asiento) <= mostrar_capacidad[1]:
                asiento = input(f"ERROR/ASIENTO OCUPADO! Seleccione un asiento entre 1 y {mostrar_capacidad[1]} (los asientos van por numero)\n ")
            precio = 120
            IVA = 0.16
            precio_tot = precio + (precio * IVA)
            if vampiro(int(cedula)) == True:
                precio_tot = (precio + (precio * IVA))/2
                print("\n***FELICIDADES***, tiene un 50% de descuento en el precio total debido a que su cedula es un numero vampiro\n")
            print(f"Su asiento es el: {asiento}, con un costo de: {precio} mas el IVA {precio * IVA} con un total de {int(cantidad_boleto) * precio_tot} codigo de boleto: {comprar_partido}-{asiento} cantidad de boletos {cantidad_boleto}")
            
    
        completar_pago = input("Desea completar su pago?\n 1. si\n 2. no\n ")
        while not completar_pago == "1" and not completar_pago == "2":
            completar_pago = input("ERROR! Desea completar su pago?\n 1. si\n 2. no\n ")

        if completar_pago == "1":
            #si desea completar el pago entrara en este if e imprimira que el pago fue realizado con exito
            print("\n ******PAGO REALIZADO CON EXITO! GRACIAS POR SU COMPRA******\n")
            if entrada == "2":
                vip_gastado += precio_tot
                vip_tot += 1
            entrada = entradas(entrada, cantidad_boleto, comprar_partido, asiento) #ya con los atributos definidos se realiza de una vez el constructor para la clase entradas y cliente y se agregan a las listas indicadas
            clienteObjeto = cliente(nombre, edad, cedula, entrada)
            clientes.append(clienteObjeto)
            codigo = f"{comprar_partido}-{asiento}" #codigo es para despues validar los asientos en la gestion de asistencias a partidos
            asientos_ocupado.append(codigo)
            boleto_lista.append(codigo)
            
        else:
            print("\n Vuelva pronto :( ")
            # HACER EL TXT

    # GESTION DE RESTAURANTES
    elif opcion == "3":
        #if por si el usuario desea entrar a la gestion de restaurante
        print("***Bienvenido a la gestion de productos en los restaurantes!***".upper())
        for estadio in estadios_totales:
            print(estadio.nombre + "\n")
            for restaurant in estadio.restaurantes: #for para ingresar a los restaurantes de un estadio 
                print(restaurant.nombre + "\n")
                for producto in restaurant.productos: #for para ingresar a los productos de cierto restaurante
                    producto.mostrar()
        opcion2 = input("\n Que opcion desea escoger para buscar productos?\n 1. Por nombre\n 2. Por tipo\n 3. Por rango de precio\n >>> ")
        while not opcion2 == "1" and not opcion2 == "2" and not opcion2 == "3":
            opcion2 = input("\n ERROR! Que opcion desea escoger para buscar productos?\n 1. Por nombre\n 2. Por tipo\n 3. Por rango de precio\n >>> ")

        # if para mostrarle al usuario los productos por nombre 
        if opcion2 == "1":
            producto_nombre = input("Ingrese el producto que desea ver por su nombre: ")
            if producto_nombre != producto.nombre:
                print("\n**Lo siento el producto no fue encontrado, intente de nuevo!**")

            for estadio in estadios_totales: 
                for restaurant in estadio.restaurantes:
                    for producto in restaurant.productos:
                        if producto.nombre == producto_nombre: #en este if se valida que el producto.nombre es decir los productos encontrados por nombre en los restaurantes sea igual a el producto que el cliente desee ver 
                            print("*** " + estadio.nombre)
                            print(restaurant.nombre)
                            producto.mostrar()
                            

        # if para mostrarle al usuario los productos por tipo 
        elif opcion2 == "2":
            producto_tipo = input("Ingrese el producto que desea ver por su tipo.\n *beverages\n *food\n >>> ")
            while not producto_tipo == "beverages" and not producto_tipo == "food":
                producto_tipo = input("ERROR! Ingrese el producto que desea ver por su tipo.\n *beverages\n *food\n >>> ")

            for estadio in estadios_totales:
                for restaurant in estadio.restaurantes:
                    for producto in restaurant.productos:
                        if producto.tipo == producto_tipo: #en este if se valida que el producto.tipo es decir los productos encontrados por tipo en los restaurantes sea igual a el producto que el cliente desee ver 
                            print("*** " + estadio.nombre)
                            print(restaurant.nombre)
                            producto.mostrar()
        
        # if para mostrarle al usuario los productos por rango de precio 
        elif opcion2 == "3":
            precio_minimo = input("Ingrese un precio minimo para ver el rango de precio: ")
            while not precio_minimo.isnumeric():
                precio_minimo = input("ERROR! Ingrese un precio minimo para ver el rango de precio: ")

            precio_maximo = input("Ingrese un precio maximo para ver el rango de precio: ")
            while not precio_maximo.isnumeric():
                precio_maximo = input("ERROR! Ingrese un precio minimo para ver el rango de precio: ")

            for estadio in estadios_totales:
                for restaurant in estadio.restaurantes:
                    for producto in restaurant.productos:
                        if producto.precio >= int(precio_minimo) and producto.precio <= int(precio_maximo): #en este if se valida que el precio del producto sea adecuado para el rango de precio ingresado y los precios encontrados en la lista de productos
                            print("*** " + estadio.nombre)
                            print(restaurant.nombre)
                            producto.mostrar()

    # Gestion de venta de restaurantes
    elif opcion == "4":
        #if por si el usuario desea ver la gestio de venta de restaurantes 
        print("***Bienvenido a la gestion de venta de restaurantes!***\n".upper())
        cedula = input("Ingrese su cedula para ver si puede entrar a los restaurantes: ")
        while not cedula.isnumeric():
            cedula = input("ERROR! Ingrese su cedula para ver si puede entrar a los restaurantes: ")
        productoEscogido = ""
        productoEscogidoNombre = ""
        cantidadAPagar = 0


        #los siguientes for son para validar que el cliente sea vip es decir que haya comprado la entrada de tipo "2" en la gestion de venta de entradas 
        # despues si el partido.id es igual al id del partido que el cliente compro entra en el for de los estadios para hacer otro if
        #que valida si el estadio es igual al estadio por su id. Lo que sigue es para entrar a los productos de un restaurante especifico de un estadio especifico
        for clienteX in clientes:
            if clienteX.cedula == cedula:
                if clienteX.entradas.tipo == "2":
                        for partido in partidos_totales:
                            if partido.id == clienteX.entradas.id_partido:
                                for estadio in estadios_totales:
                                    if partido.estadio == estadio.id:
                                        lista_productos_restaurantes_estadio = [] #se crea una lista vacia 
                                        for restaurant in estadio.restaurantes: #for que entra en los restaurantes de un estadio
                                            print("\n" + restaurant.nombre + "\n") #nombre del restaurante
                                            for producto in restaurant.productos: #for para acceder a los productos de un restaurantes 
                                                if int(clienteX.edad) > 18: #if para validar si es o no mayor de edad segun la edad ingresada en la venta de entradas
                                                    producto.mostrar() #si es mayor muestra las bebidas alcoholicas
                                                    lista_productos_restaurantes_estadio.append(producto.nombre)
                                                else: #si es menor muestra todo menos las bebidas alcoholicas
                                                    if producto.adicional != "alcoholic":
                                                        producto.mostrar()
                                                        lista_productos_restaurantes_estadio.append(producto.nombre)

                                        producto_escogido_nombre = input("\nIngrese el nombre del producto que desea comprar: ")
                                        while not producto_escogido_nombre.isalpha() or not producto_escogido_nombre in lista_productos_restaurantes_estadio:
                                            producto_escogido_nombre = input("\nERROR! Ingrese el nombre del producto que desea comprar: ")
                                        for producto in restaurant.productos:
                                            if producto_escogido_nombre == producto.nombre: #if para ingresar al producto por nombre ya que asi se le pide al usuario  
                                                producto_escogido_nombre = producto
                                        cantidad = input("\nQue cantidad de ese producto desea comprar: ")
                                        while not cantidad.isnumeric():
                                            cantidad = input("ERROR! Que cantidad desea comprar: ")

                                        lista_productos_restaurantes_estadio = []

                                        num_cedula = int(clienteX.cedula) #bloque para validar si la cedula del cliente es un numero perfecto 
                                        sum_v = 0  
                                        for i in range(1,num_cedula):  
                                            if (num_cedula % i == 0):  
                                                sum_v = sum_v + i  
                                        if(sum_v == num_cedula):  
                                            print("\n***Su cedula es un numero perfecto. Tiene un descuento de 15%***\n")
                                            cantidadAPagar = int(cantidad)*(producto_escogido_nombre.precio - (producto_escogido_nombre.precio * 0.15)) #Cantidad total a pagar con el descuento del numero perfecto
                                        else:  
                                            print("\nSu cedula no es un numero perfecto. No obtiene el descuento :( ")
                                            cantidadAPagar = int(cantidad) * producto_escogido_nombre.precio

                                        #Cantidad total a pagar sin el descuento
                                        print(f"     ***FACTURA***\n Producto escogido: {producto_escogido_nombre.nombre}\n subtotal: {int(cantidad)*(producto_escogido_nombre.precio)}\n Descuento(en caso de que lo tenga, en caso de no tenerlo se mostrara el descuento pero no se restara al total): {(int(cantidad) * producto_escogido_nombre.precio) * 0.15}\n TOTAL: {cantidadAPagar}")

                                        continuar = input("\nDesea continuar con su compra?\n 1. Si\n 2. No\n")
                                        while not continuar == "1" and not continuar == "2":
                                            continuar = input("ERROR! Desea continuar con su compra?\n 1. Si\n 2. No\n")


                                        if continuar == "1":
                                            #if para continuar con el pago 
                                            print("\n ******PAGO REALIZADO CON EXITO! GRACIAS POR SU COMPRA******\n")
                                            vip_gastado += cantidadAPagar

                                        else:
                                            #else por si no quiere continuar con el pago
                                            if continuar == "2":
                                                pass
                                                print("Vuelva pronto :( ")

                                        # intento de restar el producto del inventario
                                        # for producto in range(1,restaurant.productos):
                                        #     if restaurant.productos[producto] == producto_escogido_nombre:
                                        #         remove(restaurant.producots[producto])
                else:
                    print("\nlo siento no eres cliente vip :( ")

    # Gestión de asistencia a partidos    
    elif opcion == "5":
        #if por si el usuario desea ver la gestión de asistencia a partidos
        print("***Bienvenido a la gestión de asistencia a partidos!***".upper())
        verificar_boleto = input("Ingrese el codigo de su boleto: ")
        for boletos in boleto_lista: #for para ingresar a la lista donde se guardan los voletos y recorrerla 
            if verificar_boleto == boletos: #si verificar_boleto es igual a boletos significa que cuando el for recorrio la lista encontro el boleto que un cliente tiene por lo tanto es verdadero 
                ver_partido = comprar_partido
                for partido in partidos_totales:
                    if ver_partido == str(partido.id):
                        ""
                # si ver_partido es igual al id del partido x imprimira:
                print("\n***Boleto valido*** Bienvenido!")
                boleto_lista.remove(boletos)
            else:
                #si ver_partido no es igual al id del partido x imprimira:
                print("Boleto no valido :( ")                    

    # Indicadores de gestión (Estadísticas)
    elif opcion == "6":
        #if por si el usuario desea ver las estadisticas
        print("\n***Bienvenido a las estadisticas!***".upper())
        #promedio de cuanto gasta un cliente vip entre entradas y restaurante
        if vip_tot == 0:
            print("\nNo hay nada que promediar :( ")
        else:
            print(f"\n*El gasto promedio de un cliente vip es: {vip_gastado/vip_tot}\n") #Para esto se utilizaron contadores que vayan sumando el precio total de los vips en todo lo que gastan y dividirlo entre la cantidad de vips que hay

        #partido con mayor boletos vendidos (no funciona xd )
        # for x in clientes:
        #     if comprar_partido == entrada.id: #si comprar_partido es igual al id appendeara la cantidad de boletos que se hayan comprado y luego sacara la max cantidad de boletos
        #         boleto_cantidad_lista.append(int(cantidad_boleto))
        #         max_boleto = max(boleto_cantidad_lista)
                # print(f"*El partido con mayor boletos vendidos fue el {x.id} con {max_boleto} boletos vendidos")







        