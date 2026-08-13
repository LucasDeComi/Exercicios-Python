produtos = []

class Produto:
    def __init__(self, nome, preco):
        self.codigo = len(produtos) + 1
        self.nome = nome
        self.preco = preco
    
    def exibir(self):
        print(f"Código do produto: {self.codigo}")
        print(f"Nome do produto: {self.nome}")
        print(f"Preço do produto: {self.preco}")

def cadastrar():
    try:
        nome = input("Insira o nome do produto: ").strip()
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        
        preco = float(input("Insira o preço do produto: "))
        if preco < 0:
            raise ValueError("O preço deve ser um número positivo.")
        
        novoProduto = Produto(nome, preco)
        produtos.append(novoProduto)
        print("Produto cadastrado com sucesso!")
    except ValueError as e:
        print(e)

produtos.append(Produto("1", 1))

def listar():
    for produto in produtos:
        produto.exibir()
        
listar()