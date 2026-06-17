class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura
    def __str__(self):
        return f"Seu nome é {self.nome} e sua altura é {self.altura}"
    def __gt__(self, other):
       return self.altura > other.altura
    def __lt__(self, other):
        return self.altura < other.altura
nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura: "))
pessoinha = Pessoa(nome, altura)
other_name = input("Informe o outro nome: ")
other_high = float(input("Informe a outra altura: "))
other_people = Pessoa(other_name, other_high)
print(pessoinha)
print(pessoinha > other_people)
print(pessoinha < other_people)

