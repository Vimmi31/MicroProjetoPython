def traco(n = 50):
    print('-'*n)


def cabecalho(txt = 'Menu', tracos = 50):
    """[Imprime uma especie de cabeçalho]

    Args:
        txt (str, optional): [Texto que vai ser mostrado no cetro da tela]. Defaults to 'Menu'.
        tracos (int, optional): [Quantos traços serão desenhados na tela?]. Defaults to 50.
    """
    traco(tracos)
    print(f'\033[1;36m{txt}\033[0;0m'.center(tracos+14))
    traco(tracos)


def leiaInt(msg = ''):
    """ 
    Função que valida se o valor digitado é inteiro, se não for mostra uma mensagem de erro
    msg: Variavel opcional que vai printar o texto recebido como parametro
    return: O numero validado, como int
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError): 
            print('\033[1;91mValor digitado não é um numero Inteiro\033[0;0m')
            continue
        except KeyboardInterrupt:
            print('Programa interrompido pelo usuario')
            break
        except:
            print('Erro desconhecido')
        else:
            return n
            break


def Menu(lista, tracos = 50):
    """Imprime um menu de opçoes 

    Args:
        lista ([list]): [Recebe a lista de opçoes que será impressa]
        tracos (int, optional): [Quantos traços serão desenhados na tela?]. Defaults to 50.
    """
    cont = 0
    for i in lista:
        cont += 1
        print(f'\033[1;95m{cont} - {lista[cont-1]}\033[0;0m'.ljust(tracos+14))
    traco(tracos)
    try:
        while True:
            resp = leiaInt('\033[1;95mQual opção?\033[0;0m')
            traco(tracos)
            if resp > len(lista) or resp < 1:
                print('\033[1;91mDigite uma opção valida\033[0;0m')
                continue
            else:
                return resp
                break
    except KeyboardInterrupt:
        print('\033[0;32;0mPrograma finalizado pelo usuario\033[0;0m')
        quit()       