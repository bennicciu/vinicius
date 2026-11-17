import tkinter as tk
import random

#info player

jogador = {
    "nome": "Jerivaldo",
    "hp": 100,
    "atk": 20,
    "xp": 0
}

#info ini

gob = {
    "nome": "Gobling",
    "hp": 50,
    "atk": 15,
    "xp": 5
}

orc = {
    "nome": "Orc",
    "hp": 65,
    "atk": 20,
    "xp": 10
}


def cmc():
    global botao_fugir, botao_atacar, texto_mensagem, monstro

    botao_cmc.destroy()

    monstro = random.choice([gob, orc]).copy()

    texto_mensagem = tk.Label(janela, text=f"Um {monstro['nome']} apareceu", font=("Arial", 11))
    texto_mensagem.pack(pady=20)

    botao_atacar = tk.Button(janela, text="atacar", command=atacar)

    botao_atacar.pack(pady=5)

    botao_fugir = tk.Button(janela, text="fugir", command=fugir)
    botao_fugir.pack(pady=5)

    atualizar()

def atualizar():
    texto_jogador.config(text=f"hp de {jogador['nome']}: {jogador['hp']}")

    texto_monstro.config(text=f"hp de {monstro['nome']}: {monstro['hp']}")

    texto_xp.config(text=f"XP:{jogador['xp']}/30")

    
def atacar():
    if jogador["hp"] <= 0 or monstro["hp"] <= 0:
        return
    atk = random.randint(5, jogador["atk"])
    monstro["hp"] -= atk

    mensagem = f"você causou {atk} de dano"

    if monstro["hp"] > 0:

        atk_monstro = random.randint(1, monstro["atk"])
        jogador["hp"] -= atk_monstro

        mensagem += f"\nO {monstro['nome']} causou {atk_monstro} de dano!"

    if jogador["hp"] <= 0:
        mensagem = "perdeu"

    elif monstro["hp"] <= 0:
        mensagem = f"você ganhou {monstro['xp']} de xp"
        jogador["xp"] = jogador["xp"] + monstro["xp"]
        cmc()

        

    if jogador["hp"] <= 0 or monstro["hp"] <= 0:
        botao_atacar.config(state="disabled")
        botao_fugir.config(state="disabled")

    texto_mensagem.config(text=mensagem)

    atualizar()

def fugir():

    texto_mensagem.config(text="fugiu vagabundo")
    botao_atacar.config(state="disabled")
    botao_fugir.config(state="disabled")

janela = tk.Tk()
janela.title("meu rpg")
janela.geometry("350x350")

titulo = tk.Label(
    janela, text="batalha rpg", font=("", 20)
)
titulo.pack(pady=15)

botao_cmc = tk.Button(janela, text="Jogar", command=cmc)
botao_cmc.pack(pady=10)

texto_jogador = tk.Label(janela)
texto_jogador.pack(pady=10)  

texto_monstro = tk.Label(janela)
texto_monstro.pack(pady=10) 

texto_xp = tk.Label(janela)
texto_xp.pack(pady=5)


janela.mainloop()
