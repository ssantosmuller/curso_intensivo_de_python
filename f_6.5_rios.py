rios = {'nilo': 'egito',
        'amazonas': 'brasil',
        'misissipi': 'EUA'
        }
for nome, pais in rios.items():
    print("O Rio " + nome.title() + " percorre pelo " + pais.title())

for nome in rios.keys():
    print("Há um rio que se chama " + nome.title())

for pais in rios.values():
    print("O país é o " + pais.title())