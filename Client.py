import os
import main
import pickle
import usersVars

userVerification = False
passVerification = False
statusVerification = False
userCP = False
tryLogin = True

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
                if userVerification == True and passVerification == True:
                    input(f"\nSucesso!")
                    tryLogin = False
                    userCP = True

                else:
                    #users.close()
                    input("\nErro!\nErro desconhecido.")
                    tryLogin = True
            else:
                print("Validando Senha...")
    #else:
    #    input("Erro!\nUsuario invalido. (for#1)")
    #    tryLogin = True
#else:
#    input('Erro!\nUsuario invalido.(if#1)')
#    tryLogin = True
    



    '''with open("users.data", "rb") as new_login:
        login_list = pickle.load(new_login)
        for i in login_list:
            if username in [i][0]:
                userVerification = True
                if password in [i][0]:
                    passVerification = True
                    #Status = login_list[i]
                else:
                    input("\nErro!\nSenha invalida.")
                    Login()
            else:
                input("\nErro!\nUsuario invalido.")
                Login()'''


## +55 19 99327-8829 (whatsapp)
    ## USER CONTROL PANEL
if userCP:
    enter = -1
    os.system('cls')
    print(f"Bem vindo de volta!\nO que deseja fazer?\n")
    print("0. Sair")
    print("1. Saque")
    print("2. Deposito")
    print("3. Verificar Saldo")
    #if Status == "investidor":
    #    print("4. Investir")
    print("4. Investir")
    enter = input("\nEntrada: ")
    if enter == 0:
        import main
    elif enter == 1:
        UserSaque()
    #elif enter == 2:
    #elif enter == 3:
    #elif enter == 4:
    else:
        print("Erro!\nEntrada Invalida.")
        


#def Start():
#    tryLogin = True