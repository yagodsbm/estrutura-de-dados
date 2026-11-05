from utils import ler_inteiro, ler_inteiro_positivo, confirmar


def init():
    tamanho = ler_inteiro_positivo("Digite o tamanho da pilha: ")
    pilha = []
    return pilha, tamanho


def push(pilha, tamanho):
    if len(pilha) < tamanho:
        valor = input("Digite o valor: ")
        pilha.append(valor)
        print("Valor armazenado!")
    else:
        print("Pilha cheia!")


def pop(pilha):
    if len(pilha) > 0:
        valor = pilha.pop()
        print("Valor removido:", valor)
    else:
        print("Pilha vazia!")


def show(pilha):
    if len(pilha) > 0:
        print("Conteúdo da pilha:", pilha)
    else:
        print("Pilha vazia!")


def menu_pilha():
    estrutura = None
    tamanho = 0

    while True:
        print("\n--- MENU PILHA ---")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteúdo")
        print("5 - Voltar ao menu anterior")

        opcao = ler_inteiro("Digite a opção: ")

        if opcao == 1:
            if estrutura is None or confirmar("Já existe uma pilha. Deseja recriar? Os dados serão perdidos"):
                estrutura, tamanho = init()

        elif opcao == 2:
            if estrutura is not None:
                push(estrutura, tamanho)
            else:
                print("Crie a pilha primeiro!")

        elif opcao == 3:
            if estrutura is not None:
                pop(estrutura)
            else:
                print("Crie a pilha primeiro!")

        elif opcao == 4:
            if estrutura is not None:
                show(estrutura)
            else:
                print("Crie a pilha primeiro!")

        elif opcao == 5:
            break

        else:
            print("Opção inexistente!")
