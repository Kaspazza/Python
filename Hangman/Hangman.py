import random
import json
from datetime import datetime

hangman = (
    "\n  ##   ##    ###    ##    ##    ####    ##     ##    ###    ##    ##   _______ \n  ##   ##   ## ##   ##    ##   ##  ##   ###   ###   ## ##   ##    ##   |      |  \n  ##   ##  ##   ##  ####  ##  ##        #### ####  ##   ##  ####  ##   |      O _ (C'mon, hang me!)\n  #######  #######  ## ## ##  ##  ####  ## ### ##  #######  ## ## ##   |     /|\ \n  ##   ##  ##   ##  ##  ####  ##    ##  ##  #  ##  ##   ##  ##  ####   |     / \ \n  ##   ##  ##   ##  ##   ###   ##  ##   ##     ##  ##   ##  ##   ###   |\ \n  ##   ##  ##   ##  ##    ##    ####    ##     ##  ##   ##  ##    ##   | \ \n \n  Game developed by two clever and handsome students: Mateusz Marurczak & Krzysiek Jodłowski \n",
    "\n_______\n|      |\n| \n| \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (Why are you doing this to me?)\n| \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (One, two, three, my hands is what you hang for me!)\n|     / \ \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (I do not like it very much..)\n|     /|\ \n| \n|\ \n| \ \n",
    "\n_______\n|      |\n|      O _ (Last chance, cowboy!)\n|     /|\ \n|     / \ \n|\ \n| \ \n",
    "\n_______\n|      |\n|      x _ (I'm dead LOL, You happy?)\n|     /|\ \n|     / \ \n|\ \n| \ \n")

not_in_word = []


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
print("\nWelcome to hangman, his life depends on you!")
print("1.Start game")
print("2.How to play")
print("3.Leaderboard")
print("4.Exit")
num = input("\nWhat o You want to do? ")
while True:
    if num == "1":
        user_name = input("What's Your Name? ")
        with open("Hangman/countriesandcapitals.txt", "r") as capitals:
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
            print("Letters You failed guessing: ", ", ".join(not_in_word), end=".\n")
            if points >= 5:
                print("You lost!")
                break
            elif points <= 5 and ("".join(hidden_password)) != password:
                letter_or_word = input('Type: "l" if You want to guess letter or "w" if You know whole capital name.')
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
                        not_in_word.append(letter_guess)
                        print("Boo! You have -1 points You bastard!")

                elif letter_or_word == "w":
                    print(password)
                    word_guess = input("What's the word then? ").upper()
                    print(word_guess)

                    if word_guess == password:
                        print("Great! You won the game!")
                        end_time = datetime.now()
                        print('Duration: {}'.format(end_time - start_time))

                        with open("Hangman/score.txt", "a") as score:
                            score.write('Name: {}  '.format(user_name))
                            score.write('Duration: {}'.format(end_time - start_time))
                            score.write("\n")

                        with open("Hangman/score.txt", "r") as scores:
                            dic_score = {}
                            for line in scores:
                                (key, val) = line.split("  ")
                                dic_score[key] = val

                        temp_scores = [(k, dic_score[k]) for k in sorted(dic_score, key = dic_score.get, reverse = False)]

                        while True:
                            if len(temp_scores) > 10:
                                del temp_scores[-1]
                            else:
                                break

                        with open("Hangman/score.txt", "w") as final_scores:
                            final_scores.write(''.join('{}  {}'.format(x[0],x[1]) for x in temp_scores))

                        with open("Hangman/score.txt", "r") as scores:
                            i=0
                            for line in scores:
                                print(i+1, line, end = "")
                                i += 1
                        
                        break
                    
                    else:
                        points += 2
                        print("Boo! You have -2 points You bastard!")
                else:
                    print("Type a proper letter!")


            elif ("".join(hidden_password)) == password:
                print("Great! You won the game!")
                end_time = datetime.now()
                print('Duration: {}'.format(end_time - start_time))

                with open("Hangman/score.txt", "a") as score:
                    score.write('Name: {}  '.format(user_name))
                    score.write('Duration: {}'.format(end_time - start_time))
                    score.write("\n")

                with open("Hangman/score.txt", "r") as scores:
                    dic_score = {}
                    for line in scores:
                        (key, val) = line.split("  ")
                        dic_score[key] = val

                temp_scores = [(k, dic_score[k]) for k in sorted(dic_score, key = dic_score.get, reverse = False)]

                while True:
                    if len(temp_scores) > 10:
                        del temp_scores[-1]
                    else:
                        break

                with open("Hangman/score.txt", "w") as final_scores:
                    final_scores.write(''.join('{}  {}'.format(x[0],x[1]) for x in temp_scores))

                with open("Hangman/score.txt", "r") as scores:
                    i=0
                    for line in scores:
                        print(i+1, line, end = "")
                        i += 1                
                break


        break

    elif num == "2":
        print("you just do this and that")
        break

    elif num == "3":
        with open("Hangman/score.txt", "r") as scores:
                i=0
                for line in scores:
                    print(i+1, line, end = "")
                    i += 1
        break

    elif num == "4":
        print("BYE BYE")
        break



#temp_scores = "".join(temp_scores)

# while True:
#     if len(temp_scores) > 10:
#         del temp_scores[-1]
#     else:
#         break

# print(temp_scores)
# print(json.dump(temp_scores, separators=("  ")))

#  with open("Hangman/score.txt", "w") as new_scores:
#      json.dump(temp_scores, new_scores, separators=("  "))


# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))

# with open("Hangman/score.txt", "a") as score:
#     score.write('Name: {}  '.format(user_name))
#     score.write('Duration: {}'.format(end_time - start_time))
#     score.write("\n")

# with open("Hangman/score.txt", "r") as scores:
#     dic_score = {}
#     for line in scores:
#         (key, val) = line.split("  ")
#         dic_score[key] = val

# temp_scores = [(k, dic_score[k]) for k in sorted(dic_score, key = dic_score.get, reverse = False)]

# while True:
#     if len(temp_scores) > 10:
#         del temp_scores[-1]
#     else:
#         break

# with open("Hangman/score.txt", "w") as final_scores:
#     final_scores.write(''.join('{}  {}'.format(x[0],x[1]) for x in temp_scores))

# with open("Hangman/score.txt", "r") as scores:
#     i=0
#     for line in scores:
#         print(i+1, line, end = "")
#         i += 1
