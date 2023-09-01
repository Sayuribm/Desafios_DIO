# Desafio
# TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
# TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
# TODO: Imprimir a saída no formato especificado neste desafio.

valorHamburguer = float(input("Qual é o valolr do Hamburguer?: "))
quantidadeHamburguer = int(input("Digite a quantidade: "))
valorBebida = float(input("Qual é o valor da bebida?: "))
quantidadeBebida = int(input("Digite a quantidade: "))
valorPago = float(input("Digite o valor pago: "))

# Calcular o total dos hambúrgueres e das bebidas
totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida

# Calcular o preço total do pedido
precoTotal = totalHamburguer + totalBebida

# Verificar se o valor pago é suficiente
if valorPago >= precoTotal:
    troco = valorPago - precoTotal
    print(f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}.")
else:
    print("ATENÇÃO: O valor pago é insuficiente para cobrir o pedido.")