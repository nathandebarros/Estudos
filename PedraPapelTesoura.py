import random

pc = random.randrange(1,3)

continuar = True

def corpo():
    print(f"------------------------------------------\n\tPedra Papel ou tesoura\n------------------------------------------")
    print(f"Digite \"1\" para selecionar Pedra ")
    print(f"Digite \"2\" para selecionar Tesoura")
    print(f"Digite \"3\" para selecionar Papel")
    escolha = int(input("Isira a sua escolha: "))
    print(f"{pc}")



while continuar:
    corpo()