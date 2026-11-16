op = ["soma", "sub", "div", "mul"]



while True:

    n1 = int(input("Fala um numero ai: "))

    ops = input("Fala uma das 4 operações básicas (soma, sub, div, mul): ")

    n2 = int(input("fala outro numero ae: "))

    if ops == op[0]:
        print(n1+n2)
    elif ops == op[1]:
        print(n1-n2)
    elif ops == op[2]:
        print(n1/n2)
    else:
        print(n1*n2)

    dnv = input("Fazer outra conta? s/n: ")

    if dnv != "s":
        break

