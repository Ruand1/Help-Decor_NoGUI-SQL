# ----- Importanto Bibliotecas
from time import sleep
from termcolor import colored
import pyodbc

AI = 'Ambrósio'


def linhasepara(nomeprograma):
    tam = len(nomeprograma.center(100)) + 4
    print()
    sleep(0.5)
    print('*' * tam)
    sleep(0.5)


def carregamento(nomeprograma):
    tam = len(nomeprograma.center(100)) + 4
    print(colored('~', 'magenta') * tam)
    sleep(0.5)
    print(colored(f'{nomeprograma.center(tam)}'))
    sleep(0.5)
    print(colored('~', 'magenta') * tam)

    linhasepara(nomeprograma)


def inteligencia1(nomeprograma):
    frase1 = f'Olá meu nome é {AI}... irei ajuda-la na montagem da decoração...'
    frase2 = 'Vamos lá...Me diga o que você quer fazer...'
    for letra in frase1:
        print(colored(f'{letra}', 'blue'), end='')
        sleep(0.2)
    print('\n')
    for letra in frase2:
        print(colored(f'{letra}', 'blue'), end='')
        sleep(0.2)

    linhasepara(nomeprograma)


def menu(lista):
    cont = 1
    for item in lista:
        print(f'{cont}.{item:_>102}')
        cont += 1


def validaint(qtd, texto):
    num = 0
    while True:
        try:
            num = int(input(texto))
        except (TypeError, ValueError):
            sleep(0.5)
            print(colored('Erro! Digite um número inteiro válido...', 'red'))
        except KeyboardInterrupt:
            sleep(0.5)
            print(colored('\nErro! O usuário finalizou o aplicativo...', 'red'))
            break
        else:
            if num > qtd:  #<----or num == 0: VERIFICAR
                sleep(0.5)
                print(colored('O número digitado não esta em uma das opções...', 'red'))
                continue
            else:
                return num


def inteligencia2(num, lista, nomeprograma):
    lista = ['Cadastro de Clientes', 'Cadastro Festas', 'Cadastro Peças de Decoração', 'Sair']

    frase1 = f'Certo...opção {num}...{lista[num-1]}...Vamos lá....'
    for letra in frase1:
        print(colored(f'{letra}', 'magenta'), end='')
        sleep(0.2)
    print('\n')

    linhasepara(nomeprograma)

# ---------Funções de Menus ----- Verificar unificação em uma unica função - utilizando argumentos


def cadastrocliente():
    menu(['Cadastrar Cliente', 'Ver Clientes', 'Pesquisar Cliente', 'Editar Cliente', 'Exluir Cliente', 'Voltar'])
    opcadastro = validaint(6, 'Escolha uma opção: ')
    return opcadastro


def cadastrofestas():
    menu(['Cadastrar Festas', 'Ver Festas', 'Pesquisa Festas', 'Editar Festas', 'Excluir Festas', 'Voltar'])
    opcadastro2 = validaint(6, 'Escolha uma opção: ')
    return opcadastro2


def cadastropecas():
    menu(['Cadastrar Peças', 'Ver Lista de Peças Geral', 'Pesquisa Peças', 'Editar Peças', 'Excluir Peças', 'Voltar'])
    opcadastro3 = validaint(6, 'Escolha uma opção: ')
    return opcadastro3


def cadastrofornecedor():
    menu(['Cadastrar Fornecedor', 'Ver Lista de Fornecedores', 'Pesquisa Fornecedor', 'Editar Fornecedor', 'Excluir Fornecedor', 'Voltar'])
    opcadastro4 = validaint(6, 'Escolha uma opção: ')
    return opcadastro4
# -------------------------------------------------------------------------------------------------


def arquivoExiste(nome): #<------V1.0.0 - Verifica se o arquivo txt foi criado
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(colored('Houve um erro na criação do arquivo...', 'red'))
    else:
        print(colored(f'Arquivo {nome}, ok...', 'magenta'))

# --------Funções de Cadastros --- APENAS GRAVAÇÃO TXT
def cadastrar(nome, nomecliente='<desconhecido>', telefone='<0>', endereco='<Rua: 0'):
    try:
        a = open(nome, 'at') #Função para incluir novo cadastro
    except:
        print(colored('Erro ao abrir o arquivo...', 'red'))
    else:
        try:
            a.write(f'{nomecliente};{telefone};{endereco}\n')
        except:
            print(colored('Houve um erro na hora de escrever os dados...', 'red'))
        else:
            print(colored(f'OK....{nomecliente} cadastrada(o)...', 'magenta'))
            linhasepara('Help Decor')
            a.close()


def cadastrarfesta(nome, nomecliente='<desconhecido>', tema='<nenhum>', data='<00/00/00>'):
    try:
        a = open(nome, 'at')
    except:
        print(colored('Erro ao abrir arquivo...', 'red'))
    else:
        try:
            a.write(f'{nomecliente};{tema};{data}\n')
        except:
            print(colored('Houve um erro na hora de escrever os dados...', 'red'))
        else:
            print(colored(f'Muito bem...cadastramos a(o) cliente {nomecliente} com o tema {tema}', 'magenta'))
            linhasepara('Help Decor')
            a.close()


