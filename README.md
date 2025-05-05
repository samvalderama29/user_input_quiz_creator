# 🧠 Quiz System (Creator + Game)


A simple Python-based quiz system that includes:


* 🛠️ **Quiz Creator**: For adding, viewing, and removing quiz questions.
* 🎮 **Quiz Game**: An interactive quiz game with scoring, high score tracking, and answer key.


It uses the `colorama` and `pyfiglet` libraries to make the command-line experience more interactive.


---


## 📦 Features


### 🛠️ Quiz Creator


* Allow the user to create new quiz questions with four choices (a, b, c, d) and a correct answer
* View all stored questions in a clean format
* Delete specific questions by selecting their number
* Stores all data in a plain text file (`quiz_creator.txt`)
* Stylish code using `colorama`


### 🎮 Quiz Game


* Play through 25 general knowledge questions *(users can add more questions using `user_input_quiz_creator.py`)*
* End the game after 5 incorrect answers
* Tracks and displays your final score
* Saves and shows a sorted high score list (`high_scores.txt`)
* Includes an answer key for post-game review
* Displays the top scorer
* Stylish ASCII titles using `pyfiglet`


---


## 🚀 How to Run


1. **Install Python (if not already installed):**
  [https://www.python.org/downloads/](https://www.python.org/downloads/)


2. **Install required packages:**


```bash
pip install colorama pyfiglet
```


3. **Run the app:**


* **Quiz Creator:**


```bash
python quiz_creator.py
```


* **Quiz Game:**


```bash
python quiz_game.py
```


---


## 📁 File Structure


```
user_input_quiz_creator.py        # Tool to manage (add/view/delete) quiz questions
user_quiz_game_app.py             # The main game logic with scoring and high score tracking
quiz_creator.txt                  # Stores all the quiz questions in formatted blocks
high_scores.txt                   # Stores the names and scores of players
README.md                         # This file

