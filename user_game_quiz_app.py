# Import necessary modules
import sys # To allow program exit
import random # For shuffling questions
import os # To check for file existence
from colorama import init, Fore, Style # For colored console text
from pyfiglet import Figlet # For ASCII art titles

# Initialize colorama so that styles reset automatically after each print
init(autoreset = True)

# File paths for storing questions and high scores
questions_file = "quiz_creator.txt" # For storing user input questions
high_score_file = "high_scores.txt" # For storing player names and scores

# Load quiz questions from file
def load_questions():
    if not os.path.exists(questions_file): # Check if the quiz file exists
        print("Quiz file not found") # Display error if file is missing
        return[] # Return empty list if no file exists

    with open(questions_file, "r") as quiz_file: # Open the quiz file in read mode
        question_blocks = quiz_file.read().split("-----\n") # Read entire content and split into blocks by the "-----\n" delimiter

    # List to store parsed question dictionaries
    quiz_questions = []

    # Loop over each question block
    for question_block in question_blocks:
        lines_in_block = question_block.strip().splitlines() # Remove extra whitespace and split lines
        if len(lines_in_block) < 6: # If the block has fewer than 6 lines, it's not valid (skip it)
            continue

        # Build a dictionary for the question and its options
        file_question = {
            "file_question": lines_in_block[0][len("Question: "):], # Extract question text
            "option_a": lines_in_block[1][3:], # Extract option a
            "option_b": lines_in_block[2][3:], # Extract option b
            "option_c": lines_in_block[3][3:], # Extract option c
            "option_d": lines_in_block[4][3:], # Extract option d
            "correct_answer": lines_in_block[5][-1].lower() # Get correct option letter
        }
        quiz_questions.append(file_question)  # Add the parsed question to the list
    return quiz_questions  # Return the full list of questions

# Function to print the stylized game title using ASCII art
def print_title():
    fig = Figlet(font='bulbhead') # Use the "bulbhead" font
    quiz = fig.renderText('Quiz').splitlines() # Render "Quiz" as ASCII
    game = fig.renderText('Game').splitlines() # Render "Game" as ASCII
    for quiz_line, game_line in zip(quiz, game): # Merge and print lines side-by-side
        print(Fore.MAGENTA + quiz_line + "  " + Fore.CYAN + game_line) # Colored output
    print(Style.RESET_ALL) # Reset styles

# Function to display the main menu and handle choices
def main_menu():
    while True: # Infinite loop until user exits
        print_title()  # Show game title
        # Show game description
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +  "💡 Welcome to the Quiz Game!")
        print(Fore.LIGHTWHITE_EX + "📚 Test your general knowledge and see how high you can score!")

        # Display menu options
        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do?")
        print("1️⃣ Play")
        print("2️⃣ Check High Scores")
        print("3️⃣ Exit")

        # Get user input
        user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your option (1/2/3): ")

        # Check the user's choice using if-else logic and call the appropriate function
        if user_choice == "1":
            quiz_game_start() # Calls the function to let user play the game
        elif user_choice == "2":
            high_score_view() # Calls the function to allow user to check the high scores
        elif user_choice == "3":
            print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!") # Exit message
            sys.exit() # Breaks the loop and ends the program
        else:
            print(Fore.RED +"❌ Invalid input! Please choose between 1, 2, and 3 only.\n") # Display an error message once user input is invalid

# Function to start the quiz game, prompt for name and begin
def quiz_game_start():
    print() # Print newline for space
    print_title() # Show title again
    print(Fore.LIGHTGREEN_EX + "🎮 Starting Quiz Game...\n") # Show description of the game

    # Display the rules of the game
    print(Fore.LIGHTBLUE_EX + "📜 Rules:")
    print("✅ The game consists of 25 general knowledge questions.")
    print("❌ Once you reach 5 mistakes, the game is over.")
    print("🎯 Good luck and enjoy!")

    # Ask for the player's name
    player_name = input(Fore.YELLOW + Style.BRIGHT + "\n✍️ Enter your name: ")
    if not player_name: # Prevent empty name
        print(Fore.RED + "⚠️ Name cannot be empty.") # Prints message that provide name is empty
        return

    # Display a welcome message to the player
    print(f"\n👋 Welcome, {Fore.LIGHTYELLOW_EX + player_name}{Fore.RESET}! Let's begin!")

    # Prompt to begin the game
    enter_game = input(f'🔑 Type {Fore.LIGHTGREEN_EX}"GO" {Fore.RESET}to start the game: ')

    # If the player types "GO", start playing
    if enter_game == "GO":
        quiz_game_play(player_name) # Calls the function that allows the player to start the quiz
    else:
        print(Fore.RED + '❌ Invalid input. Type "GO" only.') # Display error if the input is invalid
        quiz_game_start() # Restart prompt

