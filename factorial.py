# -*- coding: utf-8 -*-

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

if __name__ == "__main__":
    numero = int(input('Escribe un numero para sabe su factorial: '))
  
    factorial(numero)
    result = factorial(numero)
    print(result)