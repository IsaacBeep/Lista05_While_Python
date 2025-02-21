#Peça ao usuário para inserir um número. Continue perguntando até que ele insira CINCO números, em seguida, exibam a mensagem “ O último número que você digitou foi um [número] " e pare o programa.
contador = 0

while True:
    num = int(input('Escreva um numero; '))
    contador += 1
    if contador == 5:
        print('O ultimo numero que você digitou foi:{}'.format(num))
        break
print('IsaacSouza')