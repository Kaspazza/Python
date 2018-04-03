def wyswietl():
    print("You saved the following to-do items:\n")
    with open('text.txt', 'r') as plik:
        i = 0
        for linia in plik:
            i += 1
            print(str(i) + ". " + linia + "\n")


def dodawanie():
    dodaj = input("Add an item: ")
    with open('text.txt', 'a') as plik:
        zmienna = ("[ ] " + str(dodaj) + "\n")
        plik.write(zmienna)
        print("Item added.")


def wykonane():
    wybor = int(input("Which one you want to mark as completed: ")) - 1
    with open('text.txt', 'r') as plik:
        caly = plik.readlines()
    litery = list(caly[wybor])
    litery[1] = 'x'
    litery = ''.join(litery)
    caly[wybor] = litery
    with open('text.txt', 'w') as plik:
        plik.write("".join(caly))


def usuwanie():
    with open('text.txt', 'r') as plik:
        caly = plik.readlines()
    w = 0
    while w < len(caly):
        zmienna = list(caly[w])
        if zmienna[1] == 'x':
            caly.remove(caly[w])
            w -= 1
        w += 1
    with open('text.txt', 'w') as plik:
        plik.write("".join(caly))


def start():
    while True:
        wybor = input("Please specify a command [list, add, mark, archive, exit]: ")
        if wybor == "add":
            dodawanie()

        elif wybor == "list":
            wyswietl()

        elif wybor == "mark":
            wyswietl()
            wykonane()

        elif wybor == "archive":
            usuwanie()

        elif wybor == "exit":
            break

        else:
            print("You've typed something wrong, try again later")


start()
