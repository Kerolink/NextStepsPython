# 6. Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado.
# El programa debe utilizar un bucle `for` para sumar los números.
def principal():
    x = 1
    i = 1
    suma = 0
    while x == 1:
        print("Introduce un número entero:")
        nume = input()
        try:
            nume = int(nume)
            x = 0
        except:
            print("El número introducido es erróneo")
    while i <= nume:
        suma += i
        i += 1
    print("La suma es de", suma)
    print("El programa ha finalizado")
