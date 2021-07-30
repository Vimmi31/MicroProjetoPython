def traco(n = 50):
    """[Imprime uma serie de traços na tela]

    Args:
        n (int, optional): [Numero de traços que serão exibidos]. Defaults to 50.
    """
    print('-'*n)


def NouS(txt = 'S ou N?'):
    """Função que roda até receber S ou N(Sim ou Não)

    Args:
        txt (str, optional): [Texto que vai imprimir na tela qunado chamada]. Defaults to 'S ou N?'.
    """
    while True:
        try:
            resp = str(input(txt)[0]).upper().strip()
            print(resp)
        except ValueError:
            print('Você não digitou uma String')
            continue
        if resp not in "SN":
            print('Digite apenas Sim ou Não')
            continue
        else:
            return(resp)   
        
             
def sair(seg = 0.2, tracos = 50):
    """[Função que fecha o programa, com mensagem de despedida]

    Args:
        seg (float, optional): [Tempo de "animação"]. Defaults to 0.2.
        tracos (int, optional): [Quantos traços mostrar?]. Defaults to 50.
    """
    from time import sleep
    print('Saindo', end='')
    for i in '...':
        print(i, end='', flush = True)
        sleep(seg)
    print('')
    traco(tracos)
    quit()
 

def ehCaminho(txt = 'Digite o caminho'):
    """[Identifica se o caminho digitado pelo usuario é valido, se repete até receber um caminho valido]

    Args:
        txt (str, optional): [Mensagem que irá aparecer na tela]. Defaults to 'Digite o caminho'.

    Returns:
        [String]: [Retorna o caminho em que o arquivo será criado]
    """
    from os.path import isdir
    while True:
        caminho = str(input('\033[1;36m' + txt + '\033[0;0m'))
        if isdir(caminho) == False:
            print('\033[1;91mO caminho que você digitou não é válido\033[0;0m')
            continue
        else:
            print(f'\033[1;92mOk! O arquivo será criado em: {caminho}\033[0;0m')
            break
    return caminho+'pessoas.txt' 


def adicionaPessoa(tracos = 50, caminho = ''):
    """[Função para adicionar informaçoes no documento de texto]

    Args:
        tracos (int, optional): [Quantos traços serão desenhados na tela?]. Defaults to 50.
        caminho (str, optional): [Caminho em que o arquivo se encontra]. Defaults to ''.
    """
    try:
        open(caminho, 'r+') # r+ significa que o arquivo pode ser visto e editado quando o arquivo já existe(não cria arquivos)(vem de read)
    except FileNotFoundError:
        open(caminho, 'w+') # w+ significa que o arquivo pode ser visto e editado quando o arquivo não existe(cria arquivos)(vem de write)    
    pessoas = open(caminho, 'a') # a vem de append, td o conteudo novo será adicinado no final do arquivo
    try:
        while True:
            pessoa = {'Nome': input('\033[1;36mNome da pessoa: '),
                    'Idade': input(f'Idade: \033[0;0m')}
            for i in pessoa.keys():
                if i == 'Nome':
                    pessoas.writelines('\n' + f'{i}: ' + pessoa[i] + '')
                else:
                    pessoas.writelines(f' {i}: ' + pessoa[i] + '\n' )
            traco(tracos)
            resp = NouS('\033[0;33;0mDeseja continuar? S/N\033[0;0m')
            if resp == 'N':
                break
    except KeyboardInterrupt:
        print('\033[0;32;0mPrograma finalizado pelo usuario\033[0;0m')
        pessoas.close()
        quit()    
    
    pessoas.close() #Arquivos abertos precisam ser fechados de forma correta no fim, por isso usamos o close 


def verArquivo(tracos = 50, caminho= ''):
    """[Mostra no console o arquivo criado com as informaçoes digitadas pelo usuario]

    Args:
        tracos (int, optional): [Quantos traços serão desenhados na tela?]. Defaults to 50.
        caminho (str, optional): [Caminho em que o arquivo se encontra ]. Defaults to ''.
    """
    try:
        arq = open(caminho, 'r+') # r+ significa que o arquivo pode ser visto e editado quando o arquivo já existe(não cria arquivos)(vem de read)
    except FileNotFoundError:
        print('O arquivo ainda não foi criado')
    else:
        print(arq.read())
    traco()
