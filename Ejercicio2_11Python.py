# 2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. 
# El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.
def principal():
        from datetime import datetime, timedelta
        from pytz import timezone
        import pytz

        print("Selecciona tu zona horaria de entre las siguientes:")
        print(pytz.all_timezones)
        zona = input ()
        while zona not in pytz.all_timezones:
                print("La zona horaria introducida no es válida")
                zona = input ()
        print(f"Hora en {zona}: {datetime.now(pytz.timezone(zona)).hour}:{datetime.now(pytz.timezone(zona)).minute}")
        print("El programa ha finalizado")