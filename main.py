numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
operacao = int(input('''1-Adição
2-Subtração
3-Multiplicação
4-Divisão
Escolha qual a operação que você deseja: '''))

if operacao == 1:
    print(numero1 + numero2)
elif operacao == 2:
    print(numero1 - numero2)
elif operacao == 3:
    print(numero1 * numero2)
elif operacao == 4:
    print(numero1 / numero2)
