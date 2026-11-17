import random

opcoes = ["pedra", "papel", "tesoura"]
while True:
    print("\n=== PEDRA, PAPEL E TESOURA ===")

    placar_jogador = 0
    placar_computador = 0


    for rodada in range(1, 4):
        print(f"\n--- Rodada {rodada} ---")

        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if jogador not in opcoes:
            print("Escolha inválida!")
            continue

        computador = random.choice(opcoes)

        print(f"Você escolheu: {jogador}")
        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate!")
        elif (
            (jogador == "pedra" and computador == "tesoura") or
            (jogador == "tesoura" and computador == "papel") or
            (jogador == "papel" and computador == "pedra")

        ):
            print("você venceu a rodada...")
            placar_jogador += 1

        else:
            print("computador venceu a rodada")
            placar_computador += 1

        print(f"placar: tu {placar_jogador} x maquina {placar_computador}")

    print("\n === fim do jogo, seu lixo === n/")

    if placar_jogador > placar_computador:
        print("eba, se ganho...")
    elif placar_jogador < placar_computador:
        print("SEU LIXO, EU GANHEI")
    else:
        print("empate...")

    jogar_novamente = input("\nvem x1 dnv pó? (sim/não)").lower()

    if jogar_novamente != "sim":
        print("vai correr ent? covarde")
        break
        
        # ahdcducjj