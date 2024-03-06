'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''


def fibonacci_sequence(num):
    f_sequence = [0, 1]
    while f_sequence[-1] < num:
        f_sequence.append(f_sequence[-1] + f_sequence[-2])
    return f_sequence

def verifica_numero(numero):
    f_sequence = fibonacci_sequence(numero)
    if numero in f_sequence:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero_teste = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(verifica_numero(numero_teste))
