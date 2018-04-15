import random
import sys
from datetime import datetime
import time


# Picking up user name
def name():
    user_name = input("\n > What's your name? ")
    return user_name


#  Printing out specified lines from txt file
def print_lines(txt, start, stop):
    for i in range(start, stop):
        print(txt[i], end="")


# Managing to print whole "pictures" from file (see above)
def manage_graphics(switcher):
    with open("graphics.txt", "r") as graphics:
        lines = graphics.readlines()

        if switcher == 0:
            print_lines(lines, 14, 22)
        elif switcher == 1:
            print_lines(lines, 22, 30)
        elif switcher == 2:
            print_lines(lines, 30, 38)
        elif switcher == 3:
            print_lines(lines, 38, 46)
        elif switcher == 4:
            print_lines(lines, 45, 54)
        elif switcher == 5:
            print_lines(lines, 53, 62)
        elif switcher == 6:
            print_lines(lines, 0, 14)
        elif switcher == 7:
            print_lines(lines, 62, 83)


# Printing out menu from file
def manage_menu():
    with open("menu.txt", "r") as scores:
        for i, line in enumerate(scores):
            print("   ", i + 1, line, end="")


# Printing out password layout
def print_hidden(password):
    line = ""
    for letter in ("".join(password)):
        line = line + "-"
        indent = len(line) + 4
    print("\n" + line.rjust(indent) + "\n" + "".join(password).rjust(indent) + "\n" + line.rjust(indent) + "\n")    


# Reading txt file with scores and sorting them
def sorting_highscore():
    with open("score.txt", "r") as scores:
        dic_score = {}
        for line in scores:
            key, val = line.split("  ")
            dic_score[key] = val
    temp_scores = [(k, dic_score[k]) for k in sorted(dic_score, key=dic_score.get, reverse=False)]
    return temp_scores


# Saving user highscore
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


# Start graphic and menu
def welcome():
    manage_graphics(6)
    manage_menu()


# Printing out highscore leaderboard
def high_score():
    print(" " + "_" * 45 + "\n\n  Highscore leaderboard:\n")
    with open("score.txt", "r") as scores:
        for i, line in enumerate(scores):
            line = line.split("  ")
            print(" ", (str(i + 1)).rjust(2), line[0].ljust(18), line[1], end="")
    print(" " + "_" * 45 + "\n")


# Printingo out "how to play" part from txt file
def how_to_play():
    try:
        for line in manage_graphics(7):
            print(line)
    except TypeError:
        pass


# Choosing random password from txt file and returning password along with country hint
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


# Printing out password to guess
def printing_password(password, hidden_password):
    global hidden_password2
    hidden_password2 = []
    # print(password)
    for letter in password:
        if letter == " ":
            hidden_password.append(" ")
        else:
            hidden_password.append("#")
    # print_hidden(hidden_password)
    hidden_password2 = hidden_password[:]
    return hidden_password2


# Printing out penalty points and hint
def checking_password(number):
    global points, hidden_password2, hidden_password
    if hidden_password2 == hidden_password:
        points += number
    time.sleep(1)
    print("\n Boo! You have +", number, "penalty points!")
    time.sleep(1)
    hidden_password2 = hidden_password
    if points < 4:
        manage_graphics(points)
    elif points == 4:
        manage_graphics(points)
        print(" Hint: It's a capital of " + country + ".")
    elif points == 5:
        manage_graphics(5)
    return points


# Checking if letter is in name of the city to guess
def letter(password, used):
    global hidden_password
    # print(password)
    letter_guess = input(" > What's the letter than? ").upper()
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
            # print_hidden(hidden_password)
            return hidden_password

    checking_password(1)
    used.append(letter_guess)
    return used


# Printing ot win output, table of highscores, restarts the game
def winrar(start_time, user_name):
    end_time = datetime.now()
    time.sleep(1)
    print("\n *** You won! ***")
    time.sleep(1)
    print(" *** Congratulations!!! ***")
    time.sleep(1)
    print('\n Your time: {}'.format(end_time - start_time))
    save_highscore(start_time, end_time, user_name)
    time.sleep(2)
    high_score()
    init()


# Checking if full name of the city is correct
def word(password, user_name):
    # print(password)
    full_guess = input(" > What's the name than? ").upper()
    if full_guess == password:
        winrar(start_time, user_name)

    else:
        checking_password(2)


# Handling choice of guessing word/letter
def checking(password, user_name):
    global hidden_password
    print_hidden(hidden_password)
    if password != "".join(hidden_password):
        letter_or_word = input(" > You want to guess letter(l) or a full name(f)? ")
        if letter_or_word == "l":
            letter(password, used)
        elif letter_or_word == "f":
            word(password, user_name)
        else:
            print(' You can write only "l" or "f"!')
    elif password == "".join(hidden_password):
        winrar(start_time, user_name)


# Printing out not guessed letters
def guessing_capital(password, used, user_name):
    global points
    while points < 5:
        checking(password, user_name)
        time.sleep(1)
        print("\n Letters You failed guessing: ", ", ".join(used), end=".\n")

    time.sleep(2)
    print("\n *** You lost! Sorry, but the GAME is OVER! ***\n")
    time.sleep(3)
    init()


# Managing play when "start play is chosen"
def play_game(user_name):
    global points, hidden_password, country
    password, country = random_password()    
    printing_password(password, hidden_password)
    guessing_capital(password, used, user_name)    
    return password, country


# Managing the choice when menu appears
def choice():
    pick = input("\n  > What do You want to do? ")
    while pick != "4":
        if pick == "1":
            play_game(name())
        elif pick == "2":
            how_to_play()
            manage_menu()
        elif pick == "3":
            high_score()
            manage_menu()
        else:
            print("    You have chosen the wrong number!")

        pick = input("\n  > What do You want to do? ")
    time.sleep(1)
    print("\n  *** Ok, see You next time! ***\n")
    time.sleep(1)
    sys.exit()


def init():
    global points, hidden_password, hidden_password2, country, used, start_time    
    points = 0
    hidden_password = []
    hidden_password2 = []
    country = ""
    used = []
    start_time = datetime.now()
    welcome()
    choice()


init()
