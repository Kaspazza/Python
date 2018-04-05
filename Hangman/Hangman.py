import random
from datetime import datetime

hangman = (
    "\n  ##   ##    ###    ##    ##    ####    ##     ##    ###    ##    ##   _______ \n  ##   ##   ## ##   ##    ##   ##  ##   ###   ###   ## ##   ##    ##   |      |  \n  ##   ##  ##   ##  ####  ##  ##        #### ####  ##   ##  ####  ##   |      O _ (C'mon, hang me!)\n  #######  #######  ## ## ##  ##  ####  ## ### ##  #######  ## ## ##   |     /|\ \n  ##   ##  ##   ##  ##  ####  ##    ##  ##  #  ##  ##   ##  ##  ####   |     / \ \n  ##   ##  ##   ##  ##   ###   ##  ##   ##     ##  ##   ##  ##   ###   |\ \n  ##   ##  ##   ##  ##    ##    ####    ##     ##  ##   ##  ##    ##   | \ \n \n  Game developed by two clever and handsome students: Mateusz Marurczak & Krzysiek Jodłowski \n",
    "\n_______\n|      |\n| \n| \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (Why are you doing this to me?)\n| \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (One, two, three, my hands is what you hang for me!)\n|     / \ \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (I do not like it very much..)\n|     /|\ \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (Last chance, cowboy!)\n|     /|\ \n|     / \ \n|\ \n| \ \n",
    "\n_______\n|      |\n|      x _ (I'm dead LOL, You happy?)\n|     /|\ \n|     / \ \n|\ \n| \ \n")


def rysowanie(points):
    if points == 0:
        print(hangman[1])
    elif points == 1:
        print(hangman[2])
    elif points == 2:
        print(hangman[3])
    elif points == 3:
        print(hangman[4])
    elif points == 4:
        print(hangman[5])
    else:
        print(hangman[6])


start_time = datetime.now()
dic = {}
print(hangman[0])
print("Welcome to hangman, his life depends on you!")
print("1.Start game")
print("2.How to play")
print("3.Leaderboard")
print("4.Exit")
num = input("what you want to do?")
while True:
    if num == "1":
        with open("countriesandcapitals.txt", "r") as capitals:
            for line in capitals:
                (key, val) = line.split(" | ")
                dic[key] = val
        i = 0
        points = 0
        password = random.choice(list(dic.values()))
        password = password.upper()
        password = password.replace('\n', '')
        hidden_password = []
        hidden_password2 = []

        print(password)
        y = 0

        for letter in password:
            if letter == " ":
                hidden_password.append(" ")
            else:
                hidden_password.append("_")
            y += 1

        print("".join(hidden_password))

        while True:
            rysowanie(points)
            if points >= 5:
                print("You lost!")
                break
            elif points <= 5 and ("".join(hidden_password)) != password:
                letter_or_word = input('Type: "l" if You want to guess letter or "w" if You want a word.')
                hidden_password2 = hidden_password[:]

                if letter_or_word == "l":
                    letter_guess = input("What's the letter then? ").upper()

                    for l in password:

                        if l == letter_guess:
                            x = 0
                            for letter in password:

                                if letter == " ":
                                    hidden_password[x] = " "
                                elif letter == letter_guess:
                                    hidden_password[x] = letter_guess
                                elif letter == "_":
                                    hidden_password[x] = "_"
                                x += 1
                    print("".join(hidden_password))

                    if hidden_password2 == hidden_password:
                        points += 1
                        print("Boo! You have -1 points You bastard!")

                elif letter_or_word == "w":
                    print(password)
                    word_guess = input("What's the word then? ").upper()
                    print(word_guess)

                    if word_guess == password:
                        print("Great! You won the game!")
                        break
                    else:
                        points += 2
                        print("Boo! You have -2 points You bastard!")
                else:
                    print("Type a proper letter!")


            elif ("".join(hidden_password)) == password:
                print("Great! You won the game!")
                break
        break
    elif num == "2":
        print("you just do this and that")
        break

    elif num == "3":
        # plik z tym
        break

    elif num == "4":
        print("BYE BYE")
        break

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
