from utils import ler_inteiro, ler_inteiro_positivo


def bubble_sort(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def selection_sort(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        menor = i

        for j in range(i + 1, tamanho):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


def insertion_sort(lista):
    tamanho = len(lista)

    for i in range(1, tamanho):
        valor = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valor

    return lista


def menu_ordenar():
    while True:
        print("\n--- MENU ORDENAR ---")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        print("4 - Voltar ao menu anterior")

        opcao = ler_inteiro("Digite a opção: ")

        if opcao == 4:
            break

        elif opcao in [1, 2, 3]:
            quantidade = ler_inteiro_positivo("Quantos números deseja ordenar? ")

            lista = []

            for i in range(quantidade):
                valor = ler_inteiro(f"Digite o {i + 1}º número: ")
                lista.append(valor)

            print("\nLista original:", lista)

            if opcao == 1:
                bubble_sort(lista)
                print("Algoritmo utilizado: Bubble Sort")

            elif opcao == 2:
                selection_sort(lista)
                print("Algoritmo utilizado: Selection Sort")

            elif opcao == 3:
                insertion_sort(lista)
                print("Algoritmo utilizado: Insertion Sort")

            print("Lista ordenada:", lista)

        else:
            print("Opção inexistente!")
