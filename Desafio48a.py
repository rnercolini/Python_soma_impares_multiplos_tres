# Retorna a soma dos números ímpares, múltiplos de 3, entre 1 e 500.
s = 0
for c in range(0, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print('\033[34mA soma dos números impares, múltiplos de 3, entre 1 e 500 é\033[m \033[31m{}\033[m'.format(s))
