class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo
    def __add__(self, valor_yuan):
        self.valor_yuan = valor_yuan
        self.saldo += self.valor_yuan
        print(self.saldo)
    def __sub__(self, valor_yuan):
        self.saldo -= self.valor_yuan
        print(self.saldo)        
print("****Opções de moeda:****")
print("1.USD;")
print("2.BRL.")
opcao = int(input("Informe a opção de moeda"))
if opcao == 1:
    carteira_usd = Carteira("USD", float(input("Informe seu saldo: "))*0.14)
elif opcao == 2:
    carteira_brl = Carteira("BRL", float(input("Informe seu saldo: "))*0.85)
else:
    print("Viajou")
print("****Operadores****")
print("1.Soma;")
print("2.Subtração.")
while True:
    if opcao == 1:
        operadores = int(input("Informe a operação: "))
        if operadores == 1:
            carteira_usd.__add__()
        elif operadores == 2:
            carteira_usd.__sub__()
        else:
            break
    elif opcao == 2:
        operadores = int(input("Informe a operação: "))
        if operadores == 1:
            carteira_brl.__add__()
        elif operadores == 2:
            carteira_brl.__sub__()
        else:
            break
