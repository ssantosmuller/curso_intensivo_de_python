mult = input("Digite um número e saberemos se ele é múltiplo de 10.\n Digite: ")
mult = int(mult)
print("Você digitou",mult)
if mult % 2 == 0 and mult % 5 == 0:
    print("O número digitado é multiplo de 10.")
else:
     print("O número digitado não é multiplo de 10.")
