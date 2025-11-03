my_fooods = ['pizza', 'falafel', 'carriot cake']
friend_foods = my_fooods[:]

my_fooods.append('canoli')
friend_foods.append('ice cream')

print(my_fooods)

print("Minhas comidas  favoritas são:")
for mfoods in my_fooods:
    print(mfoods)

print(friend_foods)
print("As comidas favoritas do meu amigo são:")
for ffoods in friend_foods:
    print(ffoods)
