import time

aura = 1000
l = ["criança chorando", "banco"]

print("Olá, você tem 1k de aura inicial")
time.sleep(0.5)
local = input("Você está na rua, para onde ir: criança chorando/banco? ")

if local not in l:
    print("Diga algo válido, vai ter que recomeçar só pela audacia")

if local == "criança chorando":
    acao = input("*eu devo: chutar a criança(1)/perguntar pq ela tá chorando(2) ")

if acao == 1:
    aura += 200
    print("Parábens você ganhou +200 de aura")
    time.sleep(0.9)
    print(f"Sua aura agr é {aura}")
    time.sleep(0.5)
    print("A criança começou a chorar ainda mais e saiu correndo")
elif acao == 2:
    aura -= 200
    print("você perdeu 200 de aura!")
    time.sleep(0.9)
    print(f"Sua aura agr é {aura}")
    time.sleep(0.5)
    print("A criança diz: Roubaram meu pirulito!")
    acao = input("*eu devo ajudar a criança sim(1)/não(2)")
    if acao == 1:
        print("Você encontra o cara que roubou o pirulito, ele é musculoso")
        time.sleep(0.9)
        acao = input("Tirar X1(1)/ Olhar do anjo caído(2)")
else:
    print("Diga algo válido, vai ter que recomeçar só pela audacia")