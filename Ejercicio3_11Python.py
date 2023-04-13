# 3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene.
# El programa debe utilizar un bucle while para recorrer la cadena y contar las palabras.
print("Introduce una cadena de caracteres:")
cadena = input()
palabras = 1
while len(cadena)<1:
    print("La cadena de caracteres introducida no es válida")
    print("Introduce una cadena de caracteres:")
    cadena = input()
for letra in cadena:
    if letra == " ":
        palabras += 1
print("La cadena tiene", palabras, "palabras")
print("El programa ha finalizado")
