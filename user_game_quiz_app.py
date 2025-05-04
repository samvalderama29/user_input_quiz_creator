import sys
import random
import os
from colorama import init, Fore, Style
from pyfiglet import Figlet

init(autoreset = True)

questions_file = "quiz_creator.txt"
high_score_file = "high_scores.txt"

def load_questions():
    if not os.path.exists(questions_file):
        print("Quiz file not found")
        return[]

    with open(questions_file, "r") as quiz_file:
        question_blocks = quiz_file.read().split("-----\n")

    quiz_questions = []
    for question_block in question_blocks:
        lines_in_block = question_block.strip().splitlines()
        if len(lines_in_block) < 6:
            continue
        file_question = {
            "file_question": lines_in_block[0][len("Question: "):],
            "option_a": lines_in_block[1][3:],
            "option_b": lines_in_block[2][3:],
            "option_c": lines_in_block[3][3:],
            "option_d": lines_in_block[4][3:],
            "correct_answer": lines_in_block[5][-1].lower()
        }
        quiz_questions.append(file_question)
    return quiz_questions

def print_title():
    fig = Figlet(font='bulbhead')
    quiz = fig.renderText('Quiz').splitlines()
    game = fig.renderText('Game').splitlines()
    for q, g in zip(quiz, game):
        print(Fore.MAGENTA + q + "  " + Fore.CYAN + g)
    print(Style.RESET_ALL)

def main_menu():
    while True:
        print_title()
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +  "💡 Welcome to the Quiz Game!")
        print(Fore.LIGHTWHITE_EX + "📚 Test your general knowledge and see how high you can score!")

        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do?")
        print("1️⃣ Play")
        print("2️⃣ Check High Scores")
        print("3️⃣ Exit")

        user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your option (1/2/3): ")

        if user_choice == "1":
            quiz_game_start()
        elif user_choice == "2":
            high_score_view()
        elif user_choice == "3":
            print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!")
            sys.exit()
        else:
            print(Fore.RED +"❌ Invalid input! Please choose between 1, 2, and 3 only.\n")

def quiz_game_start():
    print()
    print_title()
    print(Fore.LIGHTGREEN_EX + "🎮 Starting Quiz Game...\n")
    print(Fore.LIGHTBLUE_EX + "📜 Rules:")
    print("✅ The game consists of 25 general knowledge questions.")
    print("❌ Once you reach 5 mistakes, the game is over.")
    print("🎯 Good luck and enjoy!")

    player_name = input(Fore.YELLOW + Style.BRIGHT + "\n✍️ Enter your name: ")
    if not player_name:
        print(Fore.RED + "⚠️ Name cannot be empty.")
        return

    print(f"\n👋 Welcome, {Fore.LIGHTYELLOW_EX + player_name}{Fore.RESET}! Let's begin!")

    enter_game = input(f'🔑 Type {Fore.LIGHTGREEN_EX}"GO" {Fore.RESET}to start the game: ')

    if enter_game == "GO":
        quiz_game_play(player_name)
    else:
        print(Fore.RED + '❌ Invalid input. Type "GO" only.')
        quiz_game_start()

def quiz_game_play(player_name):
    questions_list = load_questions()
    if not questions_list:
        return

    random.shuffle(questions_list)
    current_score = 0
    incorrect_attempts = 0
    max_allowed_incorrect = 5
    question_log = []

    for current_question in questions_list:
        if incorrect_attempts >= max_allowed_incorrect:
            break

        print(Fore.LIGHTBLACK_EX + f"\n⭐ Score: {current_score} | ❌ Mistakes: {incorrect_attempts}/{max_allowed_incorrect}")
        print(Fore.LIGHTYELLOW_EX+ f"\nQuestion: {current_question["file_question"]}")
        print(f"a) {current_question["option_a"]}")
        print(f"b) {current_question["option_b"]}")
        print(f"c) {current_question["option_c"]}")
        print(f"d) {current_question["option_d"]}")

        while True:
            player_answer = input(Fore.LIGHTWHITE_EX + "Your answer (a/b/c/d): ").strip()
            if player_answer.isupper():
                print(Fore.RED + "⚠️ Capital letters are not allowed. Please use lowercase only (a/b/c/d).")
                continue
            if player_answer in ['a', 'b', 'c', 'd']:
                break
            print(Fore.RED + "⚠️ Please enter a valid option (a/b/c/d).")

        if player_answer == current_question["correct_answer"]:
            print(Fore.GREEN + "✅ Correct!")
            current_score += 1
        else:
            print(Fore.RED + f"❌ Wrong! Correct answer was: {current_question["correct_answer"]}")
            incorrect_attempts += 1

        question_log.append((current_question["file_question"], player_answer, current_question["correct_answer"]))

    print(Fore.RED + "\n🛑 GAME OVER 🛑 ")
    print(Fore.LIGHTCYAN_EX + f"\nFinal Score: {current_score}")

    save_high_score(player_name, current_score)

    while True:
        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do next?")
        print("🕹️ 1. Play Again")
        print("📄 2. View Answer Key")
        print("🏠 3. Main Menu")
        print("🚪 4. Exit")

        game_choice = input(Fore.LIGHTWHITE_EX + "Choose an option: ")
        if game_choice == "1":
            quiz_game_play(player_name)
        elif game_choice == "2":
            view_answer_key(question_log)
            menu_exit_choice()
        elif game_choice == "3":
            main_menu()
        elif game_choice == "4":
            print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!")
            break
        else:
            print(Fore.RED + "❌ Invalid input! Please choose between 1, 2, 3, and 4 only.\n")

def view_answer_key(history):
    print(Fore.LIGHTBLUE_EX + "\n📘 Answer Key")
    for i, (question, given, correct) in enumerate(history, 1):
        print(Fore.LIGHTYELLOW_EX + f"{i}. {question}")
        print(f"Your Answer: {given}")
        print(f"Correct Answer: {correct}\n")

def save_high_score(player_name, current_score):
    with open(high_score_file, "a") as file:
        file.write(f"{player_name}: {current_score}\n")

def high_score_view():
    if not os.path.exists(high_score_file):
        print(Fore.YELLOW + "⚠️ No high scores yet.")
        return

    print(Fore.LIGHTGREEN_EX + "\n🏆 High Scores 🏆")
    with open(high_score_file, "r") as file:
        print(file.read())
        menu_exit_choice()

def menu_exit_choice():
    menu_choice = input(Fore.LIGHTWHITE_EX + "Would you like to go back to the menu? (yes/no): ")
    if menu_choice.lower() == "yes":
        print()
        main_menu()
    elif menu_choice.lower() == "no":
        print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!")
        sys.exit()
    else:
        print(Fore.RED + "❗ Invalid choice! Returning to main menu.")
        return

main_menu()