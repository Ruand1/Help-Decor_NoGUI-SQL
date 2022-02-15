# ----- Importando bibliotecas
from HelpDecor import*
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


#GUI = Builder.load_file('HelpDecor.kv')

class gerenciador(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        nomecliente = str(self.get_screen('cadastrar_cliente').ids.teste.text)
        self.get_screen('cadastrar_cliente').ids.teste2.text = nomecliente
        print(nomecliente)

class cadastro_de_clientes(Screen):
    pass

class cadastro_de_festas(Screen):
    pass

class cadastro_de_pecas(Screen):
    pass

class cadastro_de_fornecedor(Screen):
    pass

class cadastrar_cliente(Screen):
    pass

class HelpDecor(App):
    def build(self):

        return gerenciador()

HelpDecor().run()



"""print(colored('Carregando Banco de Dados....', 'magenta'))
cursor = criarconexao()  #<---- Cursor vira objeto para conexão com o BD
print('Conexão bem sucedida!!!')

# <------- Cria tabela cadastros no banco de dados
criartabelacadcliente(cursor)
print(colored('Conexão Cadastro Clientes OK...!!!', 'magenta'))
sleep(0.5)
criartabelacadfestas(cursor)
print(colored('Conexão Cadastro Festas OK...!!!', 'magenta'))
sleep(0.5)
criartabelacadpecas(cursor)
print(colored('Conexão Cadastro Peças OK...!!!', 'magenta'))
criartabelacadfornecedor(cursor)
print(colored('Conexão Cadastro Fornecedores OK...!!!', 'magenta'))
sleep(1)


# ----- Programa principal
# --- Tela Carregamento
carregamento('HELP DECOR')

# --- Inicio da AI(Ambrósio)
#inteligencia1('HELP DECOR') ------------------------------------------------------------------ INCLUIR PÓS TESTES

# --- Loop Menu
while True:
    menu(['Cadastro de Clientes', 'Cadastro Festas', 'Cadastro Peças de Decoração', 'Cadastro de Fornecedores', 'Sair'])

    num = validaint(5, 'Escolha uma opção:')  # <-------- num recebe função de validação da opção escolhida

    #inteligencia2(num, menu, 'HELP DECOR') ----------------------------------------------------INCLUIR PÓS TESTES
    linhasepara('Help Decor')

# --- Cadastro Clientes
    if num == 1:
        while True:
            cliente = cadastrocliente()  #<----- função para clientes
            if cliente == 1:
                nomecliente = str(input(colored('Primeiro nome do cliente:', 'green'))).strip().title()
                sleep(0.5)
                sobrenomecliente = str(input(colored('Sobrenome do cliente:', 'green'))).strip().title()
                sleep(0.5)
                telefone = str(input(colored('Telefone do cliente:', 'green')))
                sleep(0.5)
                endereco = str(input(colored('Endereço do cliente:', 'green'))).strip().title()
                sleep(0.5)
                email = str(input(colored('Email do cliente:', 'green'))).strip().title()
                idcliente = maxcliente(cursor)  #<--- Função busca ultimo ID e continua a contagem
                cadastroclienteSQL(cursor, idcliente, nomecliente, sobrenomecliente, telefone, endereco, email)
                linhasepara('Help Decor')
            elif cliente == 2:
                try:
                    sleep(0.5)
                    linhasepara('HELP DECOR')
                    verclienteSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos clientes cadastradas(os)...', 'magenta'))
                    linhasepara('Help Decor')
            elif cliente == 3:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    pesquisaclienteSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos clientes cadastradas(os)...', 'magenta'))
                    linhasepara('Help Decor')
            elif cliente == 4:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    editarclienteSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos clientes cadastradas(os)...', 'magenta'))
                    linhasepara('Help Decor')
            elif cliente == 5:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    excluirclienteSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos clientes cadastradas(os)...', 'magenta'))
                    linhasepara('Help Decor')
            else:
                print(colored('Voltando....', 'magenta'))
                linhasepara('Help Decor')
                break
# --- Cadastro Festas
    if num == 2:
        while True:
            festas = cadastrofestas()  #<----- função para cadastro e ver festas
            if festas == 1:
                nomecliente = str(input(colored('Nome do cliente:', 'green'))).strip().title()
                sleep(0.5)
                sobrenomecliente = str(input(colored('Sobrenome do cliente:', 'green'))).strip().title()
                sleep(0.5)
                tema = str(input(colored('Tema da festa:', 'green'))).strip().title()
                sleep(0.5)
                data = str(input(colored('Data da festa:', 'green'))).strip()
                sleep(0.5)
                idfestas = maxfesta(cursor)  # <--- Função busca ultimo ID e continua a contagem
                cadastrofestaSQL(cursor, idfestas, nomecliente, sobrenomecliente, tema, data)
                linhasepara('Help Decor')
            elif festas == 2:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    verfestasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos festas cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif festas == 3:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    pesquisafestasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos festas cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif festas == 4:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    editarfestasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos festas cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif festas == 5:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    excluirfestasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos festas cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            else:
                print(colored('Voltando....', 'magenta'))
                linhasepara('Help Decor')
                break
# --- Cadastro Peças Decoração
    if num == 3:
        while True:
            pecas = cadastropecas()  #<----- função para cadastro e ver peças
            if pecas == 1:
                tipo = str(input(colored('Tipo de peça:', 'green'))).strip().title()
                sleep(0.5)
                cor = str(input(colored('Cor da peça:', 'green'))).strip().title()
                sleep(0.5)
                tamanho = str(input(colored('Tamanho da peça:', 'green'))).strip().title()
                sleep(0.5)
                composicao = str(input(colored('Material da peça:', 'green'))).strip().title()
                sleep(0.5)
                quantidade = int(input(colored('Quantidade de peças:', 'green')))
                sleep(0.5)
                coddecor = validaint(200, colored('Cód da Decor:', 'green'))
                idpecas = maxpecas(cursor)  # <--- Função busca ultimo ID e continua a contagem
                cadastropecasSQL(cursor, idpecas, tipo, cor, tamanho, composicao, quantidade, coddecor)
                linhasepara('Help Decor')
            elif pecas == 2:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    verpecasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif pecas == 3:  #<--- V1.0.1 - Incluído módulo de pesquisa - funcionando ok
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    pesquisapecasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif pecas == 4:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    editarpecasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif pecas == 5:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    excluirpecasSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
            else:
                print(colored('Voltando...', 'magenta'))
                linhasepara('Help Decor')
                break
# --- Cadastro de Fornecedores
    if num == 4:
        while True:
            fornecedor = cadastrofornecedor()  #<----- função para cadastro e ver fornecedores
            if fornecedor == 1:
                nome = str(input(colored('Nome do fornecedor:', 'green'))).strip().title()
                sleep(0.5)
                tipo = str(input(colored('Tipo de fornecedor:', 'green'))).strip().title()
                sleep(0.5)
                telefone = str(input(colored('Telefone do fornecedor:', 'green'))).strip().title()
                sleep(0.5)
                email = str(input(colored('Email do fornecedor:', 'green'))).strip().title()
                sleep(0.5)
                cnpj = str(input(colored('CNPJ do fornecedor:', 'green')))
                sleep(0.5)
                idfornecedor = maxfornecedor(cursor)  # <--- Função busca ultimo ID e continua a contagem
                cadastrofornecedorSQL(cursor, idfornecedor, nome, tipo, telefone, email, cnpj)
                linhasepara('Help Decor')
            elif fornecedor == 2:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    verfornecedorSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif fornecedor == 3:  #<--- V1.0.1 - Incluído módulo de pesquisa - funcionando ok
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    pesquisafornecedorSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif fornecedor == 4:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    editarfornecedorSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
                    linhasepara('Help Decor')
            elif fornecedor == 5:
                try:
                    sleep(0.5)
                    linhasepara('Help Decor')
                    excluirfornecedorSQL(cursor)
                except IndexError:
                    print(colored('Ops... Ainda não temos peças cadastradas...', 'magenta'))
            else:
                print(colored('Voltando...', 'magenta'))
                linhasepara('Help Decor')
                break
# --- Sair
    if num == 5:
        print(colored('Volte sempre que precisar...', 'magenta'))
        break




#  <--------------CHECK THIS - for upgrade
# --------------- Incluir módulo de locação
# --------------- fazer validação int para quantidade de peça - verificar necessidade




#  <------------------ LOGs below - update from 29/01/2022
#  <------------------ DON'T UPGRADE TO PYTHON 3.10 ---- DONT WORK WITH KIVY SO FAR
#  <------------------ The version that work today is version is 3.9.7 (29/01/2022)

#< --------- https://docs.microsoft.com/pt-br/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2
#< --------- Liberar scripts --- Use POWERSHELL

#< --------- https://kivy.org/doc/stable/gettingstarted/installation.html#using-pip
#< --------- Instalação e configuração do Kivy
#< --------- pip install --upgrade pip setuptools virtualenv        Atualiza PIP e maquinas virtuais
#< --------- virtualenv kivy_venv                                   Cria maquina virtual
#< --------- kivy_venv\Scripts\activate                             Ativa script


#< --------- 29/01/22 ------ Para utilizar o Kivy, não podemos utilizar a versão 3.10 do python,
#< --------- somente versão 3.9.7.....VERIFICAR INSTALAÇÃO


#< ----- link Como Criar Aplicativos e Programas com Python - Introdução ao Kivy """

