import random



continuar = True

def corpo():
    print(f"------------------------------------------\n\tPedra Papel ou tesoura\n------------------------------------------")
    print(f"Digite \"1\" para selecionar Pedra ")
    print(f"Digite \"2\" para selecionar Tesoura")
    print(f"Digite \"3\" para selecionar Papel")
    global escolha 
    global pc
    pc = random.randrange(1,4)
    escolha = int(input("Insira a sua escolha: "))


def jogo():
    print("------------------------------------------")
    print("RESULTADO: ", end="")
    if escolha == pc:
        print(f"Empate.")
    else:
        match escolha:
            case 1:
                if pc == 2:
                    print(f"Parbéns, você ganhou!. O adversário escolheu Tesoura")
                else:
                    print(f"Você perdeu. O adversário escolheu Papel")
            case 2:
                if pc == 1:
                    print(f"Você perdeu. O adversário escolheu Pedra")
                else: 
                    print(f"Parabéns, você ganhou! O adversário escolheu Papel")
            case 3:
                if pc == 1:
                    print(f"Parabéns, você ganhou! O adversário escolheu Pedra")
                else:
                    print(f"Você perdeu. O adversário escolheu Tesoura")
            case _: 
                    print("Error. \nPorfavor insira um valor válido.")
    print("------------------------------------------")

while continuar:
    corpo()
    jogo()
    opcao = int(input("Quer continuar?\nInsira \"1\" para 'Sim' e \"0\" para 'Não': "))
    if opcao == 0:
        continuar = False