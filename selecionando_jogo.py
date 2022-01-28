import jogo_forca
import jogo_adivinhacao

print("********************")
print("* Escolha um jogo! *")
print("********************")

print("(1) Forca / (2) Adivinhação")

#Cria a variavel "jogo" e guarda a opção
jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando forca")
    jogo_forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    jogo_adivinhacao.jogar()
