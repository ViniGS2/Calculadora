def fatorial(numero):
    if numero == 1:
        return numero
    return numero * fatorial(numero - 1)


print("Seja Bem-Vindo a Calculadora!\n")

print("Escolha a operação: ")

operacao = int(input('''1-Adição
2-Subtração
3-Multiplicação
4-Divisão
5-Fatorial

Escolha qual a operação que você deseja: '''))

if operacao != 5:
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    if operacao == 1:
        print(numero1 + numero2)
    elif operacao == 2:
        print(numero1 - numero2)
    elif operacao == 3:
        print(numero1 * numero2)
    elif operacao == 4:
        print(numero1 / numero2)
elif operacao == 5:
    numero = int(input("Digite o numero: "))
    print(fatorial(numero))
