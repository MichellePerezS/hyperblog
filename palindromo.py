#-*- coding: utf-8 -*-
def palindromo2(palabra):
    palabra_reves = palabra[::-1]

    if palabra_reves == palabra:
        return True
    return False    

def palindromo(palabra):
    letra_reves =[]
    for letra in palabra:
        letra_reves.insert(0,letra)
    palabra_reves = ''.join(letra_reves)

    if palabra_reves == palabra:
        return True
    return False


if __name__ == "__main__":
    palabra = str(input('Escribe una palabra'))

    result =palindromo2(palabra)

    if result is True:
        print('{} sí es un palíndromo.'.format(palabra))
    else:
        print('{} no es un palíndromo.'.format(palabra)) 