#Funcion que determina si ingrediente es sano

def esSano(calorias: int, vegetariano: bool):
  if vegetariano == True or calorias < 100:
    return True
  else:
    return False

#Funcion que calcula las calorias de un producto

def calcularCalorias(listaDeCalorias: list):
  sumaCalorias = 0
  for index in range(len(listaDeCalorias)):
    sumaCalorias = sumaCalorias + listaDeCalorias[index]
  totalCalorias = sumaCalorias * 0.95
  return round(totalCalorias, 2)

ingredientes = [
{ 
  "nombre": "Helado de Fresa",
  "precio": 1200
},
{
  "nombre": "Chispas de chocolate",
  "precio": 500
},
{
  "nombre": "Mani Japones",
  "precio": 900
}
]

#Funcion que determina el costo del producto

def calcularCostoProducto(ingredientes: tuple):
  totalCostoProducto = 0
  for index in range(len(ingredientes)):
    totalCostoProducto = totalCostoProducto + ingredientes[index]["precio"]
  return totalCostoProducto

#Funcion que determina la rentabilidad del producto

def calcularRentabilidadProducto(ingredientes: tuple, precio: int):
  totalCostoProducto = 0
  for index in range(len(ingredientes)):
    totalCostoProducto = totalCostoProducto + ingredientes[index]["precio"]
  rentabilidadProducto = precio - totalCostoProducto
  return rentabilidadProducto

productos = [
{
  "nombre": "Samurai de fresas", 
  "rentabilidad": 4900
},
{
  "nombre": "Samurai de mandarinas", 
  "rentabilidad": 2500
},
{
  "nombre": "Malteda chocoespacial",
  "rentabilidad": 11000
},
{
  "nombre": "Cupihelado", 
  "rentabilidad": 3200
},
]

def mejorMasRentable(productos: tuple):
  mejorProducto = ""
  rentabilidad = 0
  for index in range(len(productos)):
   if rentabilidad < productos[index]["rentabilidad"]:
     rentabilidad = productos[index]["rentabilidad"]
     mejorProducto = productos[index]["nombre"]
  return mejorProducto