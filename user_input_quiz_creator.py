from colorama import init, Fore, Style
init()
import os.path

def main_menu()
    while True:
        print("Welcome to the Quiz Creator!")
        print("This program allows you to create questions and input answer to make a quiz!")
        print("What would you like to do?")
        print("1. Add a new question")
        print("2. Remove a question")
        print("3. View all questions")
        print("4. Exit")

        user_choice = input("Enter your choice (1/2/3/4): ")