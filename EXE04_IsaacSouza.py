#Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem
#Em seguida, pergunte se ele quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa

contador = 1

while True:  
    P_convidadas = input("Digite o nome da pessoa: ")
    i = print('{} Esta convidada para a festa'.format(P_convidadas))
    M_convide = input('Quer convidar mais pessoas? s/n: ').lower()
    if M_convide == 's':
        contador += 1 
    elif M_convide == 'n':
        print('O total de {} pessoas foram convidadas para a festa'.format(contador))
        print('IsaacSouza')
        break