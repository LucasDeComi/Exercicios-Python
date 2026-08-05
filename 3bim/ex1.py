# Crie uma classe chamada produto, com os atributos código, nome, quantidade e preço unitário.
# Crie um objeto para a classe produto e mostre seus dados, e crie um método que mostre as informações do produto.

class Produto:
    def __init__(self, codigo, nome, qtde, preco):
        self.codigo = codigo
        self.nome = nome
        self.qtde = qtde
        self.preco = preco
    
    def mostrar(self):
        total = self.qtde * self.preco
        print(f"Produto: {self.nome}")
        print(f"Código do produto: {self.codigo}")
        print(f"Quantidade: {self.qtde}")
        print(f"Preço unitário: {self.preco}")
        print(f"Preço total: {total}");
        
produto = Produto(123, "Vassoura", 2, 19.9)
produto.mostrar()