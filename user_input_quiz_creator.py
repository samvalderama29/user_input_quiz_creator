import sys
from colorama import init, Fore, Style, Back
init(autoreset = True)
import os.path

def main_menu():
    while True:
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n📚 Welcome to the Quiz Creator!")
        print(Fore.LIGHTWHITE_EX + "💡 This program allows you to create questions and input answer to make a quiz!")
        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do?")
        print(f"{Fore.GREEN}1. {Fore.RESET}Add a question")
        print(f"{Fore.CYAN}2. {Fore.RESET}Remove a question")
        print("3. View all questions")
        print(f"{Fore.RED}4. {Fore.RESET}Exit")

        user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice (1/2/3/4): ")

        if user_choice == "1":
            add_new_question()
        elif user_choice == "2":
            remove_question()
        elif user_choice == "3":
            view_all_questions()
        elif user_choice == "4":
            print(Fore.CYAN + Style.BRIGHT + "\n👋🏽 Goodbye! Thank you. Quiz Creator closed.")
            break
        else:
            print(Fore.RED +"\n❌ Invalid input! Please choose between 1, 2, 3, and 4 only.")

def add_new_question():
    quiz_file = "quiz_creator.txt"

    print(Fore.GREEN + Style.BRIGHT + "\n✏️ Enter a new quiz question:")

    with open(quiz_file, "a") as file:
        user_question = input("Question: ")
        choice_a = input("Enter choice a: ")
        choice_b = input("Enter choice b: ")
        choice_c = input("Enter choice c: ")
        choice_d = input("Enter choice d: ")
        correct_answer = input("Correct answer (a/b/c/d): ").lower()

        if correct_answer not in ["a", "b", "c", "d"]:
            print(Fore.RED +"❌ Invalid input! Please choose between a, b, c, and d only.")

        file.write(f"Question: {user_question}\n")
        file.write(f"a) {choice_a}\n")
        file.write(f"b) {choice_b}\n")
        file.write(f"c) {choice_c}\n")
        file.write(f"d) {choice_d}\n")
        file.write(f"Correct answer: {correct_answer}\n")
        file.write("-----\n")

        another_question = input(Fore.CYAN + "\nDo you want to add another question? (yes/no): ")

        if another_question.lower() != "yes":
            print(Fore.RED + "\n❎ Adding questions cancelled.")
            print(Fore.GREEN + "✅ Questions saved successfully!")
            menu_exit_choice()
        else:
            add_new_question()

def remove_question():
    quiz_file = "quiz_creator.txt"

    print(Fore.GREEN + Style.BRIGHT + "\n🗑️ Remove a quiz question")

    if not os.path.exists(quiz_file):
        print(Fore.RED + "\n❗ No file found to exists")

    with open(quiz_file, "r") as file:
        quiz_creator_file = file.read()

    user_stored_questions = quiz_creator_file.strip().split("-----\n")

    if not user_stored_questions:
        print(Fore.RED + "\n❗ No questions found to exists")

    print(Fore.LIGHTWHITE_EX + "List of Questions:")
    for i, question in enumerate(user_stored_questions):
        first_line = question.splitlines()[0].replace("Question: ", " ") if question else "[Empty]"
        print(Fore.YELLOW + f"[{i}]{first_line}")

    try:
        index = int(input(Fore.LIGHTWHITE_EX + "Enter the number of the question you want to remove: "))
        if 0 <= index < len(user_stored_questions):
            confirm_remove = input(Fore.BLUE + "\nAre you sure you want to delete this question? (yes/no): ")
            if confirm_remove.lower() == "yes":
                del user_stored_questions[index]
                with open(quiz_file, "w") as file:
                    for i, question in enumerate(user_stored_questions):
                        file.write(question.strip())
                        if i < len(user_stored_questions) - 1:
                            file.write("-----\n")
                print(Fore.GREEN + "✅ Question successfully removed!")
            else:
                print(Fore.LIGHTRED_EX + "❎ Deletion cancelled")
        else:
            print(f"❌ Invalid input. Please enter a number between 0 and {len(user_stored_questions) - 1}")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

    menu_exit_choice()

def view_all_questions():
    quiz_file = "quiz_creator.txt"

    print(Fore.GREEN + Style.BRIGHT + "\n📝 View all questions")
    print(Fore.LIGHTWHITE_EX + "List of Questions:")

    with open(quiz_file, "r") as file:
        print(file.read())

    if not os.path.exists(quiz_file):
        print(Fore.RED + "❗ No file found to exists")

    menu_exit_choice()

def menu_exit_choice():
    menu_choice = input(Fore.LIGHTWHITE_EX + "\nWould you like to go back to the menu? (yes/no): ")
    if menu_choice.lower() == "yes":
        return
    elif menu_choice.lower() == "no":
        print(Fore.CYAN + Style.BRIGHT + "👋🏽 Goodbye! Thank you. Quiz Creator closed.")
        sys.exit()
    else:
        print("❗ Invalid choice! Returning to main menu.")
        return

main_menu()