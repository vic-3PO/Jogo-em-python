print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 76
total_Tentativas = 3
rodadas = 1

while(rodadas <= total_Tentativas):
    print("Tentativa {} de {}".format(rodadas, total_Tentativas))

    chute_str = input("Digite um número: ")

    chute = int(chute_str)

    print("Você digitou ",chute)

    acertou = chute == numero_secreto;
    maior   = chute > numero_secreto;
    menor   = chute < numero_secreto;

    if(acertou):
        print( "Você acertou!")
    else:
        if(maior):
            print("Vocé errou! O seu chute foi maior do que a número secreto.")
        elif(menor):
            print("Vocé errou! O Seu chute foi menor do que a número secreto.")
    
    rodadas += 1

print("Fim do Jogo!")

