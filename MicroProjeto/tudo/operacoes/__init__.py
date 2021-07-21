def traco(n = 50):
    print('-'*n)


def NouS(txt = 'S ou N?'):
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
    from time import sleep
    print('Saindo', end='')
    for i in '...':
        print(i, end='', flush = True)
        sleep(seg)
    print('')
    traco(tracos)
    quit()
 
   
def adicionaPessoa(tracos = 50):
    try:
        open('/media/vinicius/1D12E899389E14CB/MicroProjeto/Pessoas', 'r+') # r+ significa que o arquivo pode ser visto e editado quando o arquivo já existe(não cria arquivos)(vem de read)
    except FileNotFoundError:
        open('/media/vinicius/1D12E899389E14CB/MicroProjeto/Pessoas', 'w+') # w+ significa que o arquivo pode ser visto e editado quando o arquivo não existe(xria arquivos)(vem de write)
    pessoas = open('/media/vinicius/1D12E899389E14CB/MicroProjeto/Pessoas', 'a') # a vem de append, td o conteudo novo será adicinado no final do arquivo
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


def verArquivo(tracos = 50):
    try:
        arq = open('/media/vinicius/1D12E899389E14CB/MicroProjeto/Pessoas', 'r+') # r+ significa que o arquivo pode ser visto e editado quando o arquivo já existe(não cria arquivos)(vem de read)
    except FileNotFoundError:
        print('O arquivo ainda não foi criado')
    else:
        print(arq.read())
    traco()
