cities = {'juiz de fora':{
    'country': 'brasil',
    'population': 750,
    'fact': 'princesinha de minas'
    },
          'brasilia': {
    'country': 'brasil',
    'population': 1,
    'fact': 'otima cidade',    
    },
          'olinda':{
    'country': 'brasil',
    'population': 2,
    'fact': 'quero ir embora',
    }
}

for key, value in cities.items():
    print("A cidade de ",key.title(), "fica localiza no", value['country'].title(), "tem sua populaçãode",value['population'],
        " e seu fato curioso é que", value['fact'])