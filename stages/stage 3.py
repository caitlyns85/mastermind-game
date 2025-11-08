def main():
    display_board()
    guess_count = 1                 #this variable will keep count of how many guesses the user has entered
    while guess_count <= 10:    
        user_guess(guess_count)     #this while loop calls the user_guess() function with the guess_count variable as the entered parameter
        guess_count += 1            #the guess count goes up in increments of one to count the number of guesses the user is making
    print("Done")                   #once the guess_count reaches 10, the while loop will stop and this line will run which displays "Done" to the user

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

def user_guess(guess_number):
    guess_validity = False     
    while guess_validity == False:
        user_guess = input(f"{guess_number} (roygbv): ")    #"Guess" from the previous stage has been replaced with the guess number which is tracked using the guess_count variable in the main function
        if (len(user_guess) != 4):  
            guess_validity = False  
        else:
            valid_letters_count = 0
            for char in range(len(user_guess)): 
                if ((user_guess[char] == "r") or (user_guess[char] == "o")
                    or (user_guess[char] == "y") or (user_guess[char] == "g")
                    or (user_guess[char] == "b") or (user_guess[char] == "v")):
                    valid_letters_count += 1      
            if valid_letters_count == 4:
                guess_validity = True         
            else:
                guess_validity = False
    display_board()     #instead of printing the user's guess, the display_board function is called again

main()
