alunos = []
mostrado = False
def mostrarConceito(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
def mediaSala():
    notas = 0.0
    for aluno in alunos:
        notas += aluno["nota"]
    media = notas / len(alunos)
    return media
def mostrarAlunos():
    global mostrado # Para não criar outra variável dentro da função, usamos isso como um identificador
    if not mostrado:
        aprovados = 0
        recuperacao = 0
        reprovados = 0
        melhor = None
        pior = None
        for aluno in alunos:
            conceito = mostrarConceito(aluno["nota"])
            print("\nNome do aluno: ", aluno["nome"])
            print("Nota final: ", aluno["nota"])
            print("Conceito: ", conceito)
            if conceito == "Aprovado":
                aprovados += 1
            elif conceito == "Recuperação":
                recuperacao += 1
            elif conceito == "Reprovado":
                reprovados += 1
            if melhor == None or aluno["nota"] > melhor["nota"]:
                melhor = aluno
            if pior == None or aluno["nota"] < pior["nota"]:
                pior = aluno
        print("\nMédia final da turma: ", mediaSala())
        print("Quantidade de aprovados: ", aprovados)
        print("Quantidade de alunos de recuperação: ", recuperacao)
        print("Quantidade de reprovados: ", reprovados)
        print("\nAluno com a maior nota: ", melhor["nome"])
        print("Nota: ", melhor["nota"])
        print("\nAluno com a menor nota: ", pior["nome"])
        print("Nota: ", pior["nota"])
        mostrado = True
def cadastrarAluno():
    try:
        nome = input("Insira o nome do aluno: ")
        if nome == "":
            raise ValueError("O nome não pode estar vazio!")
        idade = int(input("Insira a idade do aluno: "))
        if idade < 0: 
            raise ValueError("A idade não pode ser negativa!")
        nota = float(input("Insira a nota do aluno: "))
        if nota < 0 or nota > 10:
            raise ValueError("Insira uma nota entre 0 e 10!")
        registro = {
            "nome": nome,
            "idade": idade,
            "nota": nota
        }
        alunos.append(registro)
    except ValueError as e:
        print(e)
        cadastrarAluno()
try:
    cadastrarAluno()
    while True:
        continuar = input("Deseja cadastrar outro aluno? (S/N) ")
        if(continuar.lower() == "s"):
            cadastrarAluno()
        else:
            mostrarAlunos()
            break
except KeyboardInterrupt:
    print("\nFinalizando o programa...")
    if len(alunos) > 0:
        mostrarAlunos()
except StopIteration:
    if len(alunos) > 0:
        mostrarAlunos()