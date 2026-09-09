import random

ngerado = random.randrange(1, 10)

nescolhido = int(input("Escolha um número: "))

while(ngerado != nescolhido):
    if nescolhido < ngerado:
        nescolhido = int(input("Escolha errada. Tente um número maior: "))
    else:
        nescolhido = int(input("Escolha errada. Tente um número menor: "))

if ngerado == nescolhido:
        print(f"Parabéns, você acerto!. O número certo é {ngerado}")
