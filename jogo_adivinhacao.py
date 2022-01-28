import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    #Variáveis
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 100
        
    #Pergunta ao usuário qual o nível de dificuldade ele deseja, dependendo da opção ganha mais vidas
    print("Qual o nível de dificuldade?")
    print("(1) Fácil / (2) Médio / (3)Difícil")

    #Guarda a opção do usuário
    nivel = int(input("Selecione uma opção: "))

    #Define o número de tentativas do usuário conforme sua opção
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #Controle de repetição do número de tentativas
    for rodada in range(1, total_de_tentativas + 1):
        
        #Mostrando ao usuário o total de tentativas
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        #Pegando o input do usuário
        chute_str = input("Digite um número entre 1 e 100: ")
        
        #Convertendo o input do usuário para o tipo int
        chute = int(chute_str)

        #Verifica se o chute do usuário está certo como solicitado
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            #Faz com que saia dessa interação
            continue
        
        print("Você digitou: ", chute_str)

        #Definindo novas variáveis e atribuindo o valor do chute do usuário para ficar mais legível o código
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        #Caso o chute do usuário esteja correto, printa acertou e encerra o jogo.
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            #Força a saída do laço
            break
        
        #Dando dicas para o usuário se o chute está maior ou menor do que o número secreto
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto")
                #Subtrai os pontos do usuário ao errar a tentativa
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

            
    print("Fim do jogo!")   

if(__name__ == "__main__"):
    jogar()