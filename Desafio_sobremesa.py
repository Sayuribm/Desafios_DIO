# Desafio

# TODO: Criar as condições necessárias para impressão da saída conforme o enunciado.

# O valor total do pedido for maior ou igual a R$ 50.00, o usuário receberá uma sobremesa grátis.
# Caso contrário, o usuário não receberá nenhum brinde.

valorPedido = int(input("Qual o valor do pediodo?: "))

if valorPedido >= 50:
  print("Parabéns, você ganhou uma sobremesa grátis!")
    
else: 
  print("Que pena, você não ganhou nenhum brinde especial." )