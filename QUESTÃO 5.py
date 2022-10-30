nh = int(input('Insira um número maior que 50 para calcular o H: '))

while nh < 50:
    nh = int(input('Você inseriu um número menor que 50. Por favor, insira um número maior que 50 para calcular o H: '))

h = 1

while nh > 1:

    if nh%2 == 0:
        h += (nh*2-1)/nh

    if nh%2 == 1:
        h -= (nh*2-1)/nh

    nh -= 1

ns = int(input('Insira um número maior que 50 para calcular o S: '))

while ns < 50:
    ns = int(input('Você inseriu um número menor que 50. Por favor, insira um número maior que 50 para calcular o S: '))

s = 1

while ns > 1:

    if ns%2 == 0:
        s -= ns/(ns*ns)

    if ns%2 == 1:
        s += ns/(ns*ns)
    
    ns -= 1


np = int(input('Insira um número maior que 50 para calcular o P: '))

while np < 50:
    np = int(input('Você inseriu um número menor que 50. Por favor, insira um número maior que 50 para calcular o P: '))

p2 = 0
div = 1

for i in range(2, np+1):
    p = 2
    primo = True
    while p < i:
        if i%p == 0:
            primo = False
            break
        p += 1

    if primo:
        p2 += i/(div**3)
        div += 2


print (f'O resultado de H é = {h}\nO resultado de S é = {s}\nO resultado de P é = {p2}')
