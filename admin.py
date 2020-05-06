import pickle
import random
import os
import usersVars
import json
import time


## Variaveis com dados iniciais.
initial_data = {0:('', '', '', 0.0, '', '', 0.0, '', '', False)}
initial_admin = {0:('BzJT2Y5', 'KoEXfKoUyfH', '000000-0', 0.0, '', '', 0.0, '', '', True)}
userVerification = False
passVerification = False
statusVerification = False
tryLogin = True
tryRegister = False
inMenu = False
tryGerente = True
# Tentativas de login com falhas
failedAttempts = 0 


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
            if execute.lower() == "admin" or execute == "1":
                pickle.dump(initial_admin, lmao, pickle.HIGHEST_PROTOCOL)
                exit()
            else:
                pickle.dump(initial_data, lmao, pickle.HIGHEST_PROTOCOL)
                exit()


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
                time.sleep(.3)
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
            accountI = random.randint(100000, 999999)
            accountF = random.randint(1, 9)
            usersVars.account = f"{str(accountI)}-{str(accountF)}"
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
            InMenu = True

    while inMenu:
        os.system('cls')
        print("O que deseja fazer?\n")
        print("1. Cadastrar nova conta")
        print("2. Buscar conta corrente")
        print("3. Re-definir senha")
        enter = input('\nEntrada: ')
        if (enter == '1'):
            tryRegister = True;
            inMenu = False;
        elif (enter == '2'):
            print(users)
            print('\nWIP')
        else:
            print('WIP')