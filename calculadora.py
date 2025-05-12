print("Olá, usuário!")
print("Bem-vindo à Calculadora")
print("Solicitando ao usuário que insira os dados...")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print("Escolha o operador matemático:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operador = int(input("Digite o número do operador: "))

if operador == 1:
    print("O resultado da soma é:", soma)
elif operador == 2:
    print("O resultado da subtração é:", subtracao)
elif operador == 3:
    print("O resultado da multiplicação é:", multiplicacao)
elif operador == 4:
    print("O resultado da divisão é:", divisao)
else:
    print("Operador inválido")

