import random

def jogar():
    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")

    limite_de_erros = 7
    print("Dica: É uma fruta. Você só tem {} tentativas.\n".format(limite_de_erros))

    arquivo = open("frutas.txt", "r")
    #print(arquivo.read())

    frutas = []

    for linha in arquivo:
        frutas.append(linha.strip().upper())
    #print(frutas)
    aleatorio = random.randrange(0,len(frutas))
    print(aleatorio)

    palavra_secreta = frutas[aleatorio]
    #print(palavra_secreta)

    #print(len(frutas))
    arquivo.close()


    letras_acertadas = ["_" for underline in palavra_secreta]
    #print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input("Qual letra?: ")
        chute = chute.strip().upper()


        if (chute in palavra_secreta):
            #print("Você chutou {} que está ou não na palavra secreta {}.".format(chute,palavra_secreta))
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    #print("Encontrei a letra {} na posição {}.".format(chute,index))
                    letras_acertadas[index] = letra
                    print(letras_acertadas )
                index += 1
        else:
            erros += 1
            if(limite_de_erros - erros == 1):
                print("Você pode errar somente mais {} vez!\n".format(limite_de_erros - erros))
            elif(erros != limite_de_erros):
                    print("Você pode errar somente mais {} vezes!\n".format(limite_de_erros - erros))
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        if(enforcou):
            print("Você perdeu!")
        elif(acertou):
            print("Você acertou!")
        else:
            print("Jogando...")
    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()
