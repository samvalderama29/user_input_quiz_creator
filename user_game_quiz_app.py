import random
import os
from colorama import init, Fore, Style
from pyfiglet import Figlet

init(autoreset = True)

questions_file = "quiz_creator.txt"

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

def main_menu():
    print("1. Play")
    print("2. Check High Scores")
    print("3. Exit")

    user_choice = input("Enter your option: ")

    if user_choice == "1":
        quiz_game_start()
        pass
    elif user_choice == "2":
        high_score_view()
        pass
    elif user_choice == "3":
        menu_exit()
        pass

def quiz_game_start():
    print("\nQuiz Game\n")
    player_name = input("Enter your name: ")
    if not player_name:
        print("Name cannot be empty")
        return

    print(f"\nWelcome, {player_name}! Let's begin!")

    enter_game = input('Type "GO" to start the game')

    if enter_game == "GO"
        quiz_game_play()
        pass
    else:
        print('Invalid input. Type "GO" only')
        pass

main_menu()