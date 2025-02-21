#Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “s".
#Depois que o loop for interrompido, exiba o total
contador = 0

while True:
    num = int(input("Digite um numero: "))
    num2 = input('Deseja adicionar outro numero? s/n: ').lower()
    contador += num
    if num2 == 's':
        s = contador + num

    elif num2 == 'n':
        print(s)
        print('IsaacSouza')
        break