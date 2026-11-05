from pilha import menu_pilha
from fila import menu_fila
from fila_circular import menu_fila_circular
from ordenar import menu_ordenar
from utils import ler_inteiro


def menu_principal():
    print("\n***********************************")
    print("| Estruturas de Dados e Ordenação |")
    print("-----------------------------------")
    print("| 1 - PILHA                       |")
    print("| 2 - FILA                        |")
    print("| 3 - FILA CIRCULAR               |")
    print("| 4 - ORDENAR                     |")
    print("| 5 - SAIR                        |")
    print("-----------------------------------")

    return ler_inteiro("Digite a opção desejada: ")


def main():
    while True:
        opt1 = menu_principal()

        if opt1 == 1:
            menu_pilha()

        elif opt1 == 2:
            menu_fila()

        elif opt1 == 3:
            menu_fila_circular()

        elif opt1 == 4:
            menu_ordenar()

        elif opt1 == 5:
            break

        else:
            print("Opção inexistente!")

    print("Programa finalizado!")


if __name__ == "__main__":
    main()
