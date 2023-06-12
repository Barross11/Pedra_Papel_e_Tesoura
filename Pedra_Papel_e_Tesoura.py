from time import sleep
from random import choice
from os import system
from sys import exit

def quer_continuar():
    resposta = input("[!] Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
    if resposta == "sair":
        print("[!] Foi um prazer jogar com você!")
        exit()
    else:
        system("clear")

def checar_vitoria(pontos_jogador, pontos_maquina):
    vencedor = None
    if pontos_jogador == 10:
        vencedor = "JOGADOR"
    if pontos_maquina == 10:
        vencedor = "COMPUTADOR"
    if vencedor != None:
        print(f"[~] A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
        print(f"[+] O {vencedor} é o GRANDE VENCEDOR!!!!!!")
        exit()
    else:
        quer_continuar()

def main():
    print("** Vamos jogar Pedra, Papel ou Tesoura :D **")
    print("--!-- Ganha quem alcançar 10 pontos primeiro ou pedir pra sair. QUE VENÇA O MELHOR --!--")
    opcoes = ["pedra", "papel", "tesoura"]
    parar = ""
    ponto_maquina = 0
    ponto_jogador = 0
    while parar != "sair":
        escolha = ""
        print(f"A pontuação atual é {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
        while escolha not in opcoes:
            escolha = input("[+] Você vai escolher Pedra, Papel ou Tesoura? ").lower()
            if escolha not in opcoes:
                print("[!] Você precisa colocar uma opção válida")
        print("[!] Vou fazer uma escolha *BIP* *BOP*....")
        sleep(1.5)
        escolha_maquina = choice(opcoes)

        # ----  ---- Condições de EMPATE ----  ---- 
        if escolha_maquina == escolha:
            print("[!] Escolhemos a mesma coisa")
            print("[~] Essa rodada foi empate")
            ponto_maquina += 1
            ponto_jogador += 1
            checar_vitoria(ponto_jogador, ponto_maquina)

        #  ----  ---- Condições de Vitória de Jogador ----  ---- 
        elif escolha == "tesoura" and escolha_maquina == "papel":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você ganhou essa rodada")
            ponto_jogador += 1
            checar_vitoria()
        elif escolha == "papel" and escolha_maquina == "pedra":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você ganhou essa rodada")
            ponto_jogador += 1
            checar_vitoria(ponto_jogador, ponto_maquina)
        elif escolha == "pedra" and escolha_maquina == "tesoura":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você ganhou essa rodada")
            ponto_jogador += 1
            checar_vitoria(ponto_jogador, ponto_maquina)

        #  ----  ---- Condições de Derrota do Jogador ----  ---- 
        elif escolha_maquina == "tesoura" and escolha == "papel":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você perdeu essa rodada")
            ponto_maquina += 1
            checar_vitoria(ponto_jogador, ponto_maquina)
        elif escolha_maquina == "papel" and escolha == "pedra":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você perdeu essa rodada!")
            ponto_maquina += 1
            checar_vitoria(ponto_jogador, ponto_maquina)
        elif escolha_maquina == "pedra" and escolha == "tesoura":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você perdeu essa rodada")
            ponto_maquina += 1
            checar_vitoria(ponto_jogador, ponto_maquina)
        else:
            print("[!] Algo deu errado!")
            break

if __name__ == "__main__":
    main()
