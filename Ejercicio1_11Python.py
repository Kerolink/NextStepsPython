# 1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero. 
# El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.
from datetime import datetime
print("Introduzca una fecha en formato dd/mm/aaaa:")
fecha = input()
x = 1
while x == 1:
  try:
    obj = datetime.strptime(fecha, "%d/%m/%Y").date()
    print(f"{obj.year}-{obj.month}-{obj.day}")
    x = 0 
  except:
    print("La fecha introducida es errónea")
    print("Introduzca una fecha en formato dd/mm/aaaa:")
    fecha = input()
print("El programa ha finalizado")
