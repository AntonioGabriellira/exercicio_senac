class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def exibir(self, indice = 0):
        print(f" {indice} === produto: {self.nome} -- preço: {self.preco} -- quantidade: {self.qtd}")

produto_um = Produto("massa", 5, 400)
produto_dois = Produto("tomate", 2, 100)
produtos = [produto_um, produto_dois]
for produto in produtos:
    indice = produtos.index(produto)
    produto.exibir(indice)
preco = int(input("preço do produto: "))
qtd = int(input("digite a quantidade: "))
indice_selecionado = int(input("selecione o produto: "))
if indice_selecionado > len(produtos) - 1:
    print("produto não encontrado")
else:
    produto = produtos[indice_selecionado]
    quantidade = int(input("digite a quantidade: "))
    print(f"o valor total é: {quantidade * produto}")