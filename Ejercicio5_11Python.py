# 5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh").
# El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.
print("Introduce una cadena de caracteres:")
cadena = input()
i = 0
letrinv = ""
cadinv = ""
for letra in cadena:
    letrinv = cadena[-i-1]
    i += 1
    cadinv += letrinv
print(cadinv)
print("El programa ha finalizado")