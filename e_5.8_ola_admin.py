nomes = ['joão', 'josé', 'maria', 'admin', 'clara']
for nome in nomes:
    if nome == 'admin':
        print("Seja bem vindo, adiministrador. Deseja que eu iprima seu relatório diário?")
    else:
        print(nome.title())