lugares = {}
teste = True
while teste:
    nome = input("Digite seu nome: ")
    lugar = input("Se você pudesse visitar um lugar do mundo, para onde você iria?")
    lugares[nome] = lugar
    continuar = input("Outra pessoa deseja preencher a pesquisa? (s/n)")
    if continuar == 'n':
            teste = False
print(lugares)
for key, value in lugares.items():
      print(key,"disse que iria para",value)