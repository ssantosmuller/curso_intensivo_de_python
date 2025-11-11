print("-----Inicio-----")
unconfirmed_users = ['1', '2', '3']
confirmed_users = []
print("Lista de usuários não confirmados:",unconfirmed_users)
print("Lista de usuários confirmados:",confirmed_users)


while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Lista de usuários não confirmados:",unconfirmed_users)
    print("Lista de usuários confirmados:",confirmed_users)


    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    print("Lista de usuários não confirmados:",unconfirmed_users)
    print("Lista de usuários confirmados:",confirmed_users)

print("\n The followin users have bem confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("Lista de usuários não confirmados:",unconfirmed_users)
print("Lista de usuários confirmados:",confirmed_users)

print("-----Fim-----")