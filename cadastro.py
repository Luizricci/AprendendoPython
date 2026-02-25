
nomes = []

def comandos():
    print("comandos básicos do Cadastro: ")
    print("1 - Digitar um nome")
    print("2 - Listar todos os nomes")
    print("3 - Remover um nome")
    print("9 - Voltar Para Home")
    print("0 - Sair")
    print("_________________________")

#aqui eu estou pegando os nomes e adicionaodo no array
def adicionar_nomes():
    while True:
        nome = input("Digite um nome ou (9 para voltar): ")
            
        if nome == "9":
            print("Função cancelada")
            print("_________________________")
            break
        nomes.append(nome)


#aqui eu exibo todos os nomes do array
def mostrar_nomes():
    print(nomes)
    print("_________________________")

#aqui eu estou removendo um nome do array
def remover_nome():
    print("Atenção !!!!!")
    print("Para excluir um nome terá que digita-lo da mesma forma que cadastrado ")
    nome = str(input("Digite o nome a ser excluido: "))
    while True:
        if nome in nomes:
            indice = nomes.index(nome)
            print("Nome Achado!!")
            print("Deseja proseguir com a exclusão?")
            print("________________________________")
            confirmacao = int(input("1- Sim ou 2- Não: "))
            if confirmacao == 1:
                print("Nome excluido com sucesso!!!")
                print("________________________________")
                nomes.pop(indice)
                break
            else:
                print("Exclusão cancelada")
                print("________________________________")
                break
        else:
            print("Nome não encontrado")
            break



#aqui eu estou fazendo a seleção de comandos e verificações
def start_cadastro():
    while True:
        comandos()
        comando = int(input("digite algum comando: "))
        print("________________________________")
        
        if comando == 1:
            adicionar_nomes()
        elif comando == 2:
            mostrar_nomes()
        elif comando == 3:
            remover_nome()
        elif comando == 0:
            print("Encerrando programa")
            break
        elif comando == 9:
            print("voltando para a home")
            return
        else:
            print("Comando Inválido")







