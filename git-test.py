class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def exibir(self):
        print(f" produto: {self.nome} -- preço: {self.preco} -- quantidade: {self.qtd}")

nome = input("nome do produto: ")
preco = int(input("preço do produto: "))
qtd = int(input("digite a quantidade: "))
produto = Produto(nome, preco, qtd)