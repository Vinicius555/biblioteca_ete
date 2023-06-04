import re


def validar_email(email):
    while True:
        padrao = r"^[\w\.-]+@[\w]+\.[a-zA-Z]{2,}$"
        if re.match(padrao, email):
            break
        else:
            print("Email inválido!")
            pass
