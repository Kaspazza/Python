import random
import sys
from datetime import datetime
import time

global points, hidden_password, password, country
points = 0
hidden_password = []
hidden_password2 = []
country = []

def print_hidden(passw):
    print("\n", "-----", "\n","".join(passw), "\n", "-----", "\n")

def empty_line():
    print("")

def what_to_do():
    number = input("\nWhat do you want to do? ")
    return number

def print_lines(txt, start, stop):
    for i in range(start, stop):
            print(txt[i], end ="")

def manage_graphics(switcher):
    with open("graphics.txt", "r") as graphics:
        lines = graphics.readlines()

        if switcher == 0:
            print_lines(lines, 25, 33)
        elif switcher == 1:
            print_lines(lines, 33, 41)
        elif switcher == 2:
            print_lines(lines, 41, 49)
        elif switcher == 3:
            print_lines(lines, 49, 57)
        elif switcher == 4:
            print_lines(lines, 57, 65)
        elif switcher == 5:
            print_lines(lines, 65, 73)
        elif switcher == 6:
            print_lines(lines, 0, 18)
        elif switcher == 7:
            print_lines(lines, 18, 24)    

def sorting_highscore():
    global temp_scores
    with open("score.txt", "r") as scores:
        dic_score = {}
        for line in scores:
            key, val = line.split("  ")
            dic_score[key] = val

    temp_scores = [(k, dic_score[k]) for k in sorted(dic_score, key=dic_score.get, reverse=False)]
    return temp_scores

def save_highscore():
    end_time = datetime.now()
    with open("score.txt", "a") as score:
        score.write('Name: {}  '.format(user_name))
        score.write('Time: {}'.format(end_time - start_time))  
        score.write('\n')     

    sorting_highscore()

    while len(temp_scores) > 10:
        del temp_scores[-1]

    with open("score.txt", "w") as final_scores:
        final_scores.write(''.join('{}  {}'.format(x[0], x[1]) for x in temp_scores))

def welcome():    
    manage_graphics(6)    

def high_score():
    print("\nHigh scores:\n")
    with open("score.txt", "r") as scores:
        for i, line in enumerate(scores):
            print((str(i + 1)).ljust(2), line, end="")
        empty_line()        

def how_to_play():
    manage_graphics(7)

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

def hint(password):
    global country
    with open("countriesandcapitals.txt", "r") as countries:
        for line in countries:
            (key, val) = line.split(" | ")
            if password == val:
                country = country.append(val)
        return country

def add_points(number):
    global points
    if hidden_password2 == hidden_password:
        points += number
    time.sleep(1)
    print("\nBoo! You have +", number, "penalty points!\n")
    time.sleep(1)
    if points < 4:
        manage_graphics(points)
    elif points == 4:
        manage_graphics(points)
        print("Hint: A capital of", hint(password))
        #Tu trzeba dodać podpowiedź
    else:
        manage_graphics(5)
    return points

def letter():
    print(password)
    letter_guess = input("\nWhat's the letter than? ").upper()
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

    add_points(1)
    used.append(letter_guess)

def winrar():
    end_time = datetime.now()
    time.sleep(1)
    print("\nYou won!")
    time.sleep(1)
    print("Congratulations!!")
    time.sleep(1)
    print("\n", "Your Time: {}".format(end_time - start_time))
    save_highscore()
    time.sleep(2)
    high_score()
    sys.exit()

def word():
    print(password)
    full_guess = input("\nWhat's the name than? ").upper()
    if full_guess == password:
        winrar()

    else:
        add_points(2)

def checking(password):
    if password != "".join(hidden_password):
        letter_or_word = input("You want to guess a letter(l) or a full name(f)? ")
        if letter_or_word == "l":
            letter()
        elif letter_or_word == "f":
            word()
        else:
            print("You have chosen the wrong letter!")
    elif password == "".join(hidden_password):
        winrar()
    else:
        print('\nYou can write only "l" or "f"\n')

def guessing_capital():
    global password, used
    used = []
    while points < 5:
        checking(password)
        time.sleep(1)
        print("Letters You failed guessing: ", ", ".join(used), end=".\n\n")

    time.sleep(2)
    print("You lost!\n")
    time.sleep(3)    
    sys.exit()

def play_game():
    global start_time, user_name
    user_name = input("\nWhat's your name? ")
    start_time = datetime.now()
    random_password()
    printing_password(random_password(), hidden_password)
    guessing_capital()

def choice():
    choice = what_to_do()
    while choice != "4":
        if choice == "1":
            play_game()            
        elif choice == "2":
            how_to_play()
        elif choice == "3":
            high_score()            
        else:
            print("You have chosen the wrong number!")
        choice = what_to_do()
    time.sleep(1)
    print("\nOk! Bye Bye!\n")
    time.sleep(1)

def init():    
    welcome()
    choice()

init()