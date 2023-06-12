import random
import time 
import os

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
        time.sleep(3)
        escolha_maquina = random.choice(opcoes)

        # ----  ---- Condições de EMPATE ----  ---- 
        if escolha_maquina == escolha:
            print("[!] Escolhemos a mesma coisa")
            print("[~] Essa rodada foi empate")
            parar = input("<Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
            ponto_maquina+=1
            ponto_jogador+=1
            if parar != "sair":
                os.system("clear")   
            elif parar == "sair":
                print("[!] Foi um prazer jogar com você") 
                break   
            if ponto_jogador == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("O JOGADOR é o GRANDE VENCEDOR !!!!!!")
                break
            if ponto_maquina == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("A MÁQUINA é a GRANDE VENCEDORA !!!!!!") 
                break           		              
                
        #  ----  ---- Condições de Vitória de Jogador ----  ---- 
        elif escolha == "tesoura" and escolha_maquina == "papel":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você ganhou essa rodada")
            parar = input("<Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
            ponto_jogador +=1
            if parar != "sair":
                os.system("clear") 
            elif parar == "sair":
                print("[!] Foi um prazer jogar com você") 
                break   
            if ponto_jogador == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("O JOGADOR é o GRANDE VENCEDOR !!!!!!")
                break
            if ponto_maquina == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("A MÁQUINA é a GRANDE VENCEDORA !!!!!!") 
                break           		              
        elif escolha == "papel" and escolha_maquina == "pedra":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você ganhou essa rodada")
            parar = input("<Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
            ponto_jogador +=1
            if parar != "sair":
                os.system("clear")  
            elif parar == "sair":
                print("[!] Foi um prazer jogar com você") 
                break  
            if ponto_jogador == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("O JOGADOR é o GRANDE VENCEDOR !!!!!!")
                break
            if ponto_maquina == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("A MÁQUINA é a GRANDE VENCEDORA !!!!!!") 
                break          		                     
        elif escolha == "pedra" and escolha_maquina == "tesoura":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você ganhou essa rodada")
            parar = input("<Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
            ponto_jogador +=1
            if parar != "sair":
                os.system("clear") 
            elif parar == "sair":
                print("[!] Foi um prazer jogar com você") 
                break    
            if ponto_jogador == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("O JOGADOR é o GRANDE VENCEDOR !!!!!!")
                break
            if ponto_maquina == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("A MÁQUINA é a GRANDE VENCEDORA !!!!!!") 
                break           		             
                
        #  ----  ---- Condições de Derrota do Jogador ----  ---- 
        elif escolha_maquina == "tesoura" and escolha == "papel":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você perdeu essa rodada")
            parar = input("<Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
            ponto_maquina +=1
            if parar != "sair":
                os.system("clear") 
            elif parar == "sair":
                print("[!] Foi um prazer jogar com você") 
                break 
            if ponto_jogador == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("O JOGADOR é o GRANDE VENCEDOR !!!!!!")
                break
            if ponto_maquina == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("A MÁQUINA é a GRANDE VENCEDORA !!!!!!") 
                break     
        elif escolha_maquina == "papel" and escolha == "pedra":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você perdeu essa rodada")
            parar = input("<Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
            ponto_maquina +=1
            if parar != "sair":
                os.system("clear") 
            elif parar == "sair":
                print("[!] Foi um prazer jogar com você") 
                break 
            if ponto_jogador == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("O JOGADOR é o GRANDE VENCEDOR !!!!!!")
                break
            if ponto_maquina == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("A MÁQUINA é a GRANDE VENCEDORA !!!!!!") 
                break       
        elif escolha_maquina == "pedra" and escolha == "tesoura":
            print(f"[!] Eu escolhi {escolha_maquina} e você {escolha}")
            print("[~] Você perdeu essa rodada")
            parar = input("<Pressione ENTER para permanecer jogando ou digite SAIR para parar de jogar> ").lower()
            ponto_maquina +=1
            if parar != "sair":
                os.system("clear") 
            elif parar == "sair":
                print("[!] Foi um prazer jogar com você") 
                break 
            if ponto_jogador == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("O JOGADOR é o GRANDE VENCEDOR !!!!!!")
                break
            if ponto_maquina == 10:
                print(f"A pontuação final foi {ponto_jogador} PONTOS jogador e {ponto_maquina} PONTOS maquina")
                print("A MÁQUINA é a GRANDE VENCEDORA !!!!!!") 
                break                                                  
        else:
            print("[!] Algo deu errado")
            break

if __name__ == "__main__":
    main()
