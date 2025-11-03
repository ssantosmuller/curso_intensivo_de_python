name = 'MUller'
num = 5

print("name == 'muller'? True")
print(name == 'muller')

print("name == 'mulllller'? False")
print(name == 'mullller')

print("name == 'MUller'? True")
print(name.lower() == "muller")

print(num > 0, "True")
print(num < 0, "False")
print(num == 5, "Verdadeiro")
print(num != 5, "Falso")

print(num > 0 and num > 2, "Verdadeiro")
print(num < 9 and num < 1, "Falso")

print(num > 3 or num < 2, "Verdadeiro")
print(num > 6 or num < 4, "Falso")

listagem = []
print(listagem)
for lista in range(0, 26):
    listagem.append(lista)
print("Verdadeiro", 2 in listagem)
print(listagem)