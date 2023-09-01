def main():
    n = int(input("Digite a quantidade de pedidos: "))
    total = 0

    for i in range(1, n + 1):
        pedido = input(f"Digite o nome e valor do pedido {i} (exemplo: Hamburguer 10.99): ").split()
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    # Leitura do cupom de desconto
    cupom = input("Digite o cupom de desconto (10% ou 20%): ")

    # Aplicação do desconto com base no cupom
    if cupom == "10%":
        total *= 0.9  # Aplica desconto de 10%
    elif cupom == "20%":
        total *= 0.8  # Aplica desconto de 20%

    # Exibir o valor total formatado
    print(f"Valor total: {total:.2f}")

if __name__ == "__main__":
    main()

