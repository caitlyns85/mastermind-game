def main():
    code_line_list = ["...."] * 10
    display_board(code_line_list)
    """A list has been created with each of the valid letters.
    The generate_goal() function is called with the list of valid letters
    as the first parameter and 4 as the second parameter to generate 
    a set of 4 random letters using the roygbv letters. This has been
    stored under the variable hidden_code."""
    valid_letters_list = ["r", "o", "y", "g", "b", "v"]
    hidden_code = generate_goal(valid_letters_list, 4)
    guess_count = 1
    while guess_count <= 10:
        print("Goal:", hidden_code)
        code_line_list[guess_count - 1] = user_guess(guess_count)
        display_board(code_line_list)
        guess_count += 1
    print("Done") 

def display_board(code_line):
    print("----------")
    print("Code||Mark")
    print("----------")
    print(f"{code_line[0]}||....")
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
    return user_guess

import random
def generate_goal(valid_choices, n):
    """Given a string of letters and an integer value n,
    return a string containing a random selection of n characters
    selected from the letters in valid_choices"""
    goal = ""
    for i in range(0, n):
        goal += random.choice(valid_choices)    
    return goal

main()
