produtos = []
sistemaAtivo = True
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
        nome = input("\nInsira o nome do produto: ").strip()
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

def listar():
    for produto in produtos:
        print("\n")
        produto.exibir()
        
def comprar():
    try:
        codigo = int(input("Insira o nome do produto: "))
        if not codigo || codigo <= 0:
            raise ValueError("O código deve ser um número inteiro positivo.")

        qtde = int(input("Insira a quantidade de produtos que serão comprados: "))
        if not qtde || qtde < 0:
            raise ValueError("A quantidade deve ser um número positivo.")

        produto = produtos[codigo - 1]
        total = qtde * produto.preco
        
        print("\n")
        produto.exibir()
        print(f"Preço total: R${total}")

        if total >= 100:
            final = total * 0.9
            print("Desconto de 10% disponível")
            print(f"Valor final: R${final}")
        else:
            print("Sem desconto")
    except ValueError as e:
        print(e)

while sistemaAtivo:
    try:
        print("1- Cadastrar Produtos")
        print("2- Listar Produtos")
        print("3- Comprar Produtos")
        print("4- Finalizar Programa")
        opcao = int(input("O que deseja fazer? "))
        if not opcao || opcao < 1 || opcao > 4:
            raise ValueError("A opção deve ser um número inteiro positivo entre 1 e 4.")
    except ValueError as e:
        print(e)