# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.



def calculadora(num1, num2, operacao):    
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    else:
        print("Operação inválida. Escolha uma operação válida entre 1 e 4.")
        return "0"
    
num1 = float(input("Informe o número 1: "))
num2 = float(input("Informe o número 2: "))
operacao = int(input("Escolha a operação entre 1:soma, 2:subtração, 3:multiplicação , 4:divisão: "))

resultado = calculadora(num1, num2, operacao)
print(resultado)
