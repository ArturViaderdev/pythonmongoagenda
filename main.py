class Persona:
  nombre=""
  telefono=""
  def __init__(self):
    self.nombre=""
    self.telefono=""




def menu_principal():
  opciones = {
    '1': ('Alta persona', alta),
    '2': ('Lista personas', lista),
    '3': ('Busca persona', busca),
    '4': ('Borra persona', borra),
    '5': ('Salir', salir)
  }

  generar_menu(opciones, '5')

def generar_menu(opciones, opcion_salida):
  opcion = None
  while opcion != opcion_salida:
    mostrar_menu(opciones)
    opcion = leer_opcion(opciones)
    ejecutar_opcion(opcion, opciones)
    print()  # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
  print('Seleccione una opción:')
  for clave in sorted(opciones):
    print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
  while (a := input('Opción: ')) not in opciones:
    print('Opción incorrecta, vuelva a intentarlo.')
  return a

def ejecutar_opcion(opcion, opciones):
  opciones[opcion][1]()

def alta():
  persona = Persona()
  persona.nombre=input("Introduce el nombre:")
  persona.telefono=input("Introduce el teléfono:")
  mipersona = {"nombre": persona.nombre,"telefono":persona.telefono}
  customers.insert_one(mipersona)
  print('Añadido')

def lista():
  for x in customers.find():
    print(x)
    print(x.get('nombre'))
    print(x.get('telefono'))

def busca():
  print('Has elegido la opción 3')

def borra():
  print('Has elegido la opción 4')

def salir():
  print('Saliendo')

import pymongo  # package for working with MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["agenda"]
customers = db["persona"]
menu_principal()

