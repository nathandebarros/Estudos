#criando uma matriz que será a base para o jogo da velha
matriz = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

#definição da função responsavel por mostrar o corpo do jogo da velha
def corpo(matriz):
    print(f"{matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}")
    print(f"{matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}")
    print(f"{matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}")

corpo(matriz)