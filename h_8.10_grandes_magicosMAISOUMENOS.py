magician = ['alice', 'david', 'carolina']

def show_magicians(nomes):
    for magic in magician:
        print("Hello, " + magic.title() + "!")
print("Antes de rodar a função nova:")
show_magicians(magician)
print("----------------------------")


def make_great(names):
    print("O Grande"), show_magicians(magician)

make_great(show_magicians(magician))