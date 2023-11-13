#Complejo Futbolístico “Los Mejengueros”
print("\t======================================================")
print("\tBienvenido al Complejo Futbolístico “Los Mejengueros”")
print("\t======================================================\n")


# ====================== Módulo 1: Módulo de Clientes ======================
def modulo_cliente():
    Menu("Menu módulo cliente")

def crear_cuenta():
    print("\n\tCREAR CUENTA\n")
    identificacion = input("\tDigite su número de identificación: \n\t")
    nombre = input("\tDigite su nombre: \n\t")
    primerApellido = input("\tDigite su primer apellido: \n\t")
    segundoApellido = input("\tDigite su segundo apellido: \n\t")
    telefono = input("\tDigite su número de telefono: \n\t")
    correo = input("\tDigite su correo: \n\t")
    estado = "inactivo"

def editar_perfil():
    print("\n\tACTUALIZAR DATOS PERSONALES\n")
    identificacion = input("\tDigite su numero de identificación: \n\t")
    nombre = input("\tDigite su nombre: \n\t")
    primerApellido = input("\tDigite su primer apellido: \n\t")
    segundoApellido = input("\tDigite su segundo apellido: \n\t")
    telefono = input("\tDigite su número de telefono: \n\t")
    correo = input("\tDigite su correo: \n\t")
    estado = "inactivo"

def consultar_datos_usuario():
    print("\n\tDATOS DEL CLIENTE\n")
    identifiacion = input("\tDigite su número de identificación: ")

def lista_reserva():
    print("\n\tLISTA DE RESERVAS\n")
    identificacion = input("\tDigite su número de identificación para visualizar sus reservas: ")


# ====================== Módulo 2: Módulo de Administrador =====================
def modulo_administrador():
    Menu("Menu módulo  activar cliente")
def activar_cliente():
    print("activar cliente")
def revisar_reservas():
    print("Revisar reservas")

# ================== Módulo 3: Módulo de Reserva Descripción ================
def modulo_reserva():
    print("Modulo reserva")

#==================================   Menu   ===================================
def generador_opcion(num):
    data=[]
    for i in range(num):
        data += [i+1]

    print("\tSelecione una opcion",data," ")
    opcion = int(input("\t"))
    return opcion

def Menu(menu):
    for i in range(len(MENU[menu])):
        print("\t[",i+1,"]",MENU[menu][i][0])
    
    opcion = generador_opcion(len(MENU[menu]))

    print("\t",MENU[menu][i][0])


    MENU[menu][opcion-1][1]()

MENU = {
    "Menu principal": [
        ["Módulo cliente", modulo_cliente],
        ["Módulo administrador",modulo_administrador],
        ["Módulo reserva",modulo_reserva]
    ],
    "Menu módulo cliente":[
        ["Crear cuenta" , crear_cuenta],
        ["Editar perfil", editar_perfil],
        ["Consultar dato usuario", consultar_datos_usuario],
        ["Lista reserva", lista_reserva]
    ],
      "Menu módulo  activar cliente":[
        ["Activar cliente" , activar_cliente],
        ["Revisar reservas", revisar_reservas]
    ]
}

# inicio del programa
Menu("Menu principal")