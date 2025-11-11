people = input("Obrigado por escolher nosso restaurate.\n Digite o númmero de pessoas que vão jantar: ")
people = int(people)
if people <= 0:
    print("Núero de pessoas errado. Dogite novamente.")
elif people > 8:
    print("Aguarde um instante enquanto esperamos uma mesa desocupar.")
else:
    print("Sua mesa está pronta. Pode nos acompanhar.")