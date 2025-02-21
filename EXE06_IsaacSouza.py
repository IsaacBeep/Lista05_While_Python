#Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".
while True:
    num = int(input('Digite um numero de 15 a 20: '))
    if num < 15:
        print('Numero muito baixo, tente novamente')
    elif num > 20:
        print('Numero muito alto, tente novamente')
    else:
        print('Obrigado')
        print('IsaacSouza')
        break
        