#**ainda falta criar a função responsável por analisar as vitorias por diagonais**

#criando uma matriz que será a base para o jogo da velha
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

#definição da função responsavel por mostrar o corpo do jogo da velha
def corpo(matriz):
    for i in matriz:
        for j in i:
            if j == 0:
                print("| |", end="")
            elif j == 1:
                print("|X|", end="")
            else:
                print("|O|", end="")
        print()

#função responsável por registrar as jogadas dos jogadores
def jogada():
    OpcaoInvalida = False

    X = input("X - Insira as coordenadas da sua jogada: ").split()
    if ((0 <= int(X[0]) <=2 ) and (0 <= int(X[1]) <=2) and matriz[int(X[0])][int(X[1])] == 0):  #analisa se a coodenada esta dentro do index e se não está ocupada
        matriz[int(X[0])][int(X[1])] = 1
    else:
        print("Opção invalida, tente novamente.")
        OpcaoInvalida = True
        while OpcaoInvalida:
            X = input("X - Insira as coordenadas da sua jogada: ").split()
            if ((0 <= int(X[0]) <=2 ) and (0 <= int(X[1]) <=2) and matriz[int(X[0])][int(X[1])] == 0):
                matriz[int(X[0])][int(X[1])] = 1
                OpcaoInvalida = False
            else:
                print("Opção invalida, tente novamente.")


    O = input("O - Insira as coordenadas da sua jogada: ").split()
    if ((0 <= int(O[0]) <=2 ) and (0 <= int(O[1]) <=2) and matriz[int(O[0])][int(O[1])] == 0):
        matriz[int(O[0])][int(O[1])] = 2
    else:
        print("Opção invalida, tente novamente.")
        OpcaoInvalida = True
        while(OpcaoInvalida):
            O = input("O - Insira as coordenadas da sua jogada: ").split()
            if((0 <= int(O[0]) <=2 ) and (0 <= int(O[1]) <=2) and matriz[int(O[0])][int(O[1])] == 0):
                matriz[int(O[0])][int(O[1])] = 2
                OpcaoInvalida = False
        

def AnalisaLinha(matriz):
    global Player1Venceu, Player2Venceu
    Player1Venceu = False
    Player2Venceu = False
    for i in range(len(matriz)):
        if matriz[i][0] == 1 and matriz[i][1] == 1 and matriz[i][2]== 1:
            print("O jogador X venceu.")
            Player1Venceu = True
        elif matriz[i][0] == 2 and matriz[i][1] == 2 and matriz[i][2]== 2:
            print("O jogador O venceu.")
            Player2Venceu = True
        

#função resposável por registar as jogadas dos jogadores
print("-----------------------------------------\n\t      JOGO DA VELHA  \n-----------------------------------------")

"""player1 = int(input("Digite 1 para escolher \"X\" ou 2 para \"O\": "))
if player1 == 1:
    player2 = 2
else:
    player2 = 1

if player1 == 1:
    print("Jogador 1: X\nJogador 2: O")
else:
    print("Jogador 1: O\nJogadro 2: X")"""

continuar = True

while continuar:
    corpo(matriz)
    jogada()
    AnalisaLinha(matriz)
    if Player1Venceu or Player2Venceu:
        corpo(matriz)
        continuar = False






    
            