import tkinter as tk
import random

#info player

jogador = {
    "nome": "Jerivaldo",
    "hp": 100,
    "atk": 20
}

#info ini

ini = {
    "nome": "Gobling",
    "hp": 50,
    "atk": 15
}

def atualizar():
    texto_jogador.config(text=f"hp de {jogador['nome']}: {jogador['hp']}")

    texto_ini.config(text=f"hp de {ini['nome']}: {ini['hp']}")


def atacar():
    if jogador["hp"] <= 0 or ini["hp"] <= 0:
        return
    atk = random.randint(5, jogador["atk"])
    ini["hp"] -= atk

    mensagem = f"você causou {atk} de dano"

    if ini["hp"] > 0:

        atk_ini = random.randint(1, ini["atk"])
        jogador["hp"] -= atk_ini

        mensagem += f"\nO monstro causou {atk_ini} de dano!"

    if jogador["hp"] <= 0:
        mensagem = "perdeu"

    elif ini["hp"] <= 0:
        mensagem = "ganhou"

    texto_mensagem.config(text=mensagem)

    atualizar()

def fugir():

    texto_mensagem.config(text="fugiu vagabundo")

janela = tk.Tk()
janela.title("meu rpg")
janela.geometry("350x350")

titulo = tk.Label(
    janela, text="batalha rpg", font=("", 20)
)
titulo.pack(pady=15)

texto_jogador = tk.Label(janela)
texto_jogador.pack(pady=10)  

texto_ini = tk.Label(janela)
texto_ini.pack(pady=10) 

texto_mensagem = tk.Label(janela, text="Um goblng apareceu", font=("Arial", 11))
texto_mensagem.pack(pady=20)

botao_atacar = tk.Button(janela, text="atacar", command=atacar)

botao_atacar.pack(pady=5)

botao_fugir = tk.Button(janela, text="fugir", command=fugir)
botao_fugir.pack(pady=5)

atualizar()

janela.mainloop()
