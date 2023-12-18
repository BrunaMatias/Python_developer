funcionarios = list()
aposentadoria = list()
bonus = list()

qtd_funcionarios = int(input("Quantidade de funcionários: "))

for i in range(qtd_funcionarios):
    pessoa = dict()             #protótipo pessoa= {nome, ano_nascimento, ctps, ano_contratacao, salario, idade, idade aposentadoria}
    print("\nInforme os dados do funcionário: ")            #cadastro de dados do funcionario
    pessoa["nome"] = str(input("Nome: "))
    pessoa["ano_nascimento"] = int(input("Ano de nascimento: "))
    pessoa["ctps"] = int(input("N° carteira de trabalho: "))
    pessoa["ano_contratacao"] = int(input("Ano da contratação: "))
    pessoa["salario"] = float(input("Sálario: "))
    pessoa["idade"] = 2023 - pessoa["ano_nascimento"] 
    pessoa["idade_aposentadoria"] = pessoa["ano_contratacao"] + 35 - pessoa["ano_nascimento"]

    if pessoa["ano_contratacao"] < 2020:          #condição para recebimento de bônus
        pessoa["salario"] = pessoa["salario"] + pessoa["salario"] * 0.10
        bonus.append(pessoa.copy())

    if pessoa["idade"] >= pessoa["idade_aposentadoria"]:            #condição para aposentadoria
        aposentadoria.append(pessoa.copy())

    funcionarios.append(pessoa.copy())          #adiciona funcionário a lista com todos funcionários

if len(aposentadoria) > 0:          #lista de funcionarios com aposentadoria disponível
    print("\nFuncionarios com aposentadoria disponível: ")
    for i in aposentadoria:
        print(f"Nome: {i['nome']}, Idade: {i['idade']}, N° carteira: {i['ctps']}")  
else:
    print("\nNenhum funcionário com aposentadoria disponível")

if len(bonus) > 0:          #lista de funcionarios com bônus disponível
    print("\nFuncionários com bônus no salário: ")
    for i in bonus:
        print(f"Nome: {i['nome']}, Novo salário: R${i['salario']}") 
else:
    print("\nNenhum funcionário com bônus disponível")