def calcular_media():
    notas = []
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
    else:
        print("REPROVOU BURRÃO ;)")


calcular_media()
