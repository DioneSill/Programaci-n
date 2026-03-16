def es_valido(email):
    return "@" in email

def verificar_email():
    email = input("Ingresa tu dirección de email: ")
    if es_valido(email):
        print("La dirección es válida")
    else:
        print("La dirección NO es válida")

verificar_email()