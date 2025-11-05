favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

pesquisa = ['lucas', 'jen', 'carlos', 'sarah', 'luiz']

for people in pesquisa:
    if people in favorite_languages:
        print(people.title(), "você já respondeu a pesquisa. Obrigado!\n")
    

    else:
        print(people.title() + ", você pode responder a pesquisa?")