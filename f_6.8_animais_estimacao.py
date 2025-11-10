pipoca = {'tipo': 'gato',
          'dono': 'laura'
          }
pacoca = {'tipo': 'gato',
          'dono': 'muller'
          }
spike = {'tipo': 'cao',
          'dono': 'ana'
          }
bolinho = {'tipo': 'jabuti',
          'dono': 'laura'
          }

pets  = [bolinho]
for pet in pets:
    for key, value in pet.items():
        print("Eu tenho um animmal", key[0], value,"e seu", key, value) 