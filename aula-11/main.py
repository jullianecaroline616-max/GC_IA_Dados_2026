import random

cardapio = {
    "chocolate": 5.0,
    "baunilha": 4.5,
    "morango": 3.0,
    "flocos": 9.0,
}

brindes = ["canudo", "copo personalizado", "gelo", "badge"]

def mostrar_cardapio():
    print("Cardápio:")
    for sabor, preco in cardapio.items():
        print(f"{sabor}, R$ {preco:.2f}")

def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor = input("\nEscolha o sabor: (digite 'fechar'para sair)")
        if sabor == "fechar":
            break
        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"{sabor} adicionado!, valor:"m)
        else:
            print("sabor não esta no cardapio")
    return pedido, total
v
mostrar_cardapio()
pedido, total = fazer_pedido()

print(f"\nSeu pedido: {pedido}")
print(f"Total: R$ {total:.2f}")

if total > 15:
    print(f"Parabens voce ganhou um brinde: {random.choice(brindes)}")