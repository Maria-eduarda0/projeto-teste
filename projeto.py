lista_jogo = []
while True:
    print("---- 1- Adicionar um jogo---------")
    print("---- 2- Listar itens cadastrados--")
    print("---- 3- Remover um item pelo nome-")
    print("---- 4- Sair do programa----------")
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            novo_jogo = input("Digite o nome do jogo: ")
            lista_jogo.append(novo_jogo)
            maisde1 = str(input("Deseja adicionar mais de um jogo? Resposta de Sim ou Não: ").lower())
            match maisde1:
                case "sim":
                    while True:
                        novo_jogo = input("Digite o nome do jogo: ")
                        lista_jogo.append(novo_jogo)
                        continuar = str(input("Quer adicionar outro jogo? Sim ou Não: ").lower())
                        if continuar == "não":
                            print(lista_jogo)
                            break
                case "não" :
                    print(lista_jogo)
            
        case 2:
            if len(lista_jogo) <= 0:
                print("A lista está vazia")
                input("Pressione enter para voltar ao menu")
            else:
                for indice, jogo in enumerate(lista_jogo, start= 1):
                    print(f"{indice}. {jogo}")
        case 3:
            item = input("Digite o nome do jogo para ser removido: ")
            if item in lista_jogo:
                lista_jogo.remove(item)
                print(lista_jogo)
            else:
                print("O item não está na lista")
        case 4:
            print("Saindo")
            break