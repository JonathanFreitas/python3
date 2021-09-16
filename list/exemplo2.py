#exemplo carrinho de compras

carrinho = []
fim = 'S'
while fim != 'N':
    produto = input('Digite o nome do produto: ')
    carrinho.append(produto)
    fim = input('Deseja continuar:\n [S] Sim ou [N] Não: ')
    fim = fim.upper()

print(carrinho)
