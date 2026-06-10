class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo

    def adicionar(self, valor_yuan):
        self.saldo += valor_yuan
        print(f"Saldo atualizado: {self.saldo}")

    def subtrair(self, valor_yuan):
        self.saldo -= valor_yuan
        print(f"Saldo atualizado: {self.saldo}")

print("****Opções de moeda:****")
print("1. USD;")
print("2. BRL.")
opcao = int(input("Informe a opção de moeda: "))

if opcao == 1:
    saldo_inicial = float(input("Informe seu saldo: "))
    carteira = Carteira("USD", saldo_inicial * 0.14)
elif opcao == 2:
    saldo_inicial = float(input("Informe seu saldo: "))
    carteira = Carteira("BRL", saldo_inicial * 0.85)
else:
    print("Opção inválida!")
    carteira = None

if carteira:
    print("****Operadores****")
    print("1. Soma (Adicionar Yuan);")
    print("2. Subtração (Subtrair Yuan);")
    print("3. Sair.")
    
    while True:
        operacao = int(input("Informe a operação: "))
        
        if operacao == 1:
            valor = float(input("Informe o valor Yuan a adicionar: "))
            carteira.adicionar(valor)
        elif operacao == 2:
            valor = float(input("Informe o valor Yuan a subtrair: "))
            carteira.subtrair(valor)
        elif operacao == 3:
            print("Saindo...")
            break
        else:
            print("Operação inválida!")