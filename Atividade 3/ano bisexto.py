ano_str = input("Mande um ano em numero inteiro: ")
ano = int(ano_str)

bissexto = False

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            bissexto = True
        else:
            bissexto = False
    else:
        bissexto = True
else:
    bissexto = False

print("O ano digitado foi:", ano)

if bissexto:
    print("RESPOSTA: SIM, e um ano bissexto.")
else:
    print("RESPOSTA: NAO, nao e um ano bissexto.")
