produto = "Camiseta"
preco_original = 50.00
desconto_porcentagem = 20
desconto_decimal = desconto_porcentagem / 100
valor_desconto = preco_original * desconto_decimal
preco_final = preco_original - valor_desconto
print("LOJA DE DESCONTOS MANEIROS")
print("Produto:", produto)
print("Preco Original: R$", preco_original)
print("Desconto:", desconto_porcentagem, "%")
print("Valor do Desconto: R$", valor_desconto)
print("PRECO FINAL: R$", preco_final)