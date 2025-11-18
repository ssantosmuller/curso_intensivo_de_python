sandwich_orders = ['atum', 'natural', 'frango', 'carne', 'queijo']

finished_sandwichs = []

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    #retira os sanduíches de trás para frente (.pop)
    print("Retira o sabor:",current_sandwiches)
    
    #armazena os sanduíches
    finished_sandwichs.append(current_sandwiches)

#percorre os sanduíches confirmados um por um
for finished in finished_sandwichs:
    print("Confirmo o sabor", finished)