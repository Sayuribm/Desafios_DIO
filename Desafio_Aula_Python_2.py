def menu():
    menu = """
=============== MENU ================
      1 - Novo usuário
      2 - Nova conta
      3 - Listar contas
      4 - Depositar
      5 - Extrato
      6 - Sacar
      X - Sair
=> """
    return input(menu)



def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo: print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite: print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques: print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor  # Realiza o saque deduzindo o valor do saldo
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"  # Registra a operação de saque no extrato
        numero_saques += 1  # Incrementa o contador de saques
        print("\n=== Saque realizado com sucesso! ===")
    else: print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato


def exibir_extrato(saldo, extrato=None):
    if extrato is None:
        extrato = "Não foram realizadas movimentações."
    
    print("\n================ EXTRATO ================")
    print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (ddmmaaaa): ")
    endereco = input("Informe o endereço (CEP): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    # Definição de constantes
    LIMITE_SAQUES = 3  # Limite de saques permitidos
    AGENCIA = "0001"   # Agência padrão

    # Inicialização de variáveis
    saldo = 0           
    limite = 500        
    extrato = ""        
    numero_saques = 0   
    usuarios = []       
    contas = []         


    while True:
        opcao = menu()

        if opcao == "4":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "6":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "5":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "1":
            criar_usuario(usuarios)

        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "3":
            listar_contas(contas)

        elif opcao == "X":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()