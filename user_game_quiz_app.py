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

if __name__ == "__main__":
    list_questions = load_questions()
    print("Loaded Questions:")
    for i, question in enumerate(list_questions, 1):
        print(f"Question {i}: {question["file_question"]}")
        print(f"a) {question["option_a"]}")
        print(f"b) {question["option_b"]}")
        print(f"c) {question["option_c"]}")
        print(f"d) {question["option_d"]}")
        print(f"Correct Answer: {question["correct_answer"]}")
        print()