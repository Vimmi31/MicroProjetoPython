import tudo.Menu as Menu
import tudo.operacoes as operacoes
import os
from sys import platform 

caminho = operacoes.ehCaminho('Aonde está o arquivo ou aonde você quer cria-lo?(Digite o caminho inteiro) ')
if platform == 'win32':
    os.system('cls')
      
cont = 0
try:
    while True:
        if cont != 0:
            input('Aperte qualquer tecla para voltar ao Menu')
        Menu.cabecalho()
        resp = Menu.Menu(['Adicionar pessoas', 'Ver pessoas adicionadas', 'Sair'])
        if resp == 1:
            operacoes.adicionaPessoa(caminho = caminho)
        elif resp == 2:
            operacoes.verArquivo(caminho = caminho)
        elif resp == 3:
            operacoes.sair()
        cont += 1
except KeyboardInterrupt:
        print('\033[0;32;0mPrograma finalizado pelo usuário\033[0;0m')
        quit() 
        