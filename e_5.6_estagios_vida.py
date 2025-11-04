age = -9

if age < 2 and age > 0:
    print("Sua idade é menor que 2 anos. Ainda é um bebê")
elif age >= 2 and age < 4:
    print("Sua idade está entre 2 e 4. É considerado uma criança.")
elif age >= 4 and age < 13:
    print("Sua idade está entre 4 e 13. É considerado um garoto.")
elif age >= 13 and age < 20:
    print("Sua idade está entre 13 e 20. É considerado um adolescente.")
elif age >= 20 and age < 65:
    print("Sua idade está entre 20 e 65. É considerado um adulto.")
elif age >= 65 and age < 123:
    print("Sua idade é maoir que 65. É considerado um idoso.")
elif age < 0:
    print("A idade não condiz com a ralidade. Verefique e digite novamente. ")

else:
    print("A idade não condiz com a realidade. Verefique e digite novamente. ")

