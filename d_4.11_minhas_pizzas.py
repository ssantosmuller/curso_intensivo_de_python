pizzas = ['marguerita', 'quatro queijos', 'peperoni', 'chocolate']

friend_pizzas = pizzas[:]
friend_pizzas.append('mussarela')

print("Meu amigo gosta dos seguintes sabores:")
for fpizzas in friend_pizzas:
    print(fpizzas)

print("Eu prefiro as segintes:")
for pizza in pizzas:
    print(pizza.title())