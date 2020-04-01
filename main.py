###########################
## INTERFACE DO FADEABNK ##
###########################
#    Aqui é onde o seu    #
#     dinheiro "fade"     #
###########################

# O marketing da empresa foi demitido depois de 2 meses...
import os
import random
inMenu = True

while inMenu:
    os.system('cls')
    print("Olá, o que gostaria de fazer no FadeBank?\nEntrar como:\n")
    print("1. Cliente")
    print("2. Gerente\n\n")
    choice = input("Entrada: ")
    if choice == str("1") or choice.lower() == "cliente":
        inMenu = False
        import Client
        inMenu = False
    elif choice == str("2") or choice.lower() == "gerente":
        inMenu = False
        import gerente
    else:   
        input("Erro!\nEntrada invalida.")
        inMenu = True

