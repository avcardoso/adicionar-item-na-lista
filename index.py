from time import sleep
lista = []

while True:
    print('-'*30)
    print(f'{"---MENU---":^30}')
    print('''
    1 - adicionar item a lista;
    2 - ver lista;
    3 - remover item da lista;
    4 - parar programa;
    ''')
    print('-'*30)

    resp = int(input('qual item deseja?: '))
    if resp == 4:
        print(f'sua lista: {lista}')
        print('programa finalizado.')
        break

    if resp == 1:
        lista.append(str(input('o que voce quer adicionar?: ')))
        print('loading...')
        sleep(1)
        print('item adicionado.')
        sleep(1)
    elif resp == 2:
        print(f'A lista contem: {lista}')
    
    elif resp == 3:
        print(lista)
        remover = str(input('qual o item que quer remover: '))
        lista.remove(f"{remover}")
    





