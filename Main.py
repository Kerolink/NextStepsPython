import os
import sys
#from Varios import principal

from Ejercicios import Ejercicio1_11Python
from Ejercicios import Ejercicio2_11Python
from Ejercicios import Ejercicio3_11Python
from Ejercicios import Ejercicio4_11Python
from Ejercicios import Ejercicio5_11Python
from Ejercicios import Ejercicio6_11Python
from Ejercicios import Ejercicio7_11Python
from Ejercicios import Ejercicio8_11Python
from Ejercicios import Ejercicio9_11Python
from Ejercicios import Ejercicio10_11Python
from Ejercicios import Ejercicio11_11Python


while True:
    if sys.platform.startswith("linux"):
        # linux
        os.system('clear') 
    elif sys.platform == "darwin":
        # MAX OS X
        os.system('clear') 
    elif os.name == "nt":
        #Windows, Cigwyin, etc. (32/64-bit)
        os.system('cls') 
    # os.system("cls") #Limpia la pantalla en la consola
    # os.system("clear") #Limpia pantalla consola MAC y Linux
    
    print("Bienvenidos")
    print("Menu principal")

    print("1-Cambiar formato fecha")
    print("2-Hora actual en zona horaria específica")
    print("3-Devolver número palabras cadena de texto")
    print("4-Hora en formato 24horas")
    print("5-Invertir cadena de caracteres")
    print("6-Cálculo de número desde 1 hasta el número")
    print("7-Imprimir caracteres en líneas separadas")
    print("8-Cadenas con más de 5 caracteres")
    print("9-Cadena ocurrencias reemplazadas")
    print("10-Cadenas con al menos una vocal")
    print("11-Mostrar solo numeros multiplos de 3")

    print("0-Salir")

    opcion = input("Seleccione una opción:")

    if opcion == "1":
        Ejercicio1_11Python.principal()
    elif opcion == "2":
        Ejercicio2_11Python.principal()
    elif opcion == "3":
        Ejercicio3_11Python.principal()
    elif opcion == "4":
        Ejercicio4_11Python.principal() 
    elif opcion == "5":
        Ejercicio5_11Python.principal() 
    elif opcion == "6":
        Ejercicio6_11Python.principal() 
    elif opcion == "7":
        Ejercicio7_11Python.principal()
    elif opcion == "8":
        Ejercicio8_11Python.principal()     
    elif opcion == "9":
        Ejercicio9_11Python.principal() 
    elif opcion == "10":
        Ejercicio10_11Python.principal() 
    elif opcion == "11":
        Ejercicio11_11Python.principal() 


    elif opcion == "0":
        print("Un placer atenderle. Chao!")
        break

    continuar=input("Presione enter para continuar...")