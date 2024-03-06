'''
 Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no
código;

b) Evite usar funções prontas, como, por exemplo, reverse;

'''

def inverterString(texto):
    string_invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
    return string_invertida

string_original = input("Digite uma string: ")
string_invertida = inverterString(string_original)
print("String invertida:", string_invertida)
