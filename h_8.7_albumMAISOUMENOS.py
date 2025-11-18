def make_album(name, title, faixas):
    saida = True
    while saida:
        name = input("Digite o nome do artista: ")
        title = input("Agora digite o nome do álbum: ")
        faixas = input("Por fim, informe quantas canções tem o álbum: ")
        pergunta = input("Deseja inserir mais algum artista? (S/N)")
        if pergunta == 'N':
                saida = False
        album = {'singer': name, 'disk': title}
        if faixas:
            album['faixas'] = faixas
        return album

