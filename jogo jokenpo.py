def menu():
    print('''digite sua jogada :

    [ 0 ] pedra
    [ 1 ] papel 
    [ 2 ] tesoura 
    ''')

from random import randint

print('''Bem vindo ao jogo jokenpo , digite sua opção de jogo :

    [ 0 ] computador  x computador 1
    [ 1 ] jogador x jogador 1
    [ 2 ] computador x jogado
    [ 3 ] sair do jogo  ''')
A=int(input('digite sua opção  '))

if A==0:
    computador = randint(0,2)
    computador1 = randint(0,2)
    
    if computador ==0 :
        if computador1==0 :
            print('empatou')
        elif computador1==1 :
            print('computador 1 , venceu')
        else : 
            print('computador 1 , perdeu')
    
    elif computador ==1 :
        if computador1==0 :
            print('computador 1 , perdeu')
        elif computador1==1 :
            print('empate')
        else : 
            print('computador 1 , ganhou')
    elif computador ==2:
        if computador1==0 :
            print('computador 1 , ganhou')
        elif computador1==1 :
            print('computador 1 , perdeu')
        else : 
            print('empate')


elif A==1:
    menu()
    jogador=int(input('jogador , digite sua jogada  '))
    jogador1 =int(input('jogador 1 , digite sua jogada  '))

    
    if jogador==0 :
        if jogador1==0 :
            print('empatou')
        elif jogador1==1 :
            print('jogador 1 , venceu')
        else : 
            print('jogador 1 , perdeu')
    
    elif jogador==1 :
        if jogador1==0 :
            print('jogador 1 , perdeu')
        elif jogador1==1 :
            print('empate')
        else : 
            print('jogador 1 , ganhou')
    elif jogador ==2:
        if jogador1==0 :
            print('jogador 1 , ganhou')
        elif jogador1==1 :
            print('jogador 1 , perdeu')
        else : 
            print('empate')


elif A==2:
    menu()
    computador = randint(0,2)
    jogador =int(input('digite sua jogada  '))
    
    if computador ==0 :
        if jogador==0 :
            print('empatou')
        elif jogador==1 :
            print('computador , venceu')
        else : 
            print('computador , perdeu')
    
    elif computador ==1 :
        if jogador==0 :
            print('computador , perdeu')
        elif jogador==1 :
            print('empate')
        else : 
            print('computador , ganhou')
    elif computador ==2:
        if jogador==0 :
            print('computador , ganhou')
        elif jogador==1 :
            print('computador , perdeu')
        else : 
            print('empate')

elif A==3:
    print('jogo encerrado')   
else :
    print('você escolheu uma opção inválida , o jogo será encerrado')
    