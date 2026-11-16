import tkinter as tk

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a/b

def mul(a, b):
    return a*b

def fsoma():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = soma(n1, n2)

    resultado.config(text="Resultado: " + str(valor))

def fsub():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = sub(n1, n2)

    resultado.config(text="Resultado: " + str(valor))

def fdiv():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = div(n1, n2)

    resultado.config(text="Resultado: " + str(valor))

def fmul():
    n1 = float(numero1.get())
    n2 = float(numero2.get())

    valor = mul(n1, n2)

    resultado.config(text="Resultado: " + str(valor))

janela = tk.Tk()

janela.config(bg="darkblue")

janela.title("Calculadora")

tk.Label(janela, text="Calculadora", bg="blue", fg="white").pack(padx=100, pady=20)

tk.Label(janela, text="Primeiro numero", bg="blue", fg="white").pack(padx=100, pady=20)

numero1 = tk.Entry(janela)
numero1.pack()

tk.Label(janela, text="Segundo numero", bg="blue", fg="white").pack(padx=100, pady=20)

numero2 = tk.Entry(janela)
numero2.pack()

tk.Button(janela, text="+", command=fsoma, bg="blue", fg="white").pack(padx=100, pady=10)

tk.Button(janela, text="-", command=fsub, bg="blue", fg="white").pack(padx=100, pady=10)

tk.Button(janela, text="*", command=fmul, bg="blue", fg="white").pack(padx=100, pady=10)

tk.Button(janela, text="/", command=fdiv, bg="blue", fg="white").pack(padx=100, pady=10)

resultado = tk.Label(janela, text="Resultado", bg="blue", fg="white")
resultado.pack(padx=100, pady=20)

janela.mainloop()