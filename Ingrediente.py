class Ingrediente:
  pass
  def __init__(self, precio: int, calorias: int, nombre: str, inventario: int, es_vegetariano: bool):
    self.precio = precio
    self.calorias = calorias
    self.nombre = nombre
    self.inventario = inventario
    self.es_vegetariano = es_vegetariano
    
  def es_sano(self):
    if self.es_vegetariano == True or self.calorias < 100:
      return True
    else:
      return False
    
  def abastecer(self):
    pass