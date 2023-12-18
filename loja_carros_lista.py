catalogo = list()
catalogo = [["Palio", "Fiat", 20.000, 2, 0], ["Fiesta", "Ford", 40.000, 3, 1], ["Gol", "Volkswagen", 60.000, 1, 2]]

menu = """
    [a] Adicionar dinheiro
    [c] Comprar carro
    [i] Inserir carro no catálogo
    [e] Encerrar
>= """

saldo = 0

while True:
    opcao = input(menu)

    if opcao in "Aa":
        adicionar = float(input("Informe quanto R$ adicionar na conta: "))
        saldo += adicionar      

    if opcao in "Cc":
        disponiveis = list()

        for i in catalogo:
            if saldo >= i[2] and i[3] > 0:      #verifica se saldo e unidades disponíveis são suficientes para uma possível compra
                disponiveis.append(i[:])        #adiciona carro a uma lista de disponíveis

        if len(disponiveis) == 0:
                print("Nenhum carro disponível para compra")

        elif len(disponiveis) > 0:
            for i in disponiveis:
                print(f"Código:{i[4]}, Modelo disponível: {i[0]}, marca: {i[1]}, preço: R${i[2]:.3f}, quantidade: {i[3]}")      #imprime carros pisponíveis
            
            valida_compra = input("\nDeseja comprar algum carro [s/n]: ")

            if valida_compra in "Ss":
                compra = 0
                codigo = (int(input("Informe o código do carro: ")))

                for i in disponiveis:
                    if codigo == i[4]:
                        print(f"Compra realizada com sucesso. Modelo: {i[0]}, Marca: {i[1]}, Preço: R${i[2]:.3f}")
                        saldo -= i[2]       #desconta valor da compra em saldo
                        compra = 1 
                        for p in catalogo:
                            if codigo == p[4]:
                                p[3] -= 1       #diminui 1 unidade no catalogo                               
                
                if compra == 0:
                    print("Código inserido inválido") 

                disponiveis.clear()
    
    if opcao in "Ii":
        carro = list()      #protótipo de carro: ("modelo", "marca", "preco, "quantidade", "codigo")
        carro.append(input("Informe o modelo: "))
        carro.append(input("Informe a marca: "))
        carro.append(float(input("Informe o preço: ")))
        carro.append(int(input("Informe a quantidade: ")))
        carro.append(int(input("Informe o código: "))) 
        catalogo.append(carro[:])
        carro.clear()
    
    if opcao in "Ee":
        print("Muito obrigado, programa encerrado!")   
        break