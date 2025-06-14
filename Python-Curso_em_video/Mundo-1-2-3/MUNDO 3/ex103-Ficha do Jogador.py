"""Faça um programa que tenha uma função chamada ficha(), que
receba dois parâmetros opcionais: o nome de um jogado e quantos gols ele
marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
que algum dado não tenha sido informado corretamente."""

def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


#Programa principal
nome = str(input(f'Nome do jogador: '))
pontos = input(f'Número de Gols: ')
if not pontos.isnumeric():
    pontos = 0
else:
    pontos = int(pontos)
if nome.strip() == '':
    ficha(gols=pontos)
else:
    ficha(nome, pontos)
