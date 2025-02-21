#Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".
adivinha = 50
contador = 1
while True:
    Ad = int(input('Digite um numero: '))
    if Ad <= 49:
        contador += 1
        print('Numero muito baixo')
    elif Ad >= 51:
        contador += 1
        print('Numero muito alto')
    else:
        print('Parabens você acertou em {} tentativas'.format(contador))
        print('IsaacSouza')
        break
        