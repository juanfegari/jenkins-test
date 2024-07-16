class Personas:
    def __init__(self,nombre,edad,ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def saludo(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad}. Vivo en {self.ciudad}"
    
class Pedido:
    def __init__(self,producto,cantidad,estado):
        self.producto = producto
        self.cantidad = cantidad
        self.estado = estado
    
    def info(self):
        return f"Pedido de {self.producto} por {self.cantidad} unidades, estado: {self.estado}"