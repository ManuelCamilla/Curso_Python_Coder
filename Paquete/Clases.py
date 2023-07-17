# Definición Clase Cliente heredada de la Clase Personacls

class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno, rut, edad, genero):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.rut = rut
        self.edad = edad
        self.genero = genero
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno} - Rut: {self.rut}"

class Cliente(Persona):
    def __init__(self, nombre, apellido_paterno, apellido_materno, rut, edad, genero, cod_cliente, email, telefono, direccion):
        super().__init__( nombre, apellido_paterno, apellido_materno, rut, edad, genero)
        self.cod_cliente = cod_cliente
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.compras = {}

    def compra(self, cantidad, producto):
        print(f"{self.nombre} {self.apellido_paterno} ha comprado {cantidad} {producto}.")

    
# Definición Clase Productos

class Producto:
    def __init__(self, SKU, nombre, precio):
        self.SKU = SKU
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)

class CajaEliteEntrenador(Producto):
    def __init__(self, SKU, nombre, precio, contenido):
        super().__init__(SKU, nombre, precio)
        self.contenido = contenido

    def mostrar_info(self):
        super().mostrar_info()
        print("Contenido: ", self.contenido)

class Sobre(Producto):
    def __init__(self, SKU, nombre, precio, cantidad_cartas):
        super().__init__(SKU, nombre, precio)
        self.cantidad_cartas = cantidad_cartas

    def mostrar_info(self):
        super().mostrar_info()
        print("Cantidad de cartas: ", self.cantidad_cartas)

class Carta(Producto):
    def __init__(self, SKU, nombre, precio, rareza):
        super().__init__(SKU, nombre, precio)
        self.rareza = rareza

    def mostrar_info(self):
        super().mostrar_info()
        print("Rareza: ", self.rareza)



