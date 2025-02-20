#Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela, quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
numD = int(input('Digite um numero: '))
while numD <= 59:
    soma = numD + numD
    print('Soma: {}'.format(soma))