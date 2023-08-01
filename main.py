import random # importamos la librerias
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = minus.upper()
numbers = "0123456789"
symbols = "|°!@#$%&/()=?'¡¿{}[]"

base = minus+mayus+numbers+symbols # Se agregan todos los caracteres para concatenarlos.
longitud = 12  # La idonea para cada uso.

for _ in  range(5):  # De esta manera podemos generar la cantidad de contraseñas que deseemos modificando su numero.
    muestra = random.sample(base, longitud)
    password = "".join(muestra) # Utilizamos JOIN para concatenar los datos.
    encryptPass = generate_password_hash(password)  # implementamos el Werkzeug Security Hash
    print("{} => {}".format(password, encryptPass))

