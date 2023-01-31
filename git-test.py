class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

nome = input("nome do produto: ")
preco = int(input("preço do produto: "))
qtd = int(input("digite a quantidade: "))
produto = Produto(nome, preco, qtd)