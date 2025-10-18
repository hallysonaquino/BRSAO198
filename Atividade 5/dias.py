from datetime import date, datetime

print("Digite sua data de nascimento (DD/MM/AAAA):")
dia_nasc = input("Dia: ")
mes_nasc = input("Mes: ")
ano_nasc = input("Ano: ")

data_nascimento_str = dia_nasc + "/" + mes_nasc + "/" + ano_nasc

try:
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    data_atual = date.today()
    
    diferenca = data_atual - data_nascimento
    dias_vividos = diferenca.days
    
    print("===================================")
    print("Data de Nascimento:", data_nascimento_str)
    print("Data de Hoje:", data_atual.strftime("%d/%m/%Y"))
    print("-----------------------------------")
    print("O individuo esta vivo a:")
    print(dias_vividos, "dias")
    print("===================================")

except:
    print("===================================")
    print("ERRO: Uma das datas nao foi digitada direito ou e invalida.")
    print("Tente de novo seguindo o formato DD/MM/AAAA.")
    print("===================================")