import pickle
import random
import os
import usersVars
import sys
from time import sleep


## Variaveis com dados iniciais.
initial_admin = {0:('test', '123', 10000, 0.0, 'Gerente', '', 0.0, '', '', True)}
userVerification = False
passVerification = False
statusVerification = False
tryLogin = True
tryRegister = False
inMenu = False
tryGerente = True
tryChangePassword = False
# Tentativas de login com falhas
failedAttempts = 0 

# Dict de exemplo
ex_database = {0:('test', '123', 10000, 0.0, 'Gerente', '', 0.0, '', '+55 (55) 55555-5555', True),
               1:('person', '123', 84591, 275.53, 'Davi Cavalcanti Rodrigues', 'Arquiteto', 10125.0, 'Rua Nilda de Araújo 522', '+55 (19) 98814-5612', False),
               2:('person', '123', 55672, 275.53, 'Martim Martins Correia', 'Arqueologa', 7597.0, 'Quadra EQNM 34/36 Área Especial s/n 1867', '+55 (19) 98912-4832', False),
               3:('person', '123', 33471, 275.53, 'Vitor Costa Lima', 'Jornalista', 7991.0, 'Rua São Francisco 217', '+55 (19) 98791-9512', False),
               4:('person', '123', 99812, 275.53, 'Bruno Fernandes Melo', 'Arquiteto', 8698.0, 'Rua Engenheiro Alfredo Geraldo Sica Pinto 26', '+55 (19) 98155-4612', False),
               5:('person', '123', 12074, 275.53, 'Gabriel Santos Costa', 'Dependente', 6745.0, 'Rua Muniz de Sousa 144', '+55 (19) 98915-1535', False),
               6:('person', '123', 90145, 275.53, 'Vitor Fernandes Correia', 'Garçonete', 2239.0, 'Rua Borá, 117', '+55 (19) 99832-0784', False),
               7:('person', '123', 11354, 275.53, 'Luis Correia Fernandes', 'Advogado', 8353.0, 'Rua Mensageiro João Sarmento, 1475', '+55 (19) 99884-9120', False),
               8:('person', '123', 13977, 275.53, 'Murilo Cunha Rodrigues', 'Cabeleireiro', 2379.0, 'Praça Marechal Carmona, 862', '+55 (19) 99761-6851', False),
               9:('person', '123', 14941, 275.53, 'Vinicius Barbosa Araujo', 'Taxista', 13546.0, 'Rua Miquelina Dias, 111', '+55 (19) 99835-3071', False),
               10:('person', '123', 71997, 275.53, 'Diego Melo Carvalho', 'Biologa', 9325.0, 'Viela Pioneiro Antônio Barbosa do Amaral, 179', '+55 (19) 98901-1501', False),
               11:('person', '123', 72661, 275.53, 'Bruno Souza Almeida', 'Cabeleireiro', 1575.0, 'Estrada Philuvio Cerqueira Rodrigues, 810', '+55 (19) 98915-6712', False),
               12:('person', '123', 73551, 275.53, 'Mateus Cardoso Barros', 'Professor', 4129.0, 'Rua Riachuelo, 1010', '+55 (19) 98865-3682', False),
               13:('person', '123', 74263, 275.53, 'Guilherme Fernandes Correia', 'Enfermeira', 10185.0, 'Rua Sílvio Cardoso Tavares, 1995', '+55 (19) 98748-8792', False),
               14:('person', '123', 91647, 275.53, 'Martim Azevedo Fernandes', 'Dependente', 2738.0, 'Rua Duque de Caxias, 1390', '+55 (19) 99767-1693', False),
               15:('person', '123', 92243, 275.53, 'Antonio Cardoso Pinto', 'Policial', 7171.0, 'Rua Emerentina Pinheiro Guimarães, 421', '+55 (19) 99886-0781', False),
               16:('person', '123', 90017, 275.53, 'Eduardo Rodrigues Rocha', 'Maquinista', 10816.0, 'Rua Vinte e Seis, 1577', '+55 (19) 99920-6891', False),
               17:('person', '123', 93410, 275.53, 'Kai Dias Gomes', 'Arqueologo', 7191.0, 'Rua São Felan, 1411', '+55 (19) 98835-5947', False),
               18:('person', '123', 53697, 275.53, 'Diego Costa Barbosa', 'Mecanico', 10185.0, 'Travessa Bom Jesus, 1186', '+55 (19) 98768-3651', False),
               19:('person', '123', 53781, 275.53, 'Pedro Azevedo Souza', 'Carteira', 12314.0, 'Quadra Quadra 047 Conjunto H, 1763', '+55 (19) 99864-9830', False),
               20:('person', '123', 55611, 275.53, 'Estevan Carvalho Ferreira', 'Jardineiro', 10662.0, 'Rua Dois de Julho, 1568', '+55 (19) 98902-1408', False),
               21:('person', '123', 13277, 275.53, 'Tomas Castro Santos', 'Escritor', 7982.0, 'Rua Basson, 199', '+55 (19) 98800-1741', False),
               22:('person', '123', 19510, 275.53, 'Felipe Costa Almeida', 'Faxineira', 15609.0, 'Quadra C 07, 666', '+55 (19) 98867-9684', False),
               23:('person', '123', 23641, 275.53, 'Rodrigo Gomes Melo', 'Atriz', 2738.0, 'Passagem Rodolfo Moser, 1372', '+55 (19) 99962-4172', False),
               24:('person', '123', 18774, 275.53, 'Murilo Barros Correia', 'Advogado', 3041.0, 'Rua Celeste, 1758', '+55 (19) 99772-3547', False),
               25:('person', '123', 37106, 275.53, 'Kaue Azevedo Cardoso', 'Arqueologo', 5634.0, 'Rua Teodorico do Monte Wanderley, 421', '+55 (19) 99817-0917', False),
               26:('person', '123', 12429, 275.53, 'Paulo Ricardo N Lisecki', 'Maroteiro', 5634.0, 'Joao Bettega, 4301', '+55 (41) 98815-6088', False)
            }



