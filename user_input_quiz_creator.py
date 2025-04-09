# Import necessary modules
import sys # For system parameters, use for exit functionality
from colorama import init, Fore, Style # For colored text in the terminal
init(autoreset = True) # Initialize colorama with auto reset to ensure that colors are reset after each print
import os.path # Use to interact with system's file path

def main_menu(): # Function to present a menu for user to choose
    while True:
        # Print the main menu options with colors
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n📚 Welcome to the Quiz Creator!") # Welcome message
        print(Fore.LIGHTWHITE_EX + "💡 This program allows you to create questions and input answer to make a quiz!") # Description of program
        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do?") # Prompt asking user what they want to do
        # Display menu choices
        print(f"{Fore.GREEN}1. {Fore.RESET}Add a question")
        print(f"{Fore.CYAN}2. {Fore.RESET}Remove a question")
        print("3. View all questions")
        print(f"{Fore.RED}4. {Fore.RESET}Exit")

        # Take user input for their choices
        user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice (1/2/3/4): ")

        # Check the user's choice using if-else logic and call the appropriate function
        if user_choice == "1":
            add_new_question() # Calls the function to add new question
        elif user_choice == "2":
            remove_question() # Calls the function to remove a specific question
        elif user_choice == "3":
            view_all_questions() # Calls the function to view all questions
        elif user_choice == "4":
            print(Fore.CYAN + Style.BRIGHT + "\n👋🏽 Goodbye! Thank you. Quiz Creator closed.") # Exit message
            break # Breaks the loop and ends the program
        else:
            print(Fore.RED +"\n❌ Invalid input! Please choose between 1, 2, 3, and 4 only.") # Displays an error message once user input is invalid

def add_new_question(): # Function to add new question to the quiz
    quiz_file = "quiz_creator.txt" # Define the file name to store user input

    print(Fore.GREEN + Style.BRIGHT + "\n✏️ Enter a new quiz question:") # Prompt for the question

    with open(quiz_file, "a") as file: # Open the quiz file in append mode 'a' to add new questions
        # Take input from the user for the question, choices, correct answer, and store in a variable
        user_question = input("Question: ")
        choice_a = input("Enter choice a: ")
        choice_b = input("Enter choice b: ")
        choice_c = input("Enter choice c: ")
        choice_d = input("Enter choice d: ")
        correct_answer = input("Correct answer (a/b/c/d): ").lower()

        # Validate if the input for final answer is correct
        if correct_answer not in ["a", "b", "c", "d"]:
            print(Fore.RED +"❌ Invalid input! Please choose between a, b, c, and d only.")

        # Write the question and choice to the file (.txt) in an organized manner
        file.write(f"Question: {user_question}\n")
        file.write(f"a) {choice_a}\n")
        file.write(f"b) {choice_b}\n")
        file.write(f"c) {choice_c}\n")
        file.write(f"d) {choice_d}\n")
        file.write(f"Correct answer: {correct_answer}\n")
        file.write("-----\n") # Use to separate questions with -----

        # Ask if the user wants to add another question
        another_question = input(Fore.CYAN + "\nDo you want to add another question? (yes/no): ")

        # Use if-else logic to ask for user choice
        if another_question.lower() != "yes": # Presents message for cancel and confirmation once user answers 'no'
            print(Fore.RED + "\n❎ Adding questions cancelled.")
            print(Fore.GREEN + "✅ Questions saved successfully!")
            menu_exit_choice()
        else: # Present a new list by calling the function for user to input new question
            add_new_question()

def remove_question(): # Function to remove a question to the quiz
    quiz_file = "quiz_creator.txt" # Define the file name where user input is stored

    print(Fore.GREEN + Style.BRIGHT + "\n🗑️ Remove a quiz question") # Prompt for removing a question

    if not os.path.exists(quiz_file): # Check if the file exists
        print(Fore.RED + "\n❗ No file found to exists") # Display message error once file is not found

    with open(quiz_file, "r") as file: # Open the quiz file (.txt) in read mode 'r'
        quiz_creator_file = file.read() # Read the entire content of the file

    user_stored_questions = quiz_creator_file.strip().split("-----\n") # Split the file into separate questions

    if not user_stored_questions: # Check if the file has questions
        print(Fore.RED + "\n❗ No questions found to exists") # Displays error message if no question exist

    # Print all stored question for the user to choose which one to delete
    print(Fore.LIGHTWHITE_EX + "List of Questions:")
    for i, question in enumerate(user_stored_questions):
        first_line = question.splitlines()[0].replace("Question: ", " ") if question else "[Empty]"
        print(Fore.YELLOW + f"[{i}]{first_line}") # Get first line of question and display each with index to identify through numbers

    # Use try-except logic to easily identify if user input is valid
    try:
        index = int(input(Fore.LIGHTWHITE_EX + "Enter the number of the question you want to remove: ")) # Ask user which question they want to delete
        if 0 <= index < len(user_stored_questions): # Check if the index is valid
            confirm_remove = input(Fore.BLUE + "\nAre you sure you want to delete this question? (yes/no): ") # Display message asking for user confirmation
            if confirm_remove.lower() == "yes":
                del user_stored_questions[index] # Remove the selected question using del function
                with open(quiz_file, "w") as file: # Open the file and rewrite 'w' with the remaining question that are not removed
                    for i, question in enumerate(user_stored_questions):
                        file.write(question.strip() + "\n") # Write each question back to the file
                        if i < len(user_stored_questions) - 1:
                            file.write("-----\n") # Use to separate questions
                print(Fore.GREEN + "✅ Question successfully removed!") # Displays confirmation message once question is finally removed
            else:
                print(Fore.LIGHTRED_EX + "❎ Deletion cancelled") # Displays message once deletion is cancelled
        else:
            print(f"❌ Invalid input. Please enter a number between 0 and {len(user_stored_questions) - 1}") # Display invalid message and shows instructions with index
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.") # Displays error if user input is not a number

    menu_exit_choice() # Calls the function to ask the user if they want to exit or return to menu

def view_all_questions(): # Function to view all question stored in the file
    quiz_file = "quiz_creator.txt" # Define the file name where user input is stored

    print(Fore.GREEN + Style.BRIGHT + "\n📝 View all questions") # Prompt to view all questions
    print(Fore.LIGHTWHITE_EX + "List of Questions:")

    with open(quiz_file, "r") as file: # Open the file name in read mode 'r'
        print(file.read()) # Print all the contents of the quiz file

    if not os.path.exists(quiz_file): # Check if the file exists
        print(Fore.RED + "❗ No file found to exists") # Display error message if file does not exist

    menu_exit_choice() # Calls the function to ask the user if they want to exit or return to menu

def menu_exit_choice(): # Function for user choice if they want to exit or return to the menu
    menu_choice = input(Fore.LIGHTWHITE_EX + "\nWould you like to go back to the menu? (yes/no): ") # Ask if user wants to exit or return
    if menu_choice.lower() == "yes":  # Return to the menu once user answer is 'yes'
        return
    elif menu_choice.lower() == "no": # Exit and break the program once user answer is 'no'
        print(Fore.CYAN + Style.BRIGHT + "\n👋🏽 Goodbye! Thank you. Quiz Creator closed.") # Displays exit message
        sys.exit() # Use to officially exit the program
    else:
        print(Fore.RED + "❗ Invalid choice! Returning to main menu.") # Display error message once user input is invalid
        return # Returns to main menu

main_menu() # Start the main menu function