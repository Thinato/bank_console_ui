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
from time import sleep

# Variaveis com valores iniciais
# Para que tenha um loop no menu
inMenu = True 
# A opção que o usuario vai escolher dentro da entrada
choice = 0 


while inMenu: # Inicio do menu
    os.system('cls') # Limpar a tela
    # ╔╗═║
    # ╠╣╦╬
    # ╚╝╩╬
    # Textos para o usuario
    print("╔══════════════════════════════════════════╗\n"
        + "║Olá, o que gostaria de fazer no FadeBank? ║\n"
        + "║Entrar como:                              ║\n"
        + "║                                          ║\n"
        + "║   1. Cliente                             ║\n"
        + "║   2. Gerente                             ║\n"
        + "║                                          ║\n"
        + "║        Digite \"sair\" pa1ra sair.         ║\n"
        + "╠══════════════════════════════════════════╝\n"
        + "║")

    # input da entrada do usuario, recebe um numero ou o nome da opção
    choice = input("╚═ Entrada: ")
    if choice == "1" or choice.lower() == "cliente":
        # Encerra o loop do Menu
        inMenu = False
        # Vai para o cliente
        import Client
    elif choice == "2" or choice.lower() == "gerente":
        inMenu = False
        import admin
        # Opção somente feita por texto para a saida do usuario.
    elif choice.lower() == "sair" or choice.lower() == "fechar" or choice == "0":
        sys.exit('Finalizando sessao. . .')
        # Em caso de qualquer input invalida, isso sera dado como output.
    else:
        ## Estamos usando o input para que o usuario tenha tempo de ler e reagir
        print("Erro!\nEntrada invalida.") 
        sleep(.3)
        inMenu = True

