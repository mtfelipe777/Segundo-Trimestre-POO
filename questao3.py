class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo
    def __add__(self, valor_yuan):
        self.saldo += valor_yuan
        print("Saldo atual:", self.saldo)
    def __sub__(self, valor_yuan):
        self.saldo -= valor_yuan
        print("Saldo atual:", self.saldo)


print("****Opções de moeda:****")
print("1. USD")
print("2. BRL")
opcao = int(input("Informe a opção de moeda: "))

if opcao == 1:
    carteira = Carteira("USD", float(input("Informe seu saldo: ")) * 0.14)
elif opcao == 2:
    carteira = Carteira("BRL", float(input("Informe seu saldo: ")) * 0.85)
else:
    print("Viajou")
    exit()

print("****Operadores****")
print("1. Soma")
print("2. Subtração")
print("3. Sair")

while True:
    operadores = int(input("Informe a operação: "))
    if operadores == 1:
        valor = float(input("Informe o valor: "))
        carteira.__add__(valor)
    elif operadores == 2:
        valor = float(input("Informe o valor: "))
        carteira.__sub__(valor)
    else:
        break