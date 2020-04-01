import pickle
import random
import os
import usersVars

initial_data = {0:('', '', '', 0.0, '', '', 0.0, '', '', 0)}
userVerification = False
passVerification = False
statusVerification = False
tryLogin = True
tryRegister = False
inMenu = False
tryGerente = True

while tryGerente:
    if os.path.exists('users.data'): ## verificando se o arquivo existe
        with open('users.data', 'rb') as f:
            users = pickle.load(f)
    users[usersVars.userID] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status ## definicao de um login (username, password e status)
    


    ## LOGIN ##    
    while tryLogin:
        if os.path.exists('users.data'): ## verificando se o arquivo existe
            with open('users.data', 'rb') as f:
                users = pickle.load(f)
        users[usersVars.userID] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status ## definicao de um login (username, password e status)
    
    
        userVerification = False
        passVerification = False
        statusVerification = False
        os.system('cls')
        print("Por favor realize o seu login para que possamos continuar...\n")
        usersVars.username = str(input("Usuario: "))
        usersVars.password = str(input("Senha: "))

        for i in range(len(users)):
            if usersVars.username == users[i][0]:
                userVerification = True
                if usersVars.password == users[i][1]:
                    passVerification = True
                    if users[i][9] == 1:
                        statusVerification = True
                        if userVerification == True and passVerification == True and statusVerification == True:
                            input(f"\nSucesso!")
                            tryLogin = False
                            inMenu = True

                        else:
                            #users.close()
                            input("\nErro!\nErro desconhecido.")
                            tryLogin = True
                    else:
                        input("\nErro!\nVoce não é um gerente, por favor use o painel do Cliente.")
                        tryLogin = True
                        import main
                else:
                    print("Validando Senha...")




## Username data ##
#username_data = {1:criarGerente.username}
#dataUser_out = open("gerente.username", "wb")
#pickle.dump(username_data, dataUser_out)

## Passwrod data ##
#password_data = {1:criarGerente.password}
#dataPass_out = open("gerente.password", "wb")
#pickle.dump(password_data, dataPass_out)


    if tryRegister:
        os.system('cls') # Limpar tela
        if os.path.exists('users.data'): ## verificando se o arquivo existe
            with open('users.data', 'rb') as f:
                users = pickle.load(f)
            with open('users.data', 'wb') as f:
                pickle.dump(initial_data, f, pickle.HIGHEST_PROTOCOL)
                f.close()
                tryRegister = True
            users[usersVars.userID] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status ## definicao de um login (username, password e status)

            print("Criacao de novas contas.\n") 
        
            usersVars.username = input("Usuario: ") # definindo nome de usuario
            usersVars.password = input("Senha: ") # definindo a senha
            usersVars.balance = float(200.0)
            print("==============")
            usersVars.name_full = str(input("Nome Completo: "))
            usersVars.profession = str(input("Profissão: "))
            usersVars.monthly_income = float(input("Renda Mensal: "))
            usersVars.address = str(input("Endereco: "))
            usersVars.phone_number = str(input("Numero de Telefone: "))
            usersVars.status = int(0)
            usersVars.userID = int(1)

            ## Definicao da conta corrente do novo usuario ##
            accountI = random.randint(100000, 999999)
            accountF = random.randint(1, 9)
            usersVars.account = f"{str(accountI)}-{str(accountF)}"
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

    while inMenu:
        os.system('cls')
        print("O que deseja fazer?\n")
        print("1. Cadastrar nova conta")
        print("2. Buscar conta corrente")
        print("3. Re-definir senha")
        enter = input('\nEntrada: ')