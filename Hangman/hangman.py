import random
import sys
from datetime import datetime
import time


points = 0
hidden_password = []
hidden_password2 = []
country = ""
used = []
start_time = datetime.now()


def name():
    user_name = input("What's your name? ")
    return user_name


def print_lines(txt, start, stop):
    for i in range(start, stop):
        print(txt[i], end="")


def manage_graphics(switcher):
    with open("graphics.txt", "r") as graphics:
        lines = graphics.readlines()

        if switcher == 0:
            print_lines(lines, 14, 21)
        elif switcher == 1:
            print_lines(lines, 22, 30)
        elif switcher == 2:
            print_lines(lines, 30, 38)
        elif switcher == 3:
            print_lines(lines, 38, 45)
        elif switcher == 4:
            print_lines(lines, 45, 53)
        elif switcher == 5:
            print_lines(lines, 53, 61)
        elif switcher == 6:
            print_lines(lines, 0, 14)
        elif switcher == 7:
            print_lines(lines, 61, 78)


def print_hidden(password):
    line = ""
    for letter in ("".join(password)):
        line = line + "-"
    print(line.rjust(3, ' '))
    print("".join(password).rjust(3, ' '))
    print(line.rjust(3, ' '))


def sorting_highscore():
    with open("score.txt", "r") as scores:
        dic_score = {}
        for line in scores:
            key, val = line.split("  ")
            dic_score[key] = val
    temp_scores = [(k, dic_score[k]) for k in sorted(dic_score, key=dic_score.get, reverse=False)]
    return temp_scores


def save_highscore(start, end, user_name):
    with open("score.txt", "a") as score:
        score.write('Name: {}  '.format(user_name))
        score.write('Time: {}'.format(end - start))
        score.write("\n")

    temp_scores = sorting_highscore()
    while len(temp_scores) > 10:
        del temp_scores[-1]

    with open("score.txt", "w") as final_scores:
        final_scores.write(''.join('{}  {}'.format(x[0], x[1]) for x in temp_scores))


def welcome():
    manage_graphics(6)
    with open("menu.txt", "r") as scores:
        for i, line in enumerate(scores):
            print(i + 1, line, end="")


def high_score():
    print("")
    with open("score.txt", "r") as scores:
        for i, line in enumerate(scores):
            print(i + 1, line, end="")


def how_to_play():
    try:
        for line in manage_graphics(7):
            print(line)
    except TypeError:
        pass


def random_password():
    password = ""
    dic = {}
    with open("countriesandcapitals.txt", "r") as capitals:
        for line in capitals:
            (key, val) = line.split(" | ")
            dic[key] = val

    lottery = random.choice(list(dic.items()))
    password = lottery[1].upper().replace('\n', '')
    country = lottery[0].replace('\n', '')
    return password, country


def printing_password(password, hidden_password):
    global hidden_password2
    hidden_password2 = []
    print(password)
    for letter in password:
        if letter == " ":
            hidden_password.append(" ")
        else:
            hidden_password.append("#")
    print_hidden(hidden_password)
    hidden_password2 = hidden_password[:]
    return hidden_password2


def checking_password(number):
    global points, hidden_password2, hidden_password
    if hidden_password2 == hidden_password:
        points += number
    time.sleep(1)
    print("\nBoo! You have +", number, "penalty points!")
    time.sleep(1)
    hidden_password2 = hidden_password
    if points < 4:
        manage_graphics(points)
    elif points == 4:
        manage_graphics(points)
        print("Hint: It's a capital of " + country + ".")
    else:
        manage_graphics(5)
    return points


def letter(password, used):
    global hidden_password
    print(password)
    letter_guess = input("What's the letter than? ").upper()
    for let in password:
        if let == letter_guess:
            i = 0
            for letter in password:
                if letter == " ":
                    hidden_password[i] = " "
                elif letter == letter_guess:
                    hidden_password[i] = letter_guess
                elif letter == "_":
                    hidden_password[i] = "#"
                i += 1
            print_hidden(hidden_password)
            return hidden_password

    checking_password(1)
    used.append(letter_guess)
    return used


def winrar(start_time, user_name):
    end_time = datetime.now()
    time.sleep(1)
    print("You won!")
    time.sleep(1)
    print("Congratulations!!")
    time.sleep(1)
    print('Your time: {}'.format(end_time - start_time))
    save_highscore(start_time, end_time, user_name)
    time.sleep(2)
    high_score()
    sys.exit()


def word(password, user_name):
    print(password)
    full_guess = input("What's the name than? ").upper()
    if full_guess == password:
        winrar(start_time, user_name)

    else:
        checking_password(2)


def checking(password, user_name):
    global hidden_password
    if password != "".join(hidden_password):
        letter_or_word = input("You want letter(l) or full name(f)? ")
        if letter_or_word == "l":
            letter(password, used)
        elif letter_or_word == "f":
            word(password, user_name)
        else:
            print('You can write only "l" or "f"!')
    elif password == "".join(hidden_password):
        winrar(start_time, user_name)


def guessing_capital(password, used, user_name):
    global points
    while points < 5:
        checking(password, user_name)
        time.sleep(1)
        print("Letters You failed guessing: ", ", ".join(used), end=".\n\n")

    time.sleep(2)
    print("You lost!")
    time.sleep(3)
    sys.exit()


def play_game(user_name):
    global points, hidden_password, country
    password, country = random_password()
    printing_password(password, hidden_password)
    guessing_capital(password, used, user_name)
    points = 0
    return password, country


def choice():
    pick = input("\nWhat you want to do? ")
    while pick != "4":
        if pick == "1":
            play_game(name())
        elif pick == "2":
            how_to_play()
        elif pick == "3":
            high_score()
        else:
            print("You have chosen the wrong number!")

        pick = input("\nWhat you want to do? ")
    print("Bye Bye!")


def init():
    welcome()
    choice()


init()