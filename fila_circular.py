from utils import ler_inteiro, ler_inteiro_positivo, confirmar


def init():
    tamanho = ler_inteiro_positivo("Digite o tamanho da fila circular: ")

    fila = {
        "dados": [None] * tamanho,
        "inicio": 0,
        "fim": 0,
        "quantidade": 0,
        "tamanho": tamanho
    }

    return fila


def enqueue(fila):
    if fila["quantidade"] < fila["tamanho"]:
        valor = input("Digite o valor: ")
        fila["dados"][fila["fim"]] = valor
        fila["fim"] = (fila["fim"] + 1) % fila["tamanho"]
        fila["quantidade"] += 1
        print("Valor armazenado!")
    else:
        print("Fila circular cheia!")


def dequeue(fila):
    if fila["quantidade"] > 0:
        valor = fila["dados"][fila["inicio"]]
        fila["dados"][fila["inicio"]] = None
        fila["inicio"] = (fila["inicio"] + 1) % fila["tamanho"]
        fila["quantidade"] -= 1
        print("Valor removido:", valor)
    else:
        print("Fila circular vazia!")


def show(fila):
    if fila["quantidade"] > 0:
        print("Conteúdo da fila circular:")
        for i in range(fila["quantidade"]):
            posicao = (fila["inicio"] + i) % fila["tamanho"]
            print(fila["dados"][posicao], end=" ")
        print()
    else:
        print("Fila circular vazia!")


def menu_fila_circular():
    estrutura = None

    while True:
        print("\n--- MENU FILA CIRCULAR ---")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteúdo")
        print("5 - Voltar ao menu anterior")

        opcao = ler_inteiro("Digite a opção: ")

        if opcao == 1:
            if estrutura is None or confirmar("Já existe uma fila circular. Deseja recriar? Os dados serão perdidos"):
                estrutura = init()

        elif opcao == 2:
            if estrutura is not None:
                enqueue(estrutura)
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
