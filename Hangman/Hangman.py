import random
import sys
from datetime import datetime
import time
import shutil

global points, hidden_password, password
points = 0
hidden_password = []
hidden_password2 = []


def print_lines(txt, start, stop):
    for i in range(start, stop):
        print(txt[i], end="")


def manage_graphics(switcher):
    with open("graphics.txt", "r") as graphics:
        lines = graphics.readlines()

        if switcher == 0:
            print_lines(lines, 13, 20)
        elif switcher == 1:
            print_lines(lines, 21, 28)
        elif switcher == 2:
            print_lines(lines, 29, 36)
        elif switcher == 3:
            print_lines(lines, 37, 43)
        elif switcher == 4:
            print_lines(lines, 44, 51)
        elif switcher == 5:
            print_lines(lines, 52, 59)
        elif switcher == 6:
            print_lines(lines, 0, 13)
        elif switcher == 7:
            print_lines(lines, 60, 77)


def print_hidden(password):
    columns = shutil.get_terminal_size().columns
    line = ""
    for letter in ("".join(password)):
        line = line + "--"
    print(line.center(columns))
    print("".join(password).center(columns))
    print(line.center(columns))


def sorting_highscore():
    global temp_scores
    with open("score.txt", "r") as scores:
        dic_score = {}
        for line in scores:
            key, val = line.split("  ")
            dic_score[key] = val
    temp_scores = [(k, dic_score[k]) for k in sorted(dic_score, key=dic_score.get, reverse=False)]
    return temp_scores


def save_highscore(start, end):
    with open("score.txt", "a") as score:
        score.write('Name: {}  '.format(user_name))
        score.write('Time: {}'.format(end - start))
        score.write("\n")

    sorting_highscore()

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
    global password
    password = ""
    dic = {}
    with open("countriesandcapitals.txt", "r") as capitals:
        for line in capitals:
            (key, val) = line.split(" | ")
            dic[key] = val

    password = random.choice(list(dic.values())).upper().replace('\n', '')
    return password


def printing_password(password, hidden_password):
    global hidden_password2
    hidden_password2 = []
    for letter in password:
        if letter == " ":
            hidden_password.append(" ")
        else:
            hidden_password.append("#")
    print_hidden(hidden_password)
    hidden_password2 = hidden_password[:]
    return hidden_password2


def checking_password(number):
    global points
    if hidden_password2 == hidden_password:
        points += number
    time.sleep(1)
    print("\nBoo! You have +", number, "penalty points!")
    time.sleep(1)
    if points < 4:
        manage_graphics(points)
    elif points == 4:
        manage_graphics(points)
        # Tu trzeba dodać podpowiedź
    else:
        manage_graphics(5)
    return points


def letter():
    print(password)
    letter_guess = input("What's the letter than?").upper()
    for l in password:
        if l == letter_guess:
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


def winrar():
    end_time = datetime.now()
    time.sleep(1)
    print("You won!")
    time.sleep(1)
    print("Congratulations!!")
    time.sleep(1)
    print('Your time: {}'.format(end_time - start_time))
    save_highscore(start_time,end_time)
    time.sleep(2)
    high_score()
    sys.exit()


def word():
    print(password)
    full_guess = input("What's the name than?").upper()
    if full_guess == password:
        winrar()

    else:
        checking_password(2)


def checking(password):
    if password != "".join(hidden_password):
        letter_or_word = input("You want letter(l) or full name(f)?")
        if letter_or_word == "l":
            letter()
        elif letter_or_word == "f":
            word()
    elif password == "".join(hidden_password):
        winrar()
    else:
        print('You can write only "l" or "f"')


def guessing_capital():
    global password, used
    used = []
    while points < 5:
        checking(password)
        time.sleep(1)
        print("Letters You failed guessing: ", ", ".join(used), end=".\n\n")

    time.sleep(2)
    print("You lost!")
    time.sleep(3)
    welcome()


def play_game():
    global start_time, user_name, points
    user_name = input("What's your name?")
    start_time = datetime.now()
    random_password()
    printing_password(random_password(), hidden_password)
    guessing_capital()
    points = 0


def choice():
    pick = input("\nWhat you want to do?")
    while pick != "4":
        if pick == "1":
            play_game()
        elif pick == "2":
            how_to_play()
        elif pick == "3":
            high_score()
        else:
            print("You have chosen the wrong number!")

        pick = input("\nWhat you want to do?")
    print("Bye Bye")


def init():
    welcome()
    choice()


init()
