
wybor = input("Please specify a command [list, add, mark, archive]: ")

def wyswietl():
    print("You saved the following to-do items:\n")
    plik = open("text.txt", "r")
    i = 0
    for linia in plik:
        i += 1
        print(str(i) + ". " + linia)
    plik.close()

if wybor == "add":
    dodaj = input("Add an item: ")
    plik = open("text.txt", "a")
    zmienna = ("[ ] " + str(dodaj))
    plik.write(zmienna)
    print("Item added.")
    plik.close()

elif wybor == "list":
    wyswietl()
        
elif wybor == "mark":
    wyswietl()
    wybor = int(input("Which one you want to mark as completed: ")) - 1
    plik = open("text.txt", "r")
    caly = plik.readlines()
    plik.close()
    litery = list(caly[wybor])
    litery[1] = 'x'
    litery = ''.join(litery)
    caly[wybor] = litery
    plik = open("text.txt", "w")
    plik.write("".join(caly))
    #print(caly[wybor] + "is completed")
    plik.close()

elif wybor == "archive":
    plik = open("text.txt", "r")
    caly = plik.readlines()
    plik.close()
    w = 0
    while w < len(caly):
        zmienna = list(caly[w])
        if zmienna[1] == 'x':
            caly.remove(caly[w])
            w -= 1
        w += 1
    plik = open("text.txt", "w")
    plik.write("".join(caly))
    #print(caly[wybor] + "is completed")
    plik.close()