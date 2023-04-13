# 4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30"). 
# La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.
def principal():
    x = 0
    while x == 0:
        print("Introduce una hora en formato hh:mm")
        husuario = input()
        if len(husuario) != 5 or husuario[2]!=":":
            print("La hora introducida no es correcta")
            continue
        hu = husuario[:2]
        mu = husuario[3:]
        try:
            hu = int(hu)
            mu = int(mu)
            x = 1
        except:
            print("La hora introducida no es correcta")
            continue
    print(f"La nueva hora es {hu}:{mu}")
    print("El programa ha finalziado")

