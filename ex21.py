try:
    a = float(input("Insira o primeiro número: "))
    b = float(input("Insira o segundo número: "))
    soma = a + b
    print(a, " + ", b, " = ", soma)
except ValueError: 
    print("Insira um valor válido em todos os campos!")