import os
import pickle
import usersVars
from time import sleep

# Booleans
# Se o cliente está dentro do painel de controle ou não
userCP = False
# Se o cliente está efetuando login ou não
tryLogin = True
# Se o cliente está Sacando ou não
tryWithdraw = False
# Se o cliente está Depositando ou não
tryDeposit = False
# Se o cliente esta Investindo ou não
tryInvest = False
# Loop para a tela do cliente
tryClient = True
# Deve sempre estar como True, vai dar um update nos dados a cada loop
updateData = True

# Integers
# Tentativas de login com falhas
failedAttempts = 0 
# Uma variavel feita para salvar o ID do cliente que entrou
currentUser = 0

# Integers
# usado para dar mais segurança ao cliente.
accountRemainder = str(usersVars.account)[:2]

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
    usersVars.account = int(input("Conta: "))
    usersVars.password = str(input("Senha: "))

    # Passando por todo o banco de dados a procura de um usuario que se encaixe
    for i in range(len(users)):
        # Caso tenha muitos usuarios no users.data isso deve ajudar a indicar o que está havendo
        os.system('cls')
        print('Por favor, aguarde. . .') 
        #--------------------------------#
        if usersVars.account == users[i][2] and usersVars.password == users[i][1] and users[i][9] == False:
            print(f"\nSucesso!")
            sleep(.3)
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
    accountRemainder = str(usersVars.account)[:2]
    def UpdateData():
        # Faz um update nos dados
        users[currentUser] = usersVars.username, usersVars.password, usersVars.account, usersVars.balance, usersVars.name_full, usersVars.profession, usersVars.monthly_income, usersVars.address, usersVars.phone_number, usersVars.status
        with open('users.data', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(users, f, pickle.HIGHEST_PROTOCOL)
    # 1- SAQUE
    while tryWithdraw:
        os.system('cls')

        if users[currentUser][3] > 0:
            withdraw = 0
            print('╔══════════════════════════════════\n'
                + '║\n'
                +f'╠═Conta: {accountRemainder}XXX\n'
                +f'╠═Saldo atual: {users[currentUser][3]}\n'
                + '║\n'
                + '║')
            withdraw = int(input('╠═Quanto deseja sacar? (Digite 0 para sair)\n╚ R$'))
            # Como isso é apenas uma simulação o saldo apenas é deletado
            if (withdraw <= 0):
                tryWithdraw = False
                userCP = True
            elif (withdraw > users[currentUser][3]):
                input('Erro!\nSaldo insuficiente.')
            else:
                usersVars.balance -= withdraw
                usersVars.balance = round(usersVars.balance, 2)
                UpdateData()
            break;
        else:
            input('Erro!\nSeu saldo eh invalido para realizar saques.')
    
    # 2- DEPOSITO
    while tryDeposit:
        os.system('cls')
        deposit = 0
        print('╔══════════════════════════════════\n'
            + '║\n'
            +f'╠═Conta: {accountRemainder}XXX\n'
            +f'╠═Saldo atual: {users[currentUser][3]}\n'
            + '║\n'
            + '║')
        deposit = int(input('╠═Quanto deseja depositar? (Digite 0 para sair)\n╚ R$'))
        if (deposit <= 0):
            tryDeposit = False
            userCP = True
        elif (deposit > 10000): #Limite para deposito
            input(f"\nErro!\nO valor {deposit}\neh muito alto para realizar depositos.")
            UpdateData()
            break;
        else:
            usersVars.balance += deposit
            usersVars.balance = round(usersVars.balance, 2)
            UpdateData()
        break;
    

    def Investment(initialInvest, percent, elapsedTime):
        return initialInvest * (1+(percent/100))**elapsedTime

    # 3 - Investir
    while tryInvest:
        os.system('cls')
        print('╔══════════════════════════════════\n'
            + '║\n'
            +f'╠═Conta: {accountRemainder}XXX\n'
            +f'╠═Saldo atual: {users[currentUser][3]}\n'
            + '║\n'
            + '║')
        clientInvest = float(input('╠═Aporte inicial: R$'))
        clientTime = int(input('╠═Tempo de investimento (Em meses): '))

        if clientInvest > users[currentUser][3]:
            print('ERRO!\n Aporte inicial invalido.')
            tryInvest = False
            UserCP = True
        

        if clientTime < 12:
            result = Investment(clientInvest, 0.5, clientTime) - clientInvest
        elif clientTime > 60:
            result = Investment(clientInvest, 1.0, clientTime) - clientInvest
        else:
            result = Investment(clientInvest, 0.7, clientTime) - clientInvest
        result = round(result, 2)
        
        print('║\n╚Seu lucro foi de: R$', result)
        usersVars.balance += result
        input()
        tryInvest = False
        userCP = True
        UpdateData()
        break

            

    
    ## USER CONTROL PANEL
    while userCP:
        UpdateData();
        enter = -1
        os.system('cls')
        print('╔════════════════════════════════════════\n'
            +f'╠═Bem vindo(a) de volta {users[currentUser][4]}!\n'
            + '╠═O que deseja fazer?\n'
            + '║\n'
            + '╠═  0. Sair\n'
            + '╠═  1. Saque\n'
            + '╠═  2. Deposito\n'
            + '╠═  3. Investir\n'
            + '╠═  4. Informacoes\n'
            + '╠════════════════════════════════════════')
        enter = str(input('║\n╚═ Entrada: '))
        if enter == '0':
            import main
        elif enter == '1' or enter == "saque":
            tryWithdraw = True
            userCP = False
        elif enter == '2' or enter == "deposito":
            tryDeposit = True
            userCP = False
        elif enter == '3' or enter == "investir":
            tryInvest = True
            userCP = False
        elif enter == '4' or enter == "info" or enter == "informacoes":
            os.system('cls')
            print('╔════════════════════════════\n'
                +f'╠═  INFORMACOES\n'
                +f'╠════════════════════════════\n'
                +f'╠═ Conta         : {users[currentUser][2]}\n'
                +f'╠═ Saldo         : {users[currentUser][3]}\n'
                +f'╠═ Profissao     : {users[currentUser][5]}\n'
                +f'╠═ Renda Mensal  : {users[currentUser][6]}\n'
                +f'╠═ Endereco      : {users[currentUser][7]}\n'
                +f'╠═ Numero de Tel.: {users[currentUser][8]}\n'
                +f'╠═ Cadastro      : Cliente\n'
                + '╠════════════════════════════\n'
                + '╠═ Precione \'ENTER\' para continuar. . .\n'
                + '╚════════════════════════════')
            input()
        else:
            print("Erro!\nEntrada Invalida.")

    
        