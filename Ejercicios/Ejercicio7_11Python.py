# 7. Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada.
# El programa debe utilizar un bucle `for` para recorrer la cadena.
def principal():
    print("Introduce una cadena de caracteres:")
    cadena = input()
    for letra in cadena:
        print(letra)
    print("El programa ha finalizado")