from random import randint

def psw(length,upper,lower,numbers,symbols):
    new_psw = ""
    i = 0
    # loop to fill the password
    while i < length:
        # fill with random when no parameters are given or left
        if upper == 0 and lower == 0 and numbers == 0 and symbols == 0:
            temp_char = char(0,71)
            new_psw += temp_char
            i += 1
        # pick random capital letters
        if upper != 0:
            temp_char = char(36,61)
            upper -= 1
            i += 1
            new_psw += temp_char
        # pick random lower letters
        if lower != 0:
            temp_char = char(0,25)
            lower -= 1
            i += 1
            new_psw += temp_char
        # pick random numbers
        if numbers != 0:
            temp_char = char(26,35)
            numbers -=1
            i += 1
            new_psw += temp_char
        # pick random symbol
        if symbols != 0:
            temp_char = char(62,71)
            symbols -= 1
            i += 1
            new_psw += temp_char

    return new_psw

def char(start,stop):
    ##return a random char for the new password
    s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*?"
    place = randint(start,stop)
    char = s[place]
    return char

def menu():
    # set parameters for easy use in the program
    upper = 0
    lower = 0
    numbers = 0
    symbols = 0
    # the start of the random password generator
    print("To create your random password please select the length of the password:\n")
    while True:
        try:
            length = int(input())
        except ValueError:
            print("Please input numbers only")
            continue
        if length > 0:
            break
        print("The length cant be 0 or a negative")
    print("Do you want to pick how many of every char group you wand or fully random?\n"
                       "1.I want to pick\n"
                       "2.Just give me a random one")
    while True:
        try:
            option = int(input())
        except ValueError:
            print("Please input numbers only")
            continue
        if option == 1 or option == 2 :
            break
        print("You must pick 1 or 2 only")
    # when option 1 is picked go on by one to get the user input for its password
    if option == 1:
        print("How many capital letters do you want?")
        while True:
            try:
                upper = int(input())
            except ValueError:
                print("Please input numbers only")
                continue
            if upper < 0 :
                print("Cant be a negative number")
            elif 0 <= upper <= length:
                break
            else:
                print("The number of capital letters cant be more then the " + str(length))
        char_left = length - upper
        # makes sure there is more room in the password
        if char_left != 0:
            print("How many lower letters do you want?")
            while True:
                try:
                    lower = int(input())
                except ValueError:
                    print("Please input numbers only")
                    continue
                if lower < 0:
                    print("Cant be a negative number")
                elif 0 <= lower <= char_left:
                    break
                else:
                    print("The number of lower letters cant be more then: " + str(char_left))
        else:
            print("You have reached your password length")
            print("Your password is:\n" + psw(length, upper, lower, numbers, symbols))
            return
        char_left -= lower
        # makes sure there is more room in the password
        if char_left != 0:
            print("How many numbers do you want?")
            while True:
                try:
                    numbers = int(input())
                except ValueError:
                    print("Please input numbers only")
                    continue
                if numbers < 0:
                    print("Cant be a negative number")
                elif 0 <= numbers <= char_left:
                    break
                else:
                    print("cant pick more then: " + str(char_left))
        else:
            print("You have reached your password length")
            print("Your password is:\n" + psw(length, upper, lower, numbers, symbols))
            return
        char_left -= numbers
        # makes sure there is more room in the password
        if char_left != 0:
            print("How many symbols do you want?")
            while True:
                try:
                    symbols = int(input())
                except ValueError:
                    print("Please input numbers only")
                    continue
                if symbols < 0:
                    print("Cant be a negative number")
                elif 0 <= symbols <= char_left:
                    print("Your password is:\n" + psw(length, upper, lower, numbers, symbols))
                    break
                else:
                    print("cant pick more then: " + str(char_left))
        else:
            print("You have reached your password length")
            print("Your password is:\n" + psw(length, upper, lower, numbers, symbols))
            return

    # when option 2 is picked create fully random password with in the given length
    if option == 2:
        print("Your password is:\n" + psw(length, upper, lower, numbers, symbols))


menu()

