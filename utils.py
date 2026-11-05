def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido!")


def ler_inteiro_positivo(mensagem):
    while True:
        numero = ler_inteiro(mensagem)
        if numero > 0:
            return numero
        print("O número deve ser maior que zero!")


def confirmar(mensagem):
    while True:
        resposta = input(mensagem + " (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Digite apenas 's' ou 'n'!")