while tryGerente:
    if os.path.exists('users.data'): ## verificando se o arquivo existe
        with open('users.data', 'rb') as f:
            users = pickle.load(f)
    else:
        with open('users.data', 'wb') as lmao:
            os.system('cls')
            print('Falha ao encontrar users.data.\n')
            print('Setup. . .')
            execute = input('')
            if execute.lower() == "standart" or execute == "1":
                pickle.dump(initial_admin, lmao, pickle.HIGHEST_PROTOCOL)
                sys.exit('Favor reiniciar o aplicativo')
            if execute.lower() == "example" or execute == "2":
                pickle.dump(ex_database, lmao, pickle.HIGHEST_PROTOCOL)
                sys.exit('Favor reiniciar o aplicativo')
            else:
                sys.exit('Erro de validacao')


    ## LOGIN ##    
    while tryLogin:
        if os.path.exists('users.data'): ## verificando se o arquivo existe
            with open('users.data', 'rb') as f:
                users = pickle.load(f)
        #users[usersVars.userID] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status ## definicao de um login (username, password e status)
    
    
        userVerification = False
        passVerification = False
        statusVerification = False
        os.system('cls')
        print("Por favor realize o seu login para que possamos continuar...\n")
        usersVars.username = str(input("Usuario: "))
        usersVars.password = str(input("Senha: "))

        for i in range(len(users)):
            if usersVars.username == users[i][0] and usersVars.password == users[i][1] and users[i][9] == True:
                print(f"\nSucesso!")
                tryLogin = False
                inMenu = True
                sleep(.3)
                break;
        else:
            #users.close()
            input("\nErro!\nLogin/Senha Invalidos.")
            tryLogin = True


    if tryRegister:
        os.system('cls') # Limpar tela
        if os.path.exists('users.data'): ## verificando se o arquivo existe
            with open('users.data', 'rb') as f:
                users = pickle.load(f)
            #with open('users.data', 'wb') as f:
            #    pickle.dump(initial_data, f, pickle.HIGHEST_PROTOCOL)
            #    f.close()
            #    tryRegister = True
            #users[usersVars.userID] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status ## definicao de um login (username, password e status)

            print("Criacao de novas contas.\n")
        
            usersVars.username = input("Usuario: ") # definindo nome de usuario
            usersVars.password = input("Senha: ") # definindo a senha
            usersVars.balance = float(200.0)
            print("\n==============\n")
            usersVars.name_full = str(input("Nome Completo: "))
            usersVars.profession = str(input("Profissão: "))
            usersVars.monthly_income = float(input("Renda Mensal: "))
            usersVars.address = str(input("Endereco: "))
            print('\nEx.: +55 (##) #####-####')
            usersVars.phone_number = str(input("Numero de Telefone: "))
            usersVars.status = False
            usersVars.userID = len(users)

            ## Definicao da conta corrente do novo usuario ##
            usersVars.account = random.randint(10000, 99999)
            i=0
            for i in range(len(users)):
                if usersVars.account == users[i][2]:
                    print("ERRO!\n CONTA JA EXISTENTE")
                    exit()
                    break;
            ## Retornar o numer da conta corrente ##

            print(f"\nO numero da conta corrente do usuario eh \"{usersVars.account}\"")
            ##=======================##

            if os.path.exists('users.data'): ## verificando se o arquivo existe
               i = open('users.data','rb') ## lendo os bytes
               lmao = pickle.load(i)
            #else:
            #    login_out = open("clients.data", "wb")
            while usersVars.userID in users:
                usersVars.userID += 1
            users[usersVars.userID] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status ## definicao de um login (username, password e status)
        
            with open('users.data', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(users, f, pickle.HIGHEST_PROTOCOL)
            tryRegister = False
            inMenu = True


    while tryChangePassword:
        currentUser = 0
        usersVars.account = int(input('Numero da Conta: '))
        for i in range(len(users)):
            # Caso tenha muitos usuarios no users.data isso deve ajudar a indicar o que está havendo
            os.system('cls')
            print('Por favor, aguarde. . .') 
            #--------------------------------#
            if usersVars.account == users[i][2] and users[i][9] == False:
                print(f"\nSucesso!")
                usersVars.username = users[i][0]
                usersVars.password = users[i][1]
                usersVars.account = users[i][2]
                usersVars.balance = users[i][3]
                usersVars.name_full = users[i][4]
                usersVars.profession = users[i][5]
                usersVars.monthly_income = users[i][6]
                usersVars.address = users[i][7]
                usersVars.phone_number = users[i][8]
                usersVars.status = users[i][9]
                sleep(.3)
                break;
        usersVars.password = input('Insira nova senha: ')
        # Faz um update nos dados
        users[i] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status
        with open('users.data', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(users, f, pickle.HIGHEST_PROTOCOL)
        tryChangePassword = False
        inMenu = True


    while inMenu:
        os.system('cls')
        print("╔════════════════════════════════╗\n"
             +"║ O que deseja fazer?            ║\n"
             +"║                                ║\n"
             +"╠═ 0. Sair                       ║\n"
             +"╠═ 1. Cadastrar nova conta       ║\n"
             +"╠═ 2. Buscar conta corrente      ║\n"
             +"╠═ 3. Re-definir senha           ║\n"
             +"╠════════════════════════════════╝\n"
             +"║")
        enter = input('╚══Entrada: ')
        if (enter == '1'):
            tryRegister = True;
            inMenu = False;
        elif (enter == '2'):
            os.system('cls')
            search = input('Procurar: ')
            print('<ID>, <NOME>: <CONTA CORRENTE>\n')
            i=0
            for i in range(len(users)):
                if search.lower() in users[i][4].lower():
                    print(f"{i}, {users[i][4]}: {users[i][2]}")
            input('\nPressione \'ENTER\' para continuar. . .')
        elif (enter == '3'):
            tryChangePassword = True
            inMenu = False
        elif (enter == '0'):
            import main
        else:
            inMenu = True



           
# ╔╗═║
# ╠╣╦╬
# ╚╝╩╬

