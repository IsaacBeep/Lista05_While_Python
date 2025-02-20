#Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela, quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
soma = 0 
while True:
    numD = int(input('Digite um numero: '))
    soma += numD
    print('Soma: {}'.format(soma))

    if soma > 50:
        print("O total é:  {}".format(soma))
        break 
print('IsaacSouza')