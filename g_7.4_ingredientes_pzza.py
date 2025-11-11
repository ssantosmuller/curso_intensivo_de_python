ing = True
while ing == True:
    ingredientes = input("Digite um ingrediente para sua pizza e tecle ENTER.\nCaso queira finalizar, digite QUIT.\nDigite: ")
    print("\nVocê digitou -", ingredientes, "-\n")
    if ingredientes == 'quit':
        print("Aguarde. Seu pedido já estará pronto.")
        break