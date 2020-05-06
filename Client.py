import os
import pickle
import usersVars
from time import sleep

# Booleans
# Se o cliente está dentro do painel de controle ou não
userCP = False
# Se o cliente está efetuando login ou não
tryLogin = True
# Se o cliente está sacando ou não
trySaque = False
# Se o cliente está Depositando ou não
tryDeposit = False
# Loop para a tela do cliente
tryClient = True
# Deve sempre estar como True, vai dar um update nos dados a cada loop
updateData = True

# Integers
# Tentativas de login com falhas
failedAttempts = 0 
# Uma variavel feita para salvar o ID do cliente que entrou
currentUser = 0

#--------------#
def SetData():
    usersVars.username = users[currentUser][0]
    usersVars.password = users[currentUser][1]
    usersVars.account = users[currentUser][2]
    usersVars.balance = users[currentUser][3]
    usersVars.name_full = users[currentUser][4]
    usersVars.profession = users[currentUser][5]
    usersVars.monthly_income = users[currentUser][6]
    usersVars.address = users[currentUser][7]
    usersVars.phone_number = users[currentUser][8]
    usersVars.status = users[currentUser][9]
#--------------#



## LOGIN ##    
while tryLogin:
    if os.path.exists('users.data'): ## verificando se o arquivo existe
        with open('users.data', 'rb') as f:
            users = pickle.load(f)
    else:
        # O numero 301 foi usado para ajudar a encontrar os erros dentro do código
        print("\nErro#301")
    
    os.system('cls')
    # Entradas de Login/Senha do cliente
    print("Por favor realize o seu login para que possamos continuar...\n")
    usersVars.username = str(input("Usuario: "))
    usersVars.password = str(input("Senha: "))

    # Passando por todo o banco de dados a procura de um usuario que se encaixe
    for i in range(len(users)):
        # Caso tenha muitos usuarios no users.data isso deve ajudar a indicar o que está havendo
        os.system('cls')
        print('Por favor, aguarde. . .') 
        #--------------------------------#
        if usersVars.username == users[i][0] and usersVars.password == users[i][1] and users[i][9] == False:
            print(f"\nSucesso!")
            time.sleep(.3)
            tryLogin = False
            tryClient = True
            userCP = True
            currentUser = i
            SetData()
            break;
    # Caso não seja possivel encontrar o usuario, isso aparecerá
    else:
        failedAttempts+=1;
        if (failedAttempts > 2):
            # Se isto fosse um sistema real, acho que colocar um sistema de tentativas erradas
            # seria uma boa ideia, afinal, não queremos ninguem se aproveitando do nosso servidor.
            # É claro que precisariamos de um cooldown, mas aqui acho que só isto ja basta...
            input("\nForam executadas muitas tentativas erradas")
            tryLogin = False
            import main
        input("\nErro!\nUsuario invalido.")
        tryLogin = True




while tryClient:
    # 1- SAQUE
    while trySaque:
        os.system('cls')
        if users[currentUser][3] > 0:
            print(f'Saldo atual: {users[currentUser][3]}')
            saque = int(input('\n\nQuanto deseja sacar? (Digite 0 para sair)\n'))
            # Como isso é apenas uma simulação o saldo apenas é deletado
            if (saque <= 0):
                trySaque = False
                userCP = True
            else:
                #users[currentUser][3] -= saque ## tupla != int
                usersVars.balance -= saque
            break;
        else:
            input('Erro!\nSeu saldo eh invalido para realizar saques.')
    
    while tryDeposit:
        deposit = 0
        os.system('cls')
    
        # Não foi declarado nenhum limite para a execução do saque
        print(f'Saldo atual: {users[currentUser][3]}')
        depoist = input('\n\nQuanto deseja depositar? (Digite 0 para sair)\n')
        if (deposit <= 0):
            tryDeposit = False
            userCP = True
        else:
            users[currentUser][3] += deposit
    
    
    
    
    
    
    ## USER CONTROL PANEL
    while userCP:
        enter = -1
        os.system('cls')
        print(f"Bem vindo {users[currentUser][4]}!\nO que deseja fazer?\n")

        # Deixei com varios prints, fica mais facil a visualização nesse caso
        print("0. Sair")
        print("1. Saque")
        print("2. Deposito")
        print("3. Verificar Saldo")
        print("4. Investir")
        print("5. Informacoes")
        enter = str(input("\nEntrada: "))
        if enter == '0':
            import main
        elif enter == '1' or enter == "saque":
            trySaque = True
            userCP = False
        #elif enter == 2 or enter == "deposito":
        #elif enter == 3 or enter == "verificar saldo":
        #elif enter == 4 or enter == "investir":
        #elif enter == 5 or enter == "info" or enter == "informacoes":
        else:
            print("Erro!\nEntrada Invalida.")

    while updateData:
        # Faz um update nos dados
        users[currentUser] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status
        with open('users.data', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(users, f, pickle.HIGHEST_PROTOCOL)
        break;
        
            