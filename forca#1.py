def jogar():
    print("*****************************************")
    print("------ BEM VINDO AO JOGO DA FORCA ------")
    print("*****************************************")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra??")
        index = 1
        for letra in palavra_secreta:
            if(chute.lower() == letra):
                print("Encontrei a letra {} na posicao {}".format(letra, index))
            index = index + 1

        print ("jogando...")

    print("FIM DO JOGO :(")

if (__name__ == "__main__"):
    jogar()


