idade = int(input("Diga a sua idade em numeros inteiros: "))

if idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print("Sua Idade:", idade)
print("Voce foi classificado como:", categoria)
