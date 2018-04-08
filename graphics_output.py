# printing specific lines (iterating in some range on previously read document)

def print_lines(txt, start, stop):
    for i in range(start, stop):
            print (txt[i], end ="")

# reading file and calling print_line function (passing read document and specific lines)

def manage_graphics(switcher):
    with open("graphics.txt", "r") as graphics:
        lines = graphics.readlines()        
        if switcher == 1:
            print_lines(lines, 0, 19)
        elif switcher == 2:
            print_lines(lines, 18, 25) 
        elif switcher == 3:
            print_lines(lines, 25, 33)
        elif switcher == 4:
            print_lines(lines, 33, 41)
        elif switcher == 5:
            print_lines(lines, 41, 49)    
        elif switcher == 6:
            print_lines(lines, 49, 57)
        elif switcher == 7:
            print_lines(lines, 57, 65)
        elif switcher == 8:
            print_lines(lines, 65, 73)

# calling manage_graphics function with some variable in range 1-8

some_var = int(input("Choose 1, 2, 3..8: "))
manage_graphics(some_var)