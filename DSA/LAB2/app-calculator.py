# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!
# alterado no github


def inicio_calculator():
    print('''Selecione o número da operação desejada:\n\n1 - Soma;\n2 - Subtração;\n3 - Multiplicação;\n4 - Divisão.\n''')

    operador = input("Digite sua opção (1/2/3/4):")

    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número):"))

    return operador, num1, num2


def calculator(operador, num1, num2):
    if operador == '1':
        resultado = num1 + num2
        print(f'O resultado da soma é: {num1} + {num2} = {resultado}')

    elif operador == '2':
        resultado = num1 - num2
        print(f'O resultado da subtração é: {num1} - {num2} = {resultado}')

    elif operador == '3':
        resultado = num1 * num2
        print(f'O resultado da multiplicação é: {num1} * {num2} = {resultado}')

    elif operador == '4':
        resultado = num1 / num2
        print(f'O resultado da divisão é: {num1} / {num2} = {resultado}')

    else:
        resultado = print("Operação escolhida não é valida!")

    return resultado


print("\n******************* Calculadora em Python *******************")

operador, num1, num2 = inicio_calculator()

calculator(operador=operador,
           num1=num1,
           num2=num2)
