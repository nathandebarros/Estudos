#criando uma matriz que será a base para o jogo da velha
matriz = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

#definição da função responsavel por mostrar o corpo do jogo da velha
def corpo(matriz):
    print(f"{matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}")
    print(f"{matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]}")
    print(f"{matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}")

#função resposável por registar as jogadas dos jogadores
def jogada():
    X = input("Digite as coordenadas: ").split()
    matriz[int(X[0])][int(X[1])] = "X"
    O = input("Digite as coordenadas: ").split()
    matriz[int(X[0])][int(X[1])] = "O"


def ganhou(matriz):
    for i in range(len(matriz)):
        for c in range(len(matriz)):
            if matriz[i][c] == matriz[i+1][c+1] == matriz[i+2][c+2]:
                print(f"Parabéns! O {matriz[i][c]} Ganhou.")
            elif matriz[i][c] == matriz[i+1][c] == matriz[i+2][c]:
                print(f"Parabéns! O {matriz[i][c]} ganhou")