n = -1

while n < 0 or n > 10:
    n = int(input('Digite um valor de 0 a 10: '))

    if n < 0 or n > 10:
        print('valor inválido')

print('Valor igual a: ', n)