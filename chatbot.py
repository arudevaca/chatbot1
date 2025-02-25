
horario_libre = "Me encuentro disponible los martes, miercoles y jueves de 16 a 19hs"

saludo = input("Hola, qué tal? ")
nombre = input("Cuál es tu nombre? ")
print(horario_libre)
dia = str(input("Qué día te queda bien? (sin acentos) ")).lower()


if dia == "martes" or dia == "miercoles" or dia == "jueves":
    hora = int(input("Qué hora te queda bien? (solo números): "))
    if hora >= 16 and hora <= 19:
        print(f"Listo, nos vemos el {dia} a las {hora}!!")
    elif hora < 16 or hora > 19:
        print("Lo siento, no estoy disponible a esa hora! Solo de 16 a 19hs")
else: 
    print("Lo siento. ", horario_libre)

