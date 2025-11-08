def main():
    code_line_list = ["...."] * 10      #all the lines of dots under code in the display board is being presented in this list
    display_board(code_line_list)
    guess_count = 1
    while guess_count <= 10:    
        code_line_list[guess_count - 1] = user_guess(guess_count)   #each index of the list is changed to the user's guess which is now returned when calling the user_guess() function
        display_board(code_line_list)       #the display_board() function is called with the updated information from the list
        guess_count += 1
    print("Done") 

def display_board(code_line):
    print("----------")
    print("Code||Mark")
    print("----------")
    print(f"{code_line[0]}||....")      #each line has been replaced with the list indexes from the main() function
    print(f"{code_line[1]}||....")
    print(f"{code_line[2]}||....")
    print(f"{code_line[3]}||....")
    print(f"{code_line[4]}||....")
    print(f"{code_line[5]}||....")
    print(f"{code_line[6]}||....")
    print(f"{code_line[7]}||....")
    print(f"{code_line[8]}||....")
    print(f"{code_line[9]}||....")
    print("----------")

def user_guess(guess_number):
    guess_validity = False     
    while guess_validity == False:
        user_guess = input(f"{guess_number} (roygbv): ") 
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
    return user_guess       #the display_board() function has been moved to the while loop in the main() function and the user_guess() function now returns the user's valid guess


main()
