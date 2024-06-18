
from Ingrediente import Ingrediente

class Base(Ingrediente):
  def __init__(self, sabor: str, precio: int, calorias: int, nombre: str, inventario: int, es_vegetariano: bool):
    super().__init__(precio, calorias, nombre, inventario, es_vegetariano)
    self.sabor = sabor

  def abastecer(self):
    self.inventario = self.inventario + 5