import tkinter as tk
import random

opcoes = ["pedra", "papel", "tesoura"]

placar_jogador = 0
placar_computador = 0
rodada = 0

def jogar(jogador):
    global placar_jogador, placar_computador, rodada

    computador = random.choice(opcoes)
    rodada += 1

    texto_jogadas.config(
        text=f"voce: {jogador} Computador: {computador}"
    )

    if jogador == computador:
        resultado.config(text="Empate!") 
    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "tesoura" and computador == "papel") or
        (jogador == "papel" and computador == "pedra")

    ):
        resultado.config(text="você venceu a rodada...")
        placar_jogador += 1

    else:
        resultado.config(text="computador venceu a rodada")
        placar_computador += 1

    placar.config(
        text=f"voce: {jogador} Computador: {computador}"
    )

    rodada_texto.config(text=f"rodada {rodada} de 3")

    if rodada == 3:
        if placar_jogador > placar_computador:
            resultado.config(text="voce ganho")
        elif placar_computador > placar_jogador:
            resultado.config(text="voce perdeu")
        else:
            resultado.config(text="empate")

        botao_pedra.config(state="disabled")
        botao_papel.config(state="disabled") 
        botao_tesoura.config(state="disabled")
        botao_novamente.pack(pady=10)

def reiniciar()
    global placar_jogador, placar_computador, rodada

    placar_jogador = 0
    placar_computador = 0
    rodada = 0

    placar.config(text="voce 0 x 0 computador")
    texto_jogadas.config(text="Faça sua escolha")
    resultado.config(text="")
    rodada_texto.config(text="Rodada 0 de 3")

    botao_pedra.config(state="normal")
    botao_papel.config(state="normal") 
    botao_tesoura.config(state="normal")
    botao_novamente.pack_forget()

janela = tk.Tk()
janela.title = ("pedra, papel e tesoura")
janela.geometry("400x400")

titulo = tk.Label(
    janela,
    text="PEDRA, PAPEL E TESOURA",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

texto_jogadas = tk.Label(
    janela,
    text="faça sua escolha",
    font=("Arial", 12)
)
texto_jogadas.pack(pady=10)

botao_pedra = tk.Button(
    janela,
    text="pedra",
    width=10, command=lambda: jogar("pedra")
)
botao_pedra.pack(pady=5)

botao_papel = tk.Button(
    janela,
    text="papel",
    width=10, command=lambda: jogar("papel")
)
botao_papel.pack(pady=5)

botao_tesoura = tk.Button(
    janela,
    text="tesoura",
    width=10, command=lambda: jogar("tesoura")
)
botao_tesoura.pack(pady=5)

placar = tk.Label(
    janela,
    text="voce 0 x 0 computador",
    font=("Arial", 12, "bold")
)
placar.pack(pady=15)

resultado = tk.Label(
    janela, text="", font=("Arial", 11)
)