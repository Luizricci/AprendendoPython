import cadastro
import calc_media

print("olá seja bem vindo ao meu programa que estou usando para aprender Python")
print("___________________________")

def comandos_home():
    print("Comandos Básicos: ")
    print("0- Sair do programa")
    print("1- Cadastro Simples")
    print("2- Calculadora de Média")

def start_home():
    while True:
        comandos_home()
        print("___________________________")
        comando_home = int(input("Digite Algum comando: "))
        print("___________________________")
        if comando_home == 1 :
            cadastro.start_cadastro()
        elif comando_home == 2:
            calc_media.start_media()
        elif comando_home == 0:
            print("programa Desativado")
            break
        else:
            print("Comando inválido :( ")
start_home()


