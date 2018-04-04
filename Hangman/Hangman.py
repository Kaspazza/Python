import random

dic = {}
with open("Hangman/countriesandcapitals.txt", "r") as capitals:
    for line in capitals:
        (key, val) = line.split(" | ")
        dic[key] = val

i = 0
points = 5
password = random.choice(list(dic.values()))
password = password.upper()
password = password.replace('\n', '')
hidden_password = []
hidden_password2 = []

print(password)
y=0
for letter in password:
    if letter == " ":
        hidden_password.append(" ")
    else:
        hidden_password.append("#")
    y += 1

print("".join(hidden_password))

while True:
    if points > 0 and ("".join(hidden_password)) != password:        
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
                        elif letter == "#":
                            hidden_password[x] = "#"
                        x += 1
                    print("".join(hidden_password))
            if hidden_password2 == hidden_password:
                points -= 1
                print("Boo! You have -1 points You bastard!")
            
                    
                    
                    # if ("".join(hidden_password)) == password:
                    #     print("Great! You won the game!")
                    #     break      
            
        elif letter_or_word == "w":    
            print(password)
            word_guess = input("What's the word then? ").upper()
            print(word_guess)
            if word_guess == password:
                print("Great! You won the game!")
                break            
            else:
                points -= 2
                print("Boo! You have -2 points You bastard!")
        else:
            print("Type a proper letter!")

    elif points <= 0:
        print("You lost!")
        break
    elif ("".join(hidden_password)) == password:
        print("Great! You won the game!")
        break

