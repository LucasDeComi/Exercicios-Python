try:
    valor = float(input("Insira um valor: "))
except ValueError:
    print("Insira um valor númerico!")
except EOFError:
    print("O campo não pode estar vazio!")
except KeyboardInterrupt:
    print("Programa interrompido!") 