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
            print("You win!")
        guess_count += 1
    if guess_count == 11:
        print("You lose!")

def display_board(code_line, mark_line):
    print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
    print("\u2502MASTERMIND\u2502")
    print("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518")
    print("\u250c\u2500\u2500\u2500\u2500\u252c\u252c\u2500\u2500\u2500\u2500\u2510")
    print("\u2502Code\u2502\u2502Mark\u2502")
    print("\u251c\u2500\u2500\u2500\u2500\u253c\u253c\u2500\u2500\u2500\u2500\u2524")
    print(f"\u2502{code_line[0]}\u2502\u2502{mark_line[0]}\u2502")
    print(f"\u2502{code_line[1]}\u2502\u2502{mark_line[1]}\u2502")
    print(f"\u2502{code_line[2]}\u2502\u2502{mark_line[2]}\u2502")
    print(f"\u2502{code_line[3]}\u2502\u2502{mark_line[3]}\u2502")
    print(f"\u2502{code_line[4]}\u2502\u2502{mark_line[4]}\u2502")
    print(f"\u2502{code_line[5]}\u2502\u2502{mark_line[5]}\u2502")
    print(f"\u2502{code_line[6]}\u2502\u2502{mark_line[6]}\u2502")
    print(f"\u2502{code_line[7]}\u2502\u2502{mark_line[7]}\u2502")
    print(f"\u2502{code_line[8]}\u2502\u2502{mark_line[8]}\u2502")
    print(f"\u2502{code_line[9]}\u2502\u2502{mark_line[9]}\u2502")
    print("\u2514\u2500\u2500\u2500\u2500\u2534\u2534\u2500\u2500\u2500\u2500\u2518")

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
