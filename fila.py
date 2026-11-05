from collections import deque

from utils import ler_inteiro, ler_inteiro_positivo, confirmar


def init():
    tamanho = ler_inteiro_positivo("Digite o tamanho da fila: ")
    fila = deque()
    return fila, tamanho


def enqueue(fila, tamanho):
    if len(fila) < tamanho:
        valor = input("Digite o valor: ")
        fila.append(valor)
        print("Valor armazenado!")
    else:
        print("Fila cheia!")


def dequeue(fila):
    if len(fila) > 0:
        valor = fila.popleft()  # O(1), ao contrário de list.pop(0), que é O(n)
        print("Valor removido:", valor)
    else:
        print("Fila vazia!")


def show(fila):
    if len(fila) > 0:
        print("Conteúdo da fila:", list(fila))
    else:
        print("Fila vazia!")


def menu_fila():
    estrutura = None
    tamanho = 0

    while True:
        print("\n--- MENU FILA ---")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteúdo")
        print("5 - Voltar ao menu anterior")

        opcao = ler_inteiro("Digite a opção: ")

        if opcao == 1:
            if estrutura is None or confirmar("Já existe uma fila. Deseja recriar? Os dados serão perdidos"):
                estrutura, tamanho = init()

        elif opcao == 2:
            if estrutura is not None:
                enqueue(estrutura, tamanho)
            else:
                print("Crie a fila primeiro!")

        elif opcao == 3:
            if estrutura is not None:
                dequeue(estrutura)
            else:
                print("Crie a fila primeiro!")

        elif opcao == 4:
            if estrutura is not None:
                show(estrutura)
            else:
                print("Crie a fila primeiro!")

        elif opcao == 5:
            break

        else:
            print("Opção inexistente!")
