menu = """

[d] Depositar
[e] Extrato
[s] Sacar
[x] Sair

--> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Para prosseguir, necessitamos do valor do depósito.: "))

        if valor > 0: # para evitar valores negativos
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Ocorreu um problema ao realizar a operação devido a um valor inválido.")

    elif opcao == "s":
        valor = float(input("Para prosseguir, informe o valor que você gostaria de sacar.: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Ops... Saldo insuficiente, tente novamente:")

        elif excedeu_limite:
            print("Ops... Valor do saque excede o limite.")

        elif excedeu_saques:
            print("Ops... Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Ops... O valor informado é INVÁLIDO.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
