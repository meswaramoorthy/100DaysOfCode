VALID_COLORS = ['blue', 'red', 'black', 'white']

"""Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
while True:
        userinput = input("Please enter a color")
        if userinput.lower() == "quit":
            print('bye')
            break
        elif userinput.lower() in VALID_COLORS:
            print(userinput.lower())
            continue
        else:
            print("Not a valid color")
            continue
