import re


def valida_float(string):
    regex = re.compile(r"^[+-]?\d+(?:\.?\d+)?$")
    if regex.search(string):
        return True
    return False


def valida_int(string):
    regex = re.compile(r"^[+-]?\d+$")
    if regex.search(string):
        return True
    return False


while True:
    caracter = input('digite um numero: ')

    if valida_int(caracter):
        numero = int(caracter)
        print(f'A string "{caracter}" foi convertida para {type(numero)}\n\n')
        continue

    elif valida_float(caracter):
        numero = float(caracter)
        print(f'A string "{caracter}" foi convertida para {type(numero)}\n\n')
        continue
    else:
        print(f'A string "{caracter}" não pode ser convertida para um numero!')