def cadastrarpeca(nome, tipo='<desconhecido>', cor='<desconhecido>', tamanho='<desconhecido>',
                  composicao='<desconhecido>', quantidade='0', ID='0'):
    try:
        a = open(nome, 'at')
    except:
        print(colored('Erro ao abrir arquivo...', 'red'))
    else:
        try:
            a.write(f'{tipo};{cor};{tamanho};{composicao};{quantidade};{ID}\n')
        except:
            print(colored('Houve um erro na hora de escrever os dados', 'red'))
        else:
            print(colored(f'OK...{tipo} {tamanho} da cor {cor} cadastrada(o)...', 'magenta'))
            linhasepara('Help Decor')
            a.close()
# ------------------------------------------------------

def vercliente(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler o arquivo...', 'red'))
    else:
        print('       Nome               Telefone               Endereço')
        cont = 1
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{cont}.{dado[0]:<20}{dado[1]:^18}{dado[2]:>20}')
            cont += 1
        linhasepara('Help Decor')
        a.close()
    #finally:
        #a.close()


def verfestas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler o arquivo...', 'red'))
    else:
        print('       Nome                  Tema                  Data')
        cont = 1
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            print(f'{cont}.{dado[0]:<20}{dado[1]:^18}{dado[2]:>20}')
            cont += 1
        linhasepara('Help Decor')
        a.close()
    #finally:
        #a.close()


def verpecas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler arquivo...', 'red'))
    else:
        print(' Tipo         Cor     Tamanho     Composição     Quantidade      ID')
        cont = 1
        for linha in a:
            dado = linha.split(';')
            dado[5] = dado[5].replace('\n', '')
            print(f'{cont}.{dado[0]:<10}{dado[1]:^8}{dado[2]:^12}{dado[3]:^14}{dado[4]:^18}{dado[5]:>3}')
            cont += 1
        linhasepara('Help Decor')
        a.close()


def pesquisapecas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler arquivo...', 'red'))
    else:
        while True:
            pesquisa = str(input('Digite uma palavra chave para pesquisa ou 0 para voltar: ')).capitalize()
            contpeca = 0
            if pesquisa == '0':
                break
            else:
                print(' Tipo         Cor     Tamanho     Composição     Quantidade      ID')
                cont = 1
                for linha in a:
                    dado = linha.split(';')  #<--- variável dado recebe a linha e separa em uma lista
                    dado[5] = dado[5].replace('\n', '')  #<---Dados foram gravados no banco com \n no final
                    cont += 1
                    if dado[0] == pesquisa or dado[1] == pesquisa or dado[2] == pesquisa or dado[3] == pesquisa or dado[4] == pesquisa or dado[5] == pesquisa:
                        print(f'{cont}.{dado[0]:<10}{dado[1]:^8}{dado[2]:^12}{dado[3]:^14}{dado[4]:^18}{dado[5]:>3}')
                        contpeca += 1
                print(colored(f'Encontrei {contpeca} peças com essa característica....', 'magenta'))
                linhasepara('Help Decor')
                break

        a.close()


def pesquisafestas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler arquivo...', 'red'))
    else:
        while True:
            pesquisa = str(input('Digite uma palavra chave para pesquisa ou 0 para voltar: ')).capitalize()
            contpeca = 0
            if pesquisa == '0':
                break
            else:
                print('        Nome                  Tema                  Data')
                cont = 1
                for linha in a:
                    dado = linha.split(';')  # <--- variável dado recebe a linha e separa em uma lista
                    dado[2] = dado[2].replace('\n', '')  # <---Dados foram gravados no banco com \n no final
                    cont += 1
                    if dado[0] == pesquisa or dado[1] == pesquisa or dado[2] == pesquisa:
                        print(f'{cont}.{dado[0]:<20}{dado[1]:^18}{dado[2]:>20}')
                        contpeca += 1
                print(colored(f'Encontrei {contpeca} festas com essa característica....', 'magenta'))
                linhasepara('Help Decor')
                break

        a.close()


def pesquisacliente(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler arquivo...', 'red'))
    else:
        while True:
            pesquisa = str(input('Digite uma palavra chave para pesquisa ou 0 para voltar: ')).capitalize()
            contpeca = 0
            if pesquisa == '0':
                break
            else:
                print('        Nome                  Telefone                     Endereço')
                cont = 1
                for linha in a:
                    dado = linha.split(';')  #<--- variável dado recebe a linha e separa em uma lista
                    dado[2] = dado[2].replace('\n', '')  #<---Dados foram gravados no banco com \n no final
                    cont += 1
                    if dado[0] == pesquisa or dado[1] == pesquisa or dado[2] == pesquisa:
                        print(f'{cont}.{dado[0]:<20}{dado[1]:^18}{dado[2]:>20}')
                        contpeca += 1
                print(colored(f'Encontrei {contpeca} cliente(s) com essa característica....', 'magenta'))
                linhasepara('Help Decor')
                break

        a.close()


def editarpecas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler arquivo...', 'red'))
    else:
        lista = []
        listaapoio = []
        listagravacao = []
        strapoio = ''
        cont = 1
        listaescolha = []
        escolha1 = 0
        escolha2 = 0
        print(' Tipo         Cor     Tamanho     Composição     Quantidade      ID')
        for linha in a:
            dado = linha.split(';') # <--- variável dado recebe a linha e separa em uma lista
            dado[5] = dado[5].replace('\n', '')  # <---Dados foram gravados no banco com \n no final
            print(f'{cont}.{dado[0]:<10}{dado[1]:^8}{dado[2]:^12}{dado[3]:^14}{dado[4]:^18}{dado[5]:>3}')
            cont += 1
            lista.append(linha.replace('\n', ''))  # <--- Transforma os dados txt em uma lista
        linhasepara('Help Decor')
        cont = 0

        #print(lista) #<--- Lista recebe todos os item do arq txt cadastrados ________ APENAS TESTES

        # < ------- Usuario ira escolher qual item da lista vai modificar
        escolha = validaint(len(lista), 'Escolha uma opção: ')

        listaapoio = lista[escolha-1].replace(';', ' ').split()  #<--transforma arq txt em lista na posição escolhida, PROBLEMA RESOLVIDO, TIRA PULA LINHA PARA GRAVAÇÂO POSTERIOR

# ------------- TESTES
        #print(lista)  #<-------- lista recebendo todas as informações do arq txt
        #print(escolha)  #<------ escolha do usuário
        #print(listaapoio)  #<--- Lista com os dados do txt separados
# --------------------

        # - Usuario escolhe qual atributo deseja editar
        escolha1 = validaint(6, 'Qual caracteristica deseja trocar: '
                                '[1]Tipo '
                                '[2]Cor '
                                '[3]Tamanho '
                                '[4]Composição '
                                '[5]Quantidade '
                                '[6]ID')
        listaescolha.append(escolha1)
        escolha2 = str(input(f'Digite o que deseja trocar em {escolha1}: ')).strip().capitalize()
        listaescolha.append(escolha2)
        if listaescolha[0] == 1:
            listaapoio[0] = listaescolha[1]
            strapoio = str(listaapoio).strip('[]').strip('').replace("'", '').replace(',', ';').replace(' ', '').replace('\n', '')
            lista[escolha-1] = strapoio
        elif listaescolha[0] == 2:
            listaapoio[1] = listaescolha[1]
            strapoio = str(listaapoio).strip('[]').strip('').replace("'", '').replace(',', ';').replace(' ', '').replace('\n', '')
            lista[escolha - 1] = strapoio
        elif listaescolha[0] == 3:
            listaapoio[2] = listaescolha[1]
            strapoio = str(listaapoio).strip('[]').strip('').replace("'", '').replace(',', ';').replace(' ', '').replace('\n', '')
            lista[escolha - 1] = strapoio
        elif listaescolha[0] == 4:
            listaapoio[3] = listaescolha[1]
            strapoio = str(listaapoio).strip('[]').strip('').replace("'", '').replace(',', ';').replace(' ', '').replace('\n', '')
            lista[escolha - 1] = strapoio
        elif listaescolha[0] == 5:
            listaapoio[4] = listaescolha[1]
            strapoio = str(listaapoio).strip('[]').strip('').replace("'", '').replace(',', ';').replace(' ', '').replace('\n', '')
            lista[escolha - 1] = strapoio
        elif listaescolha[0] == 6:
            listaapoio[5] = listaescolha[1]
            strapoio = str(listaapoio).strip('[]').strip('').replace("'", '').replace(',', ';').replace(' ', '').replace('\n', '')
            lista[escolha - 1] = strapoio
        #lista.replace('\n', '')
        a.close()

# ---------- TESTES
        #print(listaescolha)
        #print(strapoio)
        #print(lista)
# -----------------

        # ------ Regravar a lista com as modificações - Lê arquivo para gravação, subistitui os campos.
        try:
            a = open(nome, 'wt')
        except:
            print(colored('Erro ao ler arquivo...', 'red'))
        else:
            try:
                cont = 0
                for n in lista:
                    a.write(f'{lista[cont]}\n')
                    cont += 1
            except:
                print(colored('Houve um erro na hora de escrever os dados', 'red'))
            else:
                print(colored(f'OK...Modificações cadastradas com sucesso...', 'magenta'))
                linhasepara('Help Decor')
                a.close()


def excluirpecas(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(colored('Erro ao ler arquivo...', 'red'))
    else:
        lista = []
        listaapoio = []
        listagravacao = []
        strapoio = ''
        cont = 1
        listaescolha = []
        escolha1 = 0
        escolha2 = 0
        print(' Tipo         Cor     Tamanho     Composição     Quantidade      ID')
        for linha in a:
            dado = linha.split(';')  # <--- variável dado recebe a linha e separa em uma lista
            dado[5] = dado[5].replace('\n', '')  # <---Dados foram gravados no banco com \n no final
            print(f'{cont}.{dado[0]:<10}{dado[1]:^8}{dado[2]:^12}{dado[3]:^14}{dado[4]:^18}{dado[5]:>3}')
            cont += 1
            lista.append(linha.replace('\n', ''))  # <--- Transforma os dados txt em uma lista
        linhasepara('Help Decor')
        cont = 0

        # print(lista) #<--- Lista recebe todos os item do arq txt cadastrados ________ APENAS TESTES

        # < ------- Usuario ira escolher qual item da lista vai modificar
        escolha = validaint(len(lista), 'Escolha uma opção: ')

        listaapoio = lista[escolha-1].replace(';', ' ').split()  #<--transforma arq txt em lista na posição escolhida, PROBLEMA RESOLVIDO, TIRA PULA LINHA PARA GRAVAÇÂO POSTERIOR

# ------------- TESTES
        #print(lista)  #<-------- lista recebendo todas as informações do arq txt
        #print(escolha)  #<------ escolha do usuário
        #print(listaapoio)  #<--- Lista com os dados do txt separados
        del(lista[escolha-1])
        #print(lista)
# --------------------
        # ------ Regravar a lista com as modificações - Lê arquivo para gravação, subistitui os campos.
        try:
            a = open(nome, 'wt')
        except:
            print(colored('Erro ao ler arquivo...', 'red'))
        else:
            try:
                cont = 0
                for n in lista:
                    a.write(f'{lista[cont]}\n')
                    cont += 1
            except:
                print(colored('Houve um erro na hora de escrever os dados', 'red'))
            else:
                print(colored(f'OK...Modificações cadastradas com sucesso...', 'magenta'))
                linhasepara('Help Decor')
                a.close()

#<------- CONEXÃO COM BANCO DE DADOS
def criarconexao():
    dados_conexao = (           #<------ Dados para conexão ao bando de dados
        'Driver={SQL Server};'
        'Server=SAMSUNG;'
        'user=admin;'
        'passwd=admin;'
        'Database=Helpdecor;'
    )
    conexao = pyodbc.connect(dados_conexao)  # <------ Objeto criado para conectar ao bando de dados
    return conexao.cursor()  # <--- Retorna a conexão com o servidor

#<------- INICIO CADASTRO SQL
#<------- CADASTRO DE CLIENTES
def criartabelacadcliente(cursor):
    comando = """Use Helpdecor
        create table cadcliente(
        idc int,
        nome varchar(50),
        sobrenome varchar(50),
        telefone varchar(20),
        endereco varchar(50),
        email varchar(20),
    )"""
    cursor.execute(comando)


def cadastroclienteSQL(cursor, idc, nome='', sobrenome='', telefone=0, endereco='', email=''):
    comando = f"""INSERT INTO cadcliente(idc, nome, sobrenome, telefone, endereco, email)
                               Values
                          ('{idc}','{nome}','{sobrenome}', {telefone}, '{endereco}', '{email}')"""
    cursor.execute(comando)
    cursor.commit()


def maxcliente(cursor):
    comando = """SELECT max(idc) FROM cadcliente"""
    cursor.execute(comando)
    for maximo in cursor:
        if maximo[0] == None:
            idc = 1
            return idc
        else:
            idc = maximo[0] + 1
            return idc


def verclienteSQL(cursor):
    comando = """SELECT * FROM cadcliente"""
    cursor.execute(comando)
    print(colored('ID            Nome                     Telefone                      Endereço                  Email', 'magenta'))
    for cadastro in cursor:
        print(colored(f'{cadastro[0]}.       {cadastro[1]} {cadastro[2]}{cadastro[3]:^32}{cadastro[4]:^20}          {cadastro[5]:>20}', 'green'))
    linhasepara('Help Decor')


def pesquisaclienteSQL(cursor):
    while True:
        pesquisa = str(input('Digite uma palavra chave para pesquisa ou 0 para voltar: ')).title()
        linhasepara('Help Decor')
        contpeca = 0
        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadcliente
                            WHERE idc like '{pesquisa}' or
                            nome like '{pesquisa}%' or
                            sobrenome like '{pesquisa}%' or
                            telefone like '{pesquisa}%' or
                            endereco like '{pesquisa}%' or
                            email like '{pesquisa}%'"""
            cursor.execute(comando)
            print(colored('ID            Nome                     Telefone                      Endereço                  Email', 'magenta'))
            for cadastro in cursor:
                print(colored(f'{cadastro[0]}.       {cadastro[1]} {cadastro[2]}{cadastro[3]:^32}{cadastro[4]:^20}          {cadastro[5]:>20}', 'green'))
                contpeca += 1
            print(colored(f'\nEncontrei {contpeca} cliente(s) com essa característica....', 'magenta'))
            linhasepara('Help Decor')
            break


def editarclienteSQL(cursor):
    while True:
        cadastros = 1
        comando = """SELECT * FROM cadcliente"""
        cursor.execute(comando)
        print(colored('ID            Nome                     Telefone                      Endereço                  Email', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]}.       {cadastro[1]} {cadastro[2]}{cadastro[3]:^32}{cadastro[4]:^20}          {cadastro[5]:>20}', 'green'))
            cadastros += 1
        linhasepara('Help Decor')
        pesquisa = validaint(cadastros, 'Digite um número na lista para editar cadastro ou 0 para voltar: ')
        if pesquisa == 0:
            print(colored('Voltando...', 'magenta'))
            linhasepara('Help Decor')
            break
        else:
            comando = f"""SELECT * FROM cadcliente
                            WHERE idc='{pesquisa}'"""
            cursor.execute(comando)
            print(colored('OK...vamos editar o seguinte cadastro...', 'magenta'))
            print(colored('ID            Nome                     Telefone                      Endereço                  Email', 'magenta'))
            for cadastro in cursor:
                print(colored(f'{cadastro[0]}.       {cadastro[1]} {cadastro[2]}{cadastro[3]:^32}{cadastro[4]:^20}          {cadastro[5]:>20}', 'green'))
                linhasepara('Help Decor')
            escolha = validaint(6, 'Qual caracteristica deseja trocar: \n'
                                    '[1]ID\n'
                                    '[2]Nome\n'
                                    '[3]Sobrenome\n'                                        
                                    '[4]Telefone\n'
                                    '[5]Endereço\n'
                                    '[6]Email ')
            escolha2 = str(input(f'Digite a alteração: ')).strip().title()
            if escolha == 1:
                comando = f"""UPDATE cadcliente
                                 SET idc={escolha2}
                                WHERE idc={pesquisa}"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 2:
                comando = f"""UPDATE cadcliente
                                 SET nome='{escolha2}'
                                WHERE idc='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 3:
                comando = f"""UPDATE cadcliente
                                 SET sobrenome='{escolha2}'
                                WHERE idc='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 4:
                comando = f"""UPDATE cadcliente
                                 SET telefone={escolha2}
                                WHERE idc={pesquisa}"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 5:
                comando = f"""UPDATE cadcliente
                                 SET endereco='{escolha2}'
                                WHERE idc='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 6:
                comando = f"""UPDATE cadcliente
                                 SET email='{escolha2}'
                                WHERE idc='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break


def excluirclienteSQL(cursor):
    while True:
        cadastros = 0
        comando = """SELECT * FROM cadcliente"""
        cursor.execute(comando)
        print(colored('ID            Nome                     Telefone                      Endereço                  Email', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]}.       {cadastro[1]} {cadastro[2]}{cadastro[3]:^32}{cadastro[4]:^20}          {cadastro[5]:>20}', 'green'))
            cadastros +=1
        linhasepara('Help Decor')

        pesquisa = validaint(cadastros, 'Digite um número na lista para excluir cadastro ou 0 para voltar: ')
        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadcliente
                            WHERE idc={pesquisa}"""
            print(colored(f'Deletando cliente {cadastro[1]} {cadastro[2]}...', 'magenta'))
            comando = f"""DELETE FROM cadcliente
                            WHERE idc={pesquisa}"""
            cursor.execute(comando)
            cursor.commit()
            linhasepara('Help Decor')
            break

#<------- CADASTRO DE FESTAS
def criartabelacadfestas(cursor):
    comando = """Use Helpdecor
        create table cadfestas(
        idf int,
        nome varchar(50),
        sobrenome varchar(20),
        tema varchar(20),
        data date,
    )"""
    cursor.execute(comando)


def cadastrofestaSQL(cursor, idf, nome, sobrenome, tema, data):
    comando = f"""INSERT INTO cadfestas(idf, nome, sobrenome, tema, data)
                    Values
                        ('{idf}', '{nome}', '{sobrenome}', '{tema}', '{data}')"""
    cursor.execute(comando)
    cursor.commit()


def maxfesta(cursor):
    comando = """SELECT max(idf) FROM cadfestas"""
    cursor.execute(comando)
    for maximo in cursor:
        if maximo[0] == None:
            idf = 1
            return idf
        else:
            idf = maximo[0] + 1
            return idf


def verfestasSQL(cursor):
    comando = """SELECT * FROM cadfestas"""
    cursor.execute(comando)
    print(colored('ID                      Nome                               Tema                               Data', 'magenta'))
    for cadastro in cursor:
        print(colored(f'{cadastro[0]}.                {cadastro[1]} {cadastro[2]}                {cadastro[3]:^32}   {cadastro[4]:>20}', 'green'))
    linhasepara('Help Decor')


def pesquisafestasSQL(cursor):
    while True:
        pesquisa = str(input('Digite uma palavra chave para pesquisa ou 0 para voltar: ')).capitalize()
        contpeca = 0

        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadfestas
                            WHERE nome like '{pesquisa}%' or
                            sobrenome like '{pesquisa}%' or
                            tema like '{pesquisa}%' or
                            data like '{pesquisa}%'"""
            cursor.execute(comando)
            print(colored('ID                      Nome                               Tema                               Data', 'magenta'))
            cont = 1
            for cadastro in cursor:
                print(colored(f'{cadastro[0]}.                {cadastro[1]} {cadastro[2]}                {cadastro[3]:^32}   {cadastro[4]:>20}', 'green'))
                contpeca += 1
                cont += 1
            print(colored(f'\nEncontrei {contpeca} festa(s) com essa característica....', 'magenta'))
            linhasepara('Help Decor')
            break


def editarfestasSQL(cursor):
    while True:
        cadastros = 1
        comando = """SELECT * FROM cadfestas"""
        cursor.execute(comando)
        print(colored('ID                      Nome                               Tema                               Data', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]}.                {cadastro[1]} {cadastro[2]}                {cadastro[3]:^32}   {cadastro[4]:>20}', 'green'))
            cadastros += 1
        linhasepara('Help Decor')
        pesquisa = validaint(cadastros, 'Digite um número na lista para editar cadastro ou 0 para voltar: ')
        if pesquisa == 0:
            print(colored('Voltando...', 'magenta'))
            linhasepara('Help Decor')
            break
        else:
            comando = f"""SELECT * FROM cadfestas
                            WHERE idf='{pesquisa}'"""
            cursor.execute(comando)
            print(colored('OK...vamos editar o seguinte cadastro...', 'magenta'))
            print(colored('ID                      Nome                               Tema                               Data', 'magenta'))
            for cadastro in cursor:
                print(colored(f'{cadastro[0]}.                {cadastro[1]} {cadastro[2]}                {cadastro[3]:^32}   {cadastro[4]:>20}', 'green'))
                linhasepara('Help Decor')
            escolha = validaint(5, 'Qual caracteristica deseja trocar: \n'
                                    '[1]ID\n'
                                    '[2]Nome\n'
                                    '[3]Sobrenome\n'                                        
                                    '[4]Tema\n'
                                    '[5]Data ')
            escolha2 = str(input(f'Digite a alteração: ')).strip().title()
            if escolha == 1:
                comando = f"""UPDATE cadfestas
                                 SET idf={escolha2}
                                WHERE idf={pesquisa}"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 2:
                comando = f"""UPDATE cadfestas
                                 SET nome='{escolha2}'
                                WHERE idf='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 3:
                comando = f"""UPDATE cadfestas
                                 SET sobrenome='{escolha2}'
                                WHERE idf='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 4:
                comando = f"""UPDATE cadfestas
                                 SET tema={escolha2}
                                WHERE idf={pesquisa}"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 5:
                comando = f"""UPDATE cadfestas
                                 SET data='{escolha2}'
                                WHERE idf='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break


def excluirfestasSQL(cursor):
    while True:
        cadastros = 0
        comando = """SELECT * FROM cadfestas"""
        cursor.execute(comando)
        print(colored('ID                      Nome                               Tema                               Data', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]}.                {cadastro[1]} {cadastro[2]}                {cadastro[3]:^32}   {cadastro[4]:>20}', 'green'))
            cadastros +=1
        linhasepara('Help Decor')

        pesquisa = validaint(cadastros, 'Digite um número na lista para excluir cadastro ou 0 para voltar: ')
        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadfestas
                            WHERE idf={pesquisa}"""
            print(colored(f'Deletando festa da(o) {cadastro[1]} {cadastro[2]}...', 'magenta'))
            comando = f"""DELETE FROM cadfestas
                            WHERE idf={pesquisa}"""
            cursor.execute(comando)
            cursor.commit()
            linhasepara('Help Decor')
            break

#<------- CADASTRO DE PEÇAS
def criartabelacadpecas(cursor):
    comando = """Use Helpdecor
        create table cadpecas(
        idp int,
        tipo varchar(20),
        cor varchar(20),
        tamanho varchar(20),
        composicao varchar(20),
        quantidade int,
        coddecor int,
    )"""
    cursor.execute(comando)


def cadastropecasSQL(cursor, idp, tipo, cor, tamanho, composicao, quantidade, coddecor):
    comando = f"""INSERT INTO cadpecas(idp, tipo, cor, tamanho, composicao, quantidade, coddecor)
                    Values
                        ('{idp}', '{tipo}', '{cor}', '{tamanho}', '{composicao}', '{quantidade}', '{coddecor}')"""
    cursor.execute(comando)
    cursor.commit()


def maxpecas(cursor):
    comando = """SELECT max(idp) FROM cadpecas"""
    cursor.execute(comando)
    for maximo in cursor:
        if maximo[0] == None:
            idp = 1
            return idp
        else:
            idp = maximo[0] + 1
            return idp


def verpecasSQL(cursor):
    comando = """SELECT * FROM cadpecas"""
    cursor.execute(comando)
    print(colored('ID       Tipo         Cor            Tamanho              Composição           Quantidade          CÓD', 'magenta'))
    for cadastro in cursor:
        print(colored(f'{cadastro[0]:<7}{cadastro[1]:<13}{cadastro[2]:<14}{cadastro[3]:<21}{cadastro[4]:<28}{cadastro[5]:<16}{cadastro[6]}', 'green'))
    linhasepara('Help Decor')


def pesquisapecasSQL(cursor):
    while True:
        pesquisa = str(input('Digite uma palavra chave para pesquisa ou 0 para voltar: ')).capitalize()
        contpeca = 0

        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadpecas
                            WHERE idp like '{pesquisa}%' or
                            tipo like '{pesquisa}%' or
                            cor like '{pesquisa}%' or
                            tamanho like '{pesquisa}%' or
                            composicao like '{pesquisa}%' or
                            quantidade like '{pesquisa}%' or
                            coddecor like '{pesquisa}%'"""
            cursor.execute(comando)
            print(colored('ID       Tipo         Cor            Tamanho              Composição           Quantidade          CÓD', 'magenta'))
            for cadastro in cursor:
                print(colored(f'{cadastro[0]:<7}{cadastro[1]:<13}{cadastro[2]:<14}{cadastro[3]:<21}{cadastro[4]:<28}{cadastro[5]:<16}{cadastro[6]}', 'green'))
                contpeca += 1
            print(colored(f'\nEncontrei {contpeca} peça(s) com essa característica....', 'magenta'))
            linhasepara('Help Decor')
            break


def editarpecasSQL(cursor):
    while True:
        cadastros = 1
        comando = """SELECT * FROM cadpecas"""
        cursor.execute(comando)
        print(colored('ID       Tipo         Cor            Tamanho              Composição           Quantidade          CÓD', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]:<7}{cadastro[1]:<13}{cadastro[2]:<14}{cadastro[3]:<21}{cadastro[4]:<28}{cadastro[5]:<16}{cadastro[6]}', 'green'))
            cadastros += 1
        linhasepara('Help Decor')
        pesquisa = validaint(cadastros, 'Digite um número na lista para editar cadastro ou 0 para voltar: ')
        if pesquisa == 0:
            print(colored('Voltando...', 'magenta'))
            linhasepara('Help Decor')
            break
        else:
            comando = f"""SELECT * FROM cadpecas
                            WHERE idp='{pesquisa}'"""
            cursor.execute(comando)
            print(colored('OK...vamos editar o seguinte cadastro...', 'magenta'))
            print(colored('ID       Tipo         Cor            Tamanho              Composição           Quantidade          CÓD', 'magenta'))
            for cadastro in cursor:
                print(colored(f'{cadastro[0]:<7}{cadastro[1]:<13}{cadastro[2]:<14}{cadastro[3]:<21}{cadastro[4]:<28}{cadastro[5]:<16}{cadastro[6]}', 'green'))
                linhasepara('Help Decor')
            escolha = validaint(7, 'Qual caracteristica deseja trocar: \n'
                                    '[1]ID\n'
                                    '[2]Tipo\n'
                                    '[3]Cor\n'                                        
                                    '[4]Tamanho\n'
                                    '[5]Composição\n'
                                    '[6]Quantidade\n'
                                    '[7]Cód Decoradora')
            escolha2 = str(input(f'Digite a alteração: ')).strip().title()
            if escolha == 1:
                comando = f"""UPDATE cadpecas
                                 SET idp={escolha2}
                                WHERE idp={pesquisa}"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 2:
                comando = f"""UPDATE cadpecas
                                 SET tipo='{escolha2}'
                                WHERE idp='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 3:
                comando = f"""UPDATE cadpecas
                                 SET cor='{escolha2}'
                                WHERE idp='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 4:
                comando = f"""UPDATE cadpecas
                                 SET tamanho='{escolha2}'
                                WHERE idp='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 5:
                comando = f"""UPDATE cadpecas
                                 SET composicao='{escolha2}'
                                WHERE idp='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 6:
                comando = f"""UPDATE cadpecas
                                 SET quantidade='{escolha2}'
                                WHERE idp='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 7:
                comando = f"""UPDATE cadpecas
                                 SET coddecor='{escolha2}'
                                WHERE idp='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break


def excluirpecasSQL(cursor):
    while True:
        cadastros = 0
        comando = """SELECT * FROM cadpecas"""
        cursor.execute(comando)
        print(colored('ID       Tipo         Cor            Tamanho              Composição           Quantidade          CÓD', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]:<7}{cadastro[1]:<13}{cadastro[2]:<14}{cadastro[3]:<21}{cadastro[4]:<28}{cadastro[5]:<16}{cadastro[6]}', 'green'))
            cadastros +=1
        linhasepara('Help Decor')

        pesquisa = validaint(cadastros, 'Digite um número na lista para excluir cadastro ou 0 para voltar: ')
        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadpecas
                            WHERE idp={pesquisa}"""

            print(colored(f'Deletando peça {cadastro[1]} {cadastro[2]}...', 'magenta'))
            comando = f"""DELETE FROM cadpecas
                            WHERE idp={pesquisa}"""
            cursor.execute(comando)
            cursor.commit()
            linhasepara('Help Decor')
            break

#<------- CADASTRO DE FORNECEDORES
def criartabelacadfornecedor(cursor):
    comando = """Use Helpdecor
        create table cadfornecedor(
        idfor int,
        nome varchar(30),
        tipo varchar(20),
        telefone varchar(20),
        email varchar(20),
        cnpj varchar(30),
    )"""
    cursor.execute(comando)


def cadastrofornecedorSQL(cursor, idfor, nome, tipo, telefone, email, cnpj):
    comando = f"""INSERT INTO cadfornecedor(idfor, nome, tipo, telefone, email, cnpj)
                    Values
                        ('{idfor}', '{nome}', '{tipo}', '{telefone}', '{email}', '{cnpj}')"""
    cursor.execute(comando)
    cursor.commit()


def maxfornecedor(cursor):
    comando = """SELECT max(idfor) FROM cadfornecedor"""
    cursor.execute(comando)
    for maximo in cursor:
        if maximo[0] == None:
            idfor = 1
            return idfor
        else:
            idfor = maximo[0] + 1
            return idfor


def verfornecedorSQL(cursor):
    comando = """SELECT * FROM cadfornecedor"""
    cursor.execute(comando)
    print(colored('ID         Nome                 Tipo                Telefone            Email                CNPJ', 'magenta'))
    for cadastro in cursor:
        print(colored(f'{cadastro[0]:<6}{cadastro[1]:<18}{cadastro[2]:<24}{cadastro[3]:<20}{cadastro[4]:<18}{cadastro[5]}', 'green'))
    linhasepara('Help Decor')


def pesquisafornecedorSQL(cursor):
    while True:
        pesquisa = str(input('Digite uma palavra chave para pesquisa ou 0 para voltar: ')).capitalize()
        contpeca = 0

        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadfornecedor
                            WHERE idfor like '{pesquisa}%' or
                            nome like '{pesquisa}%' or
                            tipo like '{pesquisa}%' or
                            telefone like '{pesquisa}%' or
                            email like '{pesquisa}%' or
                            cnpj like '{pesquisa}%'"""
            cursor.execute(comando)
            print(colored('ID         Nome                 Tipo                Telefone            Email                CNPJ', 'magenta'))
            for cadastro in cursor:
                print(colored(f'{cadastro[0]:<6}{cadastro[1]:<18}{cadastro[2]:<24}{cadastro[3]:<20}{cadastro[4]:<18}{cadastro[5]}', 'green'))
                contpeca += 1
            print(colored(f'\nEncontrei {contpeca} fornecedore(s) com essa característica....', 'magenta'))
            linhasepara('Help Decor')
            break


def editarfornecedorSQL(cursor):
    while True:
        cadastros = 1
        comando = """SELECT * FROM cadfornecedor"""
        cursor.execute(comando)
        print(colored('ID         Nome                 Tipo                Telefone            Email                CNPJ', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]:<6}{cadastro[1]:<18}{cadastro[2]:<24}{cadastro[3]:<20}{cadastro[4]:<18}{cadastro[5]}', 'green'))
            cadastros += 1
        linhasepara('Help Decor')
        pesquisa = validaint(cadastros, 'Digite um número na lista para editar cadastro ou 0 para voltar: ')
        if pesquisa == 0:
            print(colored('Voltando...', 'magenta'))
            linhasepara('Help Decor')
            break
        else:
            comando = f"""SELECT * FROM cadfornecedor
                            WHERE idfor='{pesquisa}'"""
            cursor.execute(comando)
            print(colored('OK...vamos editar o seguinte cadastro...', 'magenta'))
            print(colored('ID         Nome                 Tipo                Telefone            Email                CNPJ', 'magenta'))
            for cadastro in cursor:
                print(colored(f'{cadastro[0]:<6}{cadastro[1]:<18}{cadastro[2]:<24}{cadastro[3]:<20}{cadastro[4]:<18}{cadastro[5]}', 'green'))
                linhasepara('Help Decor')
            escolha = validaint(6, 'Qual caracteristica deseja trocar: \n'
                                    '[1]ID\n'
                                    '[2]Nome\n'
                                    '[3]Tipo\n'                                        
                                    '[4]Telefone\n'
                                    '[5]Email\n'
                                    '[6]CNPJ')
            escolha2 = str(input(f'Digite a alteração: ')).strip().title()
            if escolha == 1:
                comando = f"""UPDATE cadfornecedor
                                 SET idfor={escolha2}
                                WHERE idfor={pesquisa}"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 2:
                comando = f"""UPDATE cadfornecedor
                                 SET nome='{escolha2}'
                                WHERE idfor='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 3:
                comando = f"""UPDATE cadfornecedor
                                 SET tipo='{escolha2}'
                                WHERE idfor='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 4:
                comando = f"""UPDATE cadfornecedor
                                 SET telefone='{escolha2}'
                                WHERE idfor='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 5:
                comando = f"""UPDATE cadfornecedor
                                 SET email='{escolha2}'
                                WHERE idfor='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break
            if escolha == 6:
                comando = f"""UPDATE cadfornecedor
                                 SET cnpj='{escolha2}'
                                WHERE idfor='{pesquisa}'"""
                print(colored('Editando cadastro...', 'magenta'))
                cursor.execute(comando)
                cursor.commit()
                linhasepara('Help Decor')
                break


def excluirfornecedorSQL(cursor):
    while True:
        cadastros = 0
        comando = """SELECT * FROM cadfornecedor"""
        cursor.execute(comando)
        print(colored('ID         Nome                 Tipo                Telefone            Email                CNPJ', 'magenta'))
        for cadastro in cursor:
            print(colored(f'{cadastro[0]:<6}{cadastro[1]:<18}{cadastro[2]:<24}{cadastro[3]:<20}{cadastro[4]:<18}{cadastro[5]}', 'green'))
            cadastros +=1
        linhasepara('Help Decor')

        pesquisa = validaint(cadastros, 'Digite um número na lista para excluir cadastro ou 0 para voltar: ')
        if pesquisa == '0':
            break
        else:
            comando = f"""SELECT * FROM cadfornecedor
                            WHERE idfor={pesquisa}"""

            print(colored(f'Deletando peça {cadastro[1]} {cadastro[2]}...', 'magenta'))
            comando = f"""DELETE FROM cadfornecedor
                            WHERE idfor={pesquisa}"""
            cursor.execute(comando)
            cursor.commit()
            linhasepara('Help Decor')
            break
