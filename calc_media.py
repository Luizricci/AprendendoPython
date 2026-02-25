
def comandos_media():
    print("Comandos Básicos da calculadora de média : ")
    print("1- Calcular a média ")
    print("9- Voltar para a home ")

def calcular_media():
    notas = []
    print("Lembrando que a média é 7")
    print("______________________")
    qntNotas = int(input("digite a qunatidade de notas: "))

    for x in range(qntNotas):
        nota = float(input("digite a nota: "))
        while True:
            if nota < 0 or nota >10 :
                print("a Nota do aluno não pode ser menor que 0 ou maior que 10 digite novamente")
                nota = float(input("digite a nota: "))
            else:
                notas.append(nota)
                break
    print("______________")


    soma = sum(notas)
    media= soma / qntNotas

    if media >= 7 :
        print("APROVADO SEU SAFADO")
        print("_________________")
    else:
        print("REPROVOU BURRÃO ;)")
        print("_________________")


def start_media():
    while True:
        comandos_media()
        print("______________________")
        comando = int(input("Digite algum comando: "))
        print("_____________________")
        if comando == 1:
            calcular_media()
        elif comando == 9:
            print("Voltando para a home!!!!")
            return
        else:
            print("Comando inválido :( ")
