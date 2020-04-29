###########################
## INTERFACE DO FADEABNK ##
###########################
#    Aqui é onde o seu    #
#     dinheiro "fade"     #
###########################

# O marketing da empresa foi demitido depois de 2 meses...
import os
import random
import sys

# Variaveis com valores iniciais
inMenu = True # Para que tenha um loop no menu
choice = 0 # A opção que o usuario vai escolher dentro da entrada


while inMenu: # Inicio do menu
    os.system('cls') # Limpar a tela

    # Textos para o usuario
    print("Olá, o que gostaria de fazer no FadeBank?\nEntrar como:\n")
    print("1. Cliente")
    print("2. Gerente\n"+"Digite \"sair\" pa1ra sair.\n\n")

    # input da entrada do usuario, recebe um numero ou o nome da opção
    choice = input("Entrada: ")
    if choice == str("1") or choice.lower() == "cliente":
        # Encerra o loop do Menu
        inMenu = False
        # Vai para o cliente
        import Client
    elif choice == str("2") or choice.lower() == "gerente":
        inMenu = False
        import admin
        # Opção somente feita por texto para a saida do usuario.
    elif choice.lower() == "sair" or choice.lower() == "fechar":
        sys.exit('Finalizando processo. . .')
        # Em caso de qualquer input invalida, isso sera dado como output.
    else:
        ## Estamos usando o input para que o usuario tenha tempo de ler e reagir
        input("Erro!\nEntrada invalida.") 
        inMenu = True

