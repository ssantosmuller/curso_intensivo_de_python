print("----Sanduícheda Pipoca----")
print("Atenção: Infelizmente estamos sem PASTRAMI. Sanduíches desse sabor não faremos hoje. Pedimos desculpas pelo incoveniente.")
sandwich_orders = ['atum', 'pastrami', 'natural', 'frango', 'pastrami', 'carne', 'queijo', 'pastrami']

finished_sandwichs = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    #retira os sanduíches de trás para frente (.pop)
    print("Retira o sabor:",current_sandwiches)
    
    #armazena os sanduíches
    finished_sandwichs.append(current_sandwiches)

#percorre os sanduíches confirmados um por um
for finished in finished_sandwichs:
    print("Confirmo o sabor", finished)