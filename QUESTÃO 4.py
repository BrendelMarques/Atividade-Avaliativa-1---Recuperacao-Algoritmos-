SEQUENCIACRESCENTE, SEQUENCIACRESCENTE_max, SEQUENCIACONSTANTE, SEQUENCIACONSTANTE_max, x = 0, 0, 0, 0, 1

num1 = int(input(f'Digite o número {x}: '))
while (x < 150):

    x +=1
    num2 = int(input(f'Digite o número {x}: '))

    if num1 < num2:
        SEQUENCIACRESCENTE += 1

        if SEQUENCIACRESCENTE >= SEQUENCIACRESCENTE_max:
            SEQUENCIACRESCENTE_max = SEQUENCIACRESCENTE + 1

    if num1 > num2:
        SEQUENCIACRESCENTE = 0
        elem_seq = ''

    if num1 == num2:
        SEQUENCIACONSTANTE +=1

        if num1 > elem_igual:
            elem_igual = num1

        if SEQUENCIACONSTANTE >= SEQUENCIACONSTANTE_max:
            SEQUENCIACONSTANTE_max = SEQUENCIACONSTANTE + 1

    if num1 != num2:
        SEQUENCIACONSTANTE = 0

    num1 = num2

if (SEQUENCIACRESCENTE_max > 0):
    print(f'MAIOR SEQUENCIA EM ORDEM CRESCENTE: {SEQUENCIACRESCENTE_max}')
else:
    print('NAO EXISTE SEQUENCIA EM ORDEM CRESCENTE')

if (SEQUENCIACONSTANTE_max > 0):
    print(f'MAIOR SEQUENCIA DE NUMEROS CONSTANTES: {SEQUENCIACONSTANTE_max}')
else:
    print('NAO EXISTE SEQUENCIA DE NUMEROS CONSTANTES')
