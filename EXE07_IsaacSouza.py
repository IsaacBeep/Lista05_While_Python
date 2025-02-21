#Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.

lista = []
contador = 0
while True:
    num = int(input('Digite um numero inteiro ("0" para terminar a execução): '))
    
    if num != 0: #Adicionar
        lista.append(num)

        if num in lista: #Procurar na lista
            print(lista)
            VerificarI = input('Seu produto esta repetido na lista? s/n: ')
            
            if VerificarI == 's':
                i = lista.index(num)
                lista.remove(num)
                print(lista)
            elif VerificarI == 'n':
                print('Continue')

    elif num == 0: #Finalizar
        print(lista)
        break


