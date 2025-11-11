pacoca = {'tipo': 'gato',
          'dono': 'muller'
          }
pipoca = {'tipo': 'gato',
          'dono': 'laura'
          }
costelinha = {'tipo': 'cachorro',
              'dono': 'antonio'
              }
pets = [pacoca, pipoca, costelinha]

print(pets)

for pet in pets:
    print(pet['dono'].title(), "tem um",pet['tipo'])