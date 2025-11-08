def main():
    code_line_list = ["...."] * 10
    mark_line_list = ["...."] * 10      
    display_board(code_line_list, mark_line_list)
    valid_letters_list = ["r", "o", "y", "g", "b", "v"]
    hidden_code = generate_goal(valid_letters_list, 4)
    guess_count = 1
    while guess_count <= 10:
        code_line_list[guess_count - 1] = user_guess(guess_count)
        mark_line_list[guess_count - 1] = calculate_matches(hidden_code, code_line_list[guess_count-1])
        display_board(code_line_list, mark_line_list)
        if mark_line_list[guess_count - 1] == "BBBB":
            guess_count = 100
            #guess_count has been set to much higher to stop the while loop
            print("You win!")
        guess_count += 1
    if guess_count == 11:
        print("You lose!")

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
    """Given a string of letters and an integer value n,
    return a string containing a random selection of n characters
    selected from the letters in valid_choices"""
    goal = ""
    for i in range(0, n):
        goal += random.choice(valid_choices)    
    return goal

def calculate_matches(goal, guess):
    """The function name has changed to calculate all matches to allow
    a more efficient way to add to the variable matches.
    A list has been created for each of the variables goal and guess.
    Each of the indexes in the goal list consists of the individual letters
    of the hidden code, and each of the indexes in the guess list consists of
    the individual letters of the user's guess.
    The lists have been created to allow removal of that letter to ensure there
    are no double-ups from previous letter matches. Random letters; "a" for
    goal and "z" for guess, have been inserted in thei place to not change
    the length of the lists"""
    goal_letters_list = [goal[0], goal[1], goal[2], goal[3]]
    guess_letters_list = [guess[0], guess[1], guess[2], guess[3]]
    matches = ""
    for i in range(len(goal_letters_list)):
        if goal_letters_list[i] == guess_letters_list[i]:
            matches += "B"
            goal_letters_list.pop(i)
            guess_letters_list.pop(i)
            goal_letters_list.insert(i, "a")
            guess_letters_list.insert(i, "z")
    for i in range(len(goal_letters_list)):
        if goal_letters_list[i] == guess_letters_list[0]:
            matches += "W"
            goal_letters_list.pop(i)
            guess_letters_list.pop(0)
            goal_letters_list.insert(i, "a")
            guess_letters_list.insert(0, "z")
        elif goal_letters_list[i] == guess_letters_list[1]:
            matches += "W"
            goal_letters_list.pop(i)
            guess_letters_list.pop(1)
            goal_letters_list.insert(i, "a")
            guess_letters_list.insert(1, "z")
        elif goal_letters_list[i] == guess_letters_list[2]:
            matches += "W"
            goal_letters_list.pop(i)
            guess_letters_list.pop(2)
            goal_letters_list.insert(i, "a")
            guess_letters_list.insert(2, "z")
        elif goal_letters_list[i] == guess_letters_list[3]:
            matches += "W"
            goal_letters_list.pop(i)
            guess_letters_list.pop(3)
            goal_letters_list.insert(i, "a")
            guess_letters_list.insert(3, "z")
    while len(matches) < 4:
        matches += "."
    return matches

main()