# Function to play the quiz with scoring and mistakes
def quiz_game_play(player_name):
    questions_list = load_questions() # Load all questions from file
    if not questions_list: # If no questions, exit function
        return

    random.shuffle(questions_list) # Shuffle questions using the random module
    current_score = 0 # Track correct answers
    incorrect_attempts = 0 # Track wrong answers
    max_allowed_incorrect = 5 # Game ends after 5 wrong answers
    question_log = [] # For storing player's answers

    # Loop over each question
    for current_question in questions_list:
        if incorrect_attempts >= max_allowed_incorrect:
            break # Stop if there are a record of 5 mistakes

        # Show score and mistake count
        print(Fore.LIGHTBLACK_EX + f"\n⭐ Score: {current_score} | ❌ Mistakes: {incorrect_attempts}/{max_allowed_incorrect}")
        # Show question and options
        print(Fore.LIGHTYELLOW_EX+ f"\nQuestion: {current_question["file_question"]}")
        print(f"a) {current_question["option_a"]}")
        print(f"b) {current_question["option_b"]}")
        print(f"c) {current_question["option_c"]}")
        print(f"d) {current_question["option_d"]}")

        # Input validation using while loop
        while True:
            player_answer = input(Fore.LIGHTWHITE_EX + "Your answer (a/b/c/d): ").strip() # Prompt user for input

            if player_answer.isupper(): # Check if input is in uppercase, which is not allowed
                print(Fore.RED + "⚠️ Capital letters are not allowed. Please use lowercase only (a/b/c/d).")
                continue # Ask user again to input answer
            if player_answer in ['a', 'b', 'c', 'd']: # Check if input is one of the allowed options
                break # Exit the loop if input is valid
            print(Fore.RED + "⚠️ Please enter a valid option (a/b/c/d).") # Inform the user about invalid input

        # Check if the user's answer is correct
        if player_answer == current_question["correct_answer"]:
            print(Fore.GREEN + "✅ Correct!") # Display message if answer is correct
            current_score += 1 # Increment score if correct
        else:
            print(Fore.RED + f"❌ Wrong! Correct answer was: {current_question["correct_answer"]}") # Display correct answer if user input is wrong
            incorrect_attempts += 1 # Increment incorrect attempts

        # Store the question, the user's answer, and the correct answer for review
        question_log.append((current_question["file_question"], player_answer, current_question["correct_answer"]))

    # Check the user's score using if-else logic and print a game over or congratulatory message
    if current_score == len(questions_list):
        print(Fore.LIGHTCYAN_EX + f"\nFinal Score: {current_score}") # Show the player's final score
        print(Fore.GREEN + "🎉 Congratulations! You got a perfect score! 🎉") # Display congratulations message
    else:
        print(Fore.RED + "\n🛑 GAME OVER 🛑") # Display game over message
        print(Fore.LIGHTCYAN_EX + f"\nFinal Score: {current_score}") # Show the player's final score

    # Save the score with the player's name in the high_scores.txt file
    save_high_score(player_name, current_score)

    # Display a menu after game ends to let user choose what to do next
    while True:
        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do next?")
        print("🕹️ 1. Play Again")
        print("📄 2. View Answer Key")
        print("🏠 3. Main Menu")
        print("🚪 4. Exit")

        # Get user input
        game_choice = input(Fore.LIGHTWHITE_EX + "Choose an option: ")

        # Check the user's choice using if-else logic and call the appropriate function
        if game_choice == "1":
            quiz_game_play(player_name) # Calls the function and replay the game with the same name
        elif game_choice == "2":
            view_answer_key(question_log) # Calls the function and view the history of the player's game
            menu_exit_choice() # Calls the function to ask user to directly exit or go back to the main menu
        elif game_choice == "3":
            main_menu() # Calls the function and returns to main menu
        elif game_choice == "4":
            print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!") # Exit message
            break # Breaks the loop and ends the program
        else:
            print(Fore.RED + "❌ Invalid input! Please choose between 1, 2, 3, and 4 only.\n") # Display an error message once user input is invalid

# Function to display the answer key after a game session
def view_answer_key(history):
    print(Fore.LIGHTBLUE_EX + "\n📘 Answer Key")
    for i, (question, given, correct) in enumerate(history, 1):
        print(Fore.LIGHTYELLOW_EX + f"{i}. {question}")
        print(f"Your Answer: {given}")
        print(f"Correct Answer: {correct}\n")

# Function to save the player's name and score to the high score file
def save_high_score(player_name, current_score):
    with open(high_score_file, "a") as file:
        file.write(f"{player_name}: {current_score}\n")

# Function to view the high scores
def high_score_view():
    if not os.path.exists(high_score_file): # Check if the high score file exists
        print(Fore.YELLOW + "⚠️ No high scores yet.") # Display a warning message if no high scores exist
        return

    print() # Print a blank line for space
    print_title()  # Call the function to print the game title
    print(Fore.LIGHTGREEN_EX + "🏆 High Scores 🏆") # Print the heading for the high scores in green

    # Initialize an empty list to store player scores and names
    scores = []
    with open(high_score_file, "r") as file: # Open the high score file in read mode to display the stored scores
        for name_line in file: # Loop through each line in the file
            player_name, player_score = name_line.strip().rsplit(":", 1) # Split each line into player name and score
            scores.append((int(player_score), player_name)) # Append the score and name as a tuple to the scores list

    # Sort the list of scores in descending order (highest to lowest)
    scores.sort(reverse = True)

    # Loop through the sorted list
    for score, name in scores:
        print(f"{name}: {score}") # Display each name with their corresponding score

    menu_exit_choice() # Calls the function to display the exit menu options

# Function for user choice if they want to exit or return to the menu
def menu_exit_choice():
    menu_choice = input(Fore.LIGHTWHITE_EX + "\n⇄ Would you like to go back to the menu? (yes/no): ") # Ask if user wants to exit or return
    if menu_choice.lower() == "yes": # Return to the menu once user answer is 'yes'
        print()
        main_menu()
    elif menu_choice.lower() == "no": # Exit and break the program once user answer is 'no'
        print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!") # Display exit message
        sys.exit() # Use to officially exit the program
    else:
        print(Fore.RED + "❗ Invalid choice! Returning to main menu.") # Display error message once user input is invalid
        return # Returns to main menu

main_menu() # Start the main menu function