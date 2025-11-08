def main():
    code_line_list = ["...."] * 10
    #A list is made to represent each line under "Mark" on the display board
    mark_line_list = ["...."] * 10      
    display_board(code_line_list, mark_line_list)
    valid_letters_list = ["r", "o", "y", "g", "b", "v"]
    hidden_code = generate_goal(valid_letters_list, 4)
    guess_count = 1
    while guess_count <= 10:
        print("Goal:", hidden_code)
        code_line_list[guess_count - 1] = user_guess(guess_count)
        """The calculate_exact_matches() function is called with the
        hidden_code variable as the first parameter and corresponding index
        from code_line_list as the second parameter. This is assigned to
        the specific index in mark_line_list to update that index"""
        mark_line_list[guess_count - 1] = calculate_exact_matches(hidden_code, code_line_list[guess_count-1])
        display_board(code_line_list, mark_line_list)
        guess_count += 1
    print("Done") 

"""A second parameter has been added to the function below to allow
for the changes in mark_line_list"""
def display_board(code_line, mark_line):
    print("----------")
    print("Code||Mark")
    print("----------")
    print(f"{code_line[0]}||{mark_line[0]}")
    print(f"{code_line[1]}||{mark_line[1]}")
    print(f"{code_line[2]}||{mark_line[2]}")
    print(f"{code_line[3]}||{mark_line[3]}")
    print(f"{code_line[4]}||{mark_line[4]}")
    print(f"{code_line[5]}||{mark_line[5]}")
    print(f"{code_line[6]}||{mark_line[6]}")
    print(f"{code_line[7]}||{mark_line[7]}")
    print(f"{code_line[8]}||{mark_line[8]}")
    print(f"{code_line[9]}||{mark_line[9]}")
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
    goal = ""
    for i in range(0, n):
        goal += random.choice(valid_choices)    
    return goal

def calculate_exact_matches(goal, guess):
    """This function compares each corresponding letter of the two
    parameters. With every match, "B" is added to the exact_matches variable,
    followed by a series of "." until the string is 4 characters long."""
    exact_matches = ""
    for char in range(len(goal)):
        if goal[char] == guess[char]:
            exact_matches += "B"
    while len(exact_matches) < 4:
        exact_matches += "."
    return exact_matches

main()
