# crie um programa que faça o computador jogar pedra, papel e tesoura. 
# O usuário escolhe o que quer e o computador tbm e mostrar na tela quem ganhou.

from random import randint
from time import sleep # contador de tempo
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)

print('''Vamos jogar JOKENPÔ ou conhecido também como Pedra, Papel e Tesoura?
Escolha uma opção e bom jogo.
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
user= int(input('Qual a sua opção? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 11)

print('O computador jogou {}' .format(itens[pc]))
print('O jogador jogou {}' .format(itens[user]))

print('-=' * 11)

if pc == 0: # pc jogou pedra
    if user == 0:
        print('EMPATE')
    elif user == 1:
        print('VOCÊ VENCEU')
    elif user == 2:
        print('COMPUTADOR VENCEU')

elif pc == 1: # pc jogou papel
    if user == 0:
        print('COMPUTADOR VENCEU')
    elif user == 1:
        print('EMPATE')
    elif user == 2:
        print('VOCÊ VENCEU')

elif pc == 2: # pc jogou tesoura
    if user == 0:
        print('VOCÊ VENCEU  ')
    elif user == 1:
        print('COMPUTADOR VENCEU')
    elif user == 2:
        print('EMPATE')




'''if user == 'tesoura' and pc == 'papel'or user == 'papel' and pc == 'pedra' or user == 'pedra' and pc == 'tesoura':
    print('PARABÉNS! VOCê GANHOU. O computador jogou {} e você jogou {}.' .format(pc, user))

elif user == 'papel' and pc == 'tesoura'or user == 'pedra' and pc == 'papel' or user == 'tesoura' and pc == 'pedra':
    print('AHHH, VOCÊ PERDEU. O computador jogou {} e você jogou {}.' .format(pc, user))

elif user == pc:
    print('Ninguém ganhou. O computador jogou {} e você jogou {}.' .format(pc, user))'''



