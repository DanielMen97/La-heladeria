from Ingrediente import Ingrediente

class Componente(Ingrediente):
  def __init__(self, precio: int, calorias: int, nombre: str, inventario: int, es_vegetariano: bool):
    super().__init__(precio, calorias, nombre, inventario, es_vegetariano)

  def abastecer(self):
    self.inventario = self.inventario + 10

