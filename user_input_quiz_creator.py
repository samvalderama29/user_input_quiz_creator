from colorama import init, Fore, Style, Back
init(autoreset = True)
import os.path

def main_menu():
    while True:
        print(Fore.GREEN + Style.BRIGHT + "\nWelcome to the Quiz Creator!")
        print(Fore.LIGHTWHITE_EX + "This program allows you to create questions and input answer to make a quiz!")
        print(Fore.LIGHTWHITE_EX + "\nWhat would you like to do?")
        print("1. Add a new question")
        print("2. Remove a question")
        print("3. View all questions")
        print("4. Exit")

        user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice (1/2/3/4): ")

        if user_choice == "1":
            # add_new_question()
            pass
        elif user_choice == "2":
            # remove_question()
            pass
        elif user_choice == "3":
            # view_all_questions()
            pass
        elif user_choice == "4":
            print(Fore.CYAN + "Goodbye! Thank you. Quiz Creator closed.")
            break
        else:
            print(Fore.RED +"Invalid input! Please choose between 1, 2, 3, and 4 only.")

main_menu()