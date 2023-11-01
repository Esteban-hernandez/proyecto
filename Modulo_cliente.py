# Módulo 1: Módulo de Clientes   	
# Descripción 

# A)  i.	Registrar un nuevo cliente, solicitando la siguiente información:

# 1.	Identificación.
# 2.	Nombre
# 3.	Primer Apellido
# 4.	Segundo Apellido.
# 5.	Teléfono
# 6.	Correo
# 7.	Activo o Inactivo (Por defecto Inactivo)

# En este módulo se podrá realizar lo siguiente:

# ii. Actualizar un cliente existente: Permitiendo modificar toda la información del cliente, únicamente dejando intacto la Identificación.

#iii.	Consultar un cliente: Solicitando la identificación, desplegará la información básica del cliente.

#iv.	Listado de reservas: mediante el cual el cliente podrá revisar las reservas que ha realizado en el complejo.


#Complejo Futbolístico “Los Mejengueros”
print("\t======================================================")
print("\tBienvenido al Complejo Futbolístico “Los Mejengueros”")
print("\t======================================================\n")

#Menu Principal

print("\t======================================================")
print("\tMenu principal")
print("\t======================================================\n")
print("\t[1] Módulo de Clientes")
print("\t[2] Módulo de Administrador")
print("\t[3] Módulo de Reserva")
print("\t[4] Módulo de Informes")
print("\t[5] Salir")

ciclo_menu_principal = True
while ciclo_menu_principal == True:
    modulo = input("\tSeleccione un modulo (1,2,3,4,5)  ")
    if modulo == "1":
        modulo = "clientes"
        ciclo_menu_principal = False
    elif modulo == "2":
        modulo = "administrador"
        ciclo_menu_principal = False
    elif modulo == "3":
        modulo = "reservas"
        ciclo_menu_principal = False
    elif modulo == "4":
        modulo = "informes"
        ciclo_menu_principal = False
    elif modulo == "5":
        modulo = "salir"
        ciclo_menu_principal = False
    else:
        print("\tEl modulo ",modulo," no es valido. intente de nuevo\n")
    
    if modulo == "clientes" or modulo == "administrador" or modulo == "reservas" or modulo == "informes":
        print("\t======================================================")
        print("\tModulo ",modulo)
        print("\t======================================================\n")


#Menu Módulo de Clientes 
print("\tMenu")
print("\t[1] Registrarse")
print("\t[2] Actualizar un cliente existente")
print("\t[3] Consultar un cliente")
print("\t[4] lista de reservas")
print("\t[5] Salir")

ciclo_menu_clientes = True
while ciclo_menu_clientes == True:
    opcion_menu_cliente = input("\tSeleccione una opcion (1,2,3,4,5)  ")
    if opcion_menu_cliente == "1":
        opcion_menu_cliente = "registrarse"
        ciclo_menu_clientes = False
    elif opcion_menu_cliente == "2":
        opcion_menu_cliente = "actualizar"
        ciclo_menu_clientes = False
    elif opcion_menu_cliente == "3":
        opcion_menu_cliente = "consultar"
        ciclo_menu_clientes = False
    elif opcion_menu_cliente == "4":
        opcion_menu_cliente = "lista_reservas"
        ciclo_menu_clientes = False
    elif opcion_menu_cliente == "5":
        ciclo_menu_clientes = False
    else:
        print("\tLa opcion ",opcion_menu_cliente," no es valido. intente de nuevo\n")


#Registraser
if modulo == "clientes" and opcion_menu_cliente == "registrarse":
    print("\n\tCREAR CUENTA\n")
    
    identificacion = input("\tDigite su nemro de identificacion: \n\t")
    nombre = input("\tDigite su nombre: \n\t")
    primerApellido = input("\tDigite su primer apellido: \n\t")
    segundoApellido = input("\tDigite su segundo apellido: \n\t")
    telefono = input("\tDigite su numero de telefono: \n\t")
    correo = input("\tDigite su correo: \n\t")
    estado = "inactivo"

#Actualizar dato del cliente
elif modulo == "clientes" and opcion_menu_cliente == "actualizar":
    print("\n\tACTUALIZAR DATOS PERSONALES\n")

    identificacion = input("\tDigite su nemro de identificacion: \n\t")
    nombre = input("\tDigite su nombre: \n\t")
    primerApellido = input("\tDigite su primer apellido: \n\t")
    segundoApellido = input("\tDigite su segundo apellido: \n\t")
    telefono = input("\tDigite su numero de telefono: \n\t")
    correo = input("\tDigite su correo: \n\t")
    estado = "inactivo"

#Consultar un cliente
if modulo == "clientes" and opcion_menu_cliente == "consultar":
    print("\n\tDATOS DEL CLIENTE\n")

#Listado de reservas
if modulo == "clientes" and opcion_menu_cliente == "lista_reservas":
    print("\n\tLISTA DE RESERVAS\n")