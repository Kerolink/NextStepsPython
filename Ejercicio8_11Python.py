# 8. Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres. 
# El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.
def principal():
    cadenas = list()
    cadcinco = list()
    palabra = "aleatorio"
    while len(palabra)>1:
        print("Introduzca una nueva cadena de caracteres")
        palabra = input()
        cadenas.append(palabra)
    for pal in cadenas:
        if len(pal)>5:
            cadcinco.append(pal)
    print(cadcinco)
    print("El programa ha finalizado")
