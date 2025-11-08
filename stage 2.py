def main():
    display_board()
    user_guess()

def display_board():
    print("----------")
    print("Code||Mark")
    print("----------")
    print("....||....")
    print("....||....")
    print("....||....")
    print("....||....")
    print("....||....")
    print("....||....")
    print("....||....")
    print("....||....")
    print("....||....")
    print("....||....")
    print("----------")

def user_guess():
    guess_validity = False      #this variable will return whether the user's guess is valid
                                #it has been set to false to start the while loop
    while guess_validity == False:
        user_guess = input("Guess (roygbv): ")      #anytime the validity of the user's guess returns false, it will prompt the user to enter a new guess
        if (len(user_guess) != 4):        
            guess_validity = False      #this ensures the user enters exactly 4 character for their guess
        else:
            valid_letters_count = 0
            #the following for...in loop using the range() function goes through each character of the guess to make sure the character is valid
            for char in range(len(user_guess)): 
                if ((user_guess[char] == "r") or (user_guess[char] == "o")
                    or (user_guess[char] == "y") or (user_guess[char] == "g")
                    or (user_guess[char] == "b") or (user_guess[char] == "v")):
                    valid_letters_count += 1        #this variable adds a count for every valid character
            if valid_letters_count == 4:
                guess_validity = True           #guess is valid if there are exactly 4 valid characters
            else:
                guess_validity = False
    print("You guessed:", user_guess)       #the while loop will end when the guess validity no longer returns as false, then it will run this line to display the user's guess

main()
display_board()
