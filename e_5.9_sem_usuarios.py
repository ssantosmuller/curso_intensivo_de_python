nomes = []

if nomes == []:
        print("Precisamos encontrar alguns usuários.")        
else:
    for nome in nomes:
        if nome == 'admin':
            print("Seja bem vindo, adiministrador. Deseja que eu iprima seu relatório diário?")
        else:
            print("Seja bem vindo",nome.title(),".")