import tudo.Menu as Menu
import tudo.operacoes as operacoes
cont = 0
try:
    while True:
        if cont != 0:
            input('Aperte quanquer tecla para voltar ao Menu')
        Menu.cabecalho()
        resp = Menu.Menu(['Adicionar pessoas', 'Ver pessoas adicionadas', 'Sair'])
        if resp == 1:
            operacoes.adicionaPessoa()
        elif resp == 2:
            operacoes.verArquivo()
        elif resp == 3:
            operacoes.sair()
        cont += 1
except KeyboardInterrupt:
        print('\033[0;32;0mPrograma finalizado pelo usuario\033[0;0m')
        quit() 