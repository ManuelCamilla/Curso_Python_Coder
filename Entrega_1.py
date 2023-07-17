
#Importación Librerias y definición de Ruta
ruta = "C:/Users/Manuel Camilla/OneDrive/Escritorio/Curso Python/Entregas/Segunda Entrega/Paquete"

# Definición Función para Registrar Usuario

def registrar_usuario(diccionario):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    diccionario[usuario] = contraseña
    guardar_registro(diccionario)
    print("Registro exitoso.")

# Definición Función para Guardar Registro de Usuario

def guardar_registro(diccionario):
    with open(ruta +"BD_Usuarios.txt", "w") as archivo:
        for usuario, contraseña in diccionario.items():
            archivo.write(f"{usuario},{contraseña}\n")

# Definición Función para Mostrar Registro de Usuario

def mostrar_registros(diccionario):
    with open(ruta +"BD_Usuarios.txt", "r") as archivo:
        for linea in archivo:
            usuario, contraseña = linea.strip().split(",")
            diccionario[usuario] = contraseña

    print("Registros almacenados:")
    for usuario, contraseña in diccionario.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

# Definición Función para Comprobar el Inicio de Sección de un Usuario

def login(diccionario):
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in diccionario and diccionario[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Definición Función para Mostar Menú de Registro de Base de Datos

def menu():
    registros = {}
    opcion = ""
    while opcion != "4":
        print("\n === Menú ===")
        print("1. Registrar usuario")
        print("2. Mostrar registros")
        print("3. Iniciar sesión")
        print("4. Salir")
        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            registrar_usuario(registros)
        elif opcion == "2":
            mostrar_registros(registros)
        elif opcion == "3":
            login(registros)
        elif opcion == "4":
            print("Adiós")
        else:
            print("Opción inválida. Intente nuevamente.")


menu()