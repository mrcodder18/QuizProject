import tkinter as tk
from tkinter import messagebox
import random

questions = [
    ("What is the output of 2 + 2?", ["3", "4", "5", "6"], "4"),
    ("Which of the following is a valid Python data type?", ["int", "str", "list", "all of the above"], "all of the above"),
    ("What is the correct way to declare a variable in Python?", ["int x = 10", "x = 10", "10 = x", "variable x = 10"], "x = 10"),
    ("Which of these is used to define a function in Python?", ["def", "function", "method", "lambda"], "def"),
    ("What does the 'len()' function do?", ["Returns the length of an object", "Returns the size of an object", "Returns the type of an object", "None of the above"], "Returns the length of an object"),
    ("Which of the following data structures is mutable?", ["List", "Tuple", "String", "All of the above"], "List"),
    ("What will be the output of `print(2 ** 3)`?", ["8", "6", "9", "4"], "8"),
    ("Which keyword is used to create a class in Python?", ["class", "def", "object", "type"], "class"),
    ("How do you insert a comment in Python?", ["# comment", "// comment", "/* comment */", "//"], "# comment"),
    ("Which of the following is not a valid variable name in Python?", ["my_var", "var1", "1st_var", "_var"], "1st_var"),
    ("How do you check if a variable is an integer?", ["is_integer()", "type(x) == int", "x.is_integer()", "x == int"], "type(x) == int"),
    ("What is the keyword used to exit a loop in Python?", ["exit", "break", "continue", "stop"], "break"),
    ("Which of these is an immutable data type?", ["List", "Tuple", "Set", "Dictionary"], "Tuple"),
    ("Which of the following is used to handle exceptions in Python?", ["try-except", "if-else", "catch-finally", "while-except"], "try-except"),
    ("Which method can be used to convert a string into a list?", ["split()", "convert()", "to_list()", "list()"], "split()"),
    ("What does `range(5)` produce?", ["[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4, 5]", "Error"], "[0, 1, 2, 3, 4]"),
    ("What is the default value of `sep` in the `print()` function?", ["' '", "None", "''", "Tab"], "' '"),
    ("Which of the following methods removes the last item from a list?", ["remove()", "pop()", "delete()", "clear()"], "pop()"),
    ("What is the correct syntax to create a set?", ["set = {}", "set()", "set([])", "[]"], "set()"),
    ("Which of the following is a built-in function in Python?", ["int()", "input()", "max()", "All of the above"], "All of the above"),
    ("What does the `map()` function do?", ["Applies a function to all items in an input list", "Maps one list to another", "Loops through a list", "Filters a list"], "Applies a function to all items in an input list"),
    ("What is the result of `10 / 2` in Python?", ["5", "5.0", "10.0", "2"], "5.0"),
    ("Which operator is used to compare two values?", ["=", "==", "<>", "is"], "=="),
    ("What will the following code output: `print('Hello'.upper())`?", ["hello", "HELLO", "hello()", "HELLO()"], "HELLO"),
    ("How would you create an empty dictionary?", ["{}", "[]", "()", "dict()"], "dict()"),
    ("Which of the following statements is correct about Python classes?", ["Classes are blueprints for creating objects", "Classes are objects", "Classes are functions", "None of the above"], "Classes are blueprints for creating objects"),
    ("Which module is used to generate random numbers in Python?", ["math", "random", "statistics", "time"], "random"),
    ("What does `self` refer to in Python class methods?", ["The class", "The instance of the class", "The method", "The variable"], "The instance of the class"),
    ("Which function is used to read input from the user in Python?", ["input()", "read()", "scan()", "get()"], "input()"),
    ("What is the correct way to handle multiple exceptions in one block?", ["try-except-else", "try-except-finally", "try-except-except", "try-except as"], "try-except-finally"),
    ("What is the purpose of the `continue` statement?", ["It stops the loop", "It skips the current iteration and moves to the next one", "It exits the loop", "None of the above"], "It skips the current iteration and moves to the next one"),
    ("What does the `zip()` function do?", ["Merges two lists", "Swaps elements in a list", "Creates a tuple from two lists", "None of the above"], "Creates a tuple from two lists"),
    ("What will the following code output: `print(type([]))`?", ["<class 'list'>", "<type 'list'>", "<class 'tuple'>", "<type 'tuple'>"], "<class 'list'>"),
    ("Which operator is used to raise a number to a power in Python?", ["**", "*", "^", "//"], "**"),
    ("Which of the following is not a valid loop in Python?", ["for", "while", "until", "None of the above"], "until"),
    ("What does the `sorted()` function do?", ["Sorts a list", "Returns a sorted list", "Sorts in place", "None of the above"], "Returns a sorted list"),
    ("Which of these is used for memory management in Python?", ["Garbage Collection", "Manual Management", "Automatic Memory Management", "None of the above"], "Garbage Collection"),
    ("Which of the following is used to convert a string to lowercase?", ["to_lower()", "lower()", "convert()", "case()"], "lower()"),
    ("What will the following code output: `print(5 > 3)`?", ["True", "False", "None", "Error"], "True"),
    ("What is the default return value of a Python function that does not return anything?", ["None", "0", "False", "Empty"], "None"),
    ("Which of these is used to define a block of code in Python?", ["Indentation", "Brackets", "Parentheses", "Curly Braces"], "Indentation"),
    ("What does `os.path.join()` do?", ["Joins two file paths", "Returns the absolute path", "Splits a file path", "None of the above"], "Joins two file paths"),
    ("How can you prevent a variable from being modified in Python?", ["By using `const` keyword", "By using `final` keyword", "By using `immutable` keyword", "Python has no such mechanism"], "Python has no such mechanism"),
    ("What is the purpose of `assert` in Python?", ["To check if a condition is true", "To raise an exception", "To test code", "None of the above"], "To check if a condition is true"),
    ("What does `repr()` do in Python?", ["Converts an object to a string", "Converts an object to a readable string", "Evaluates the object", "Returns an object description"], "Converts an object to a readable string"),
    ("Which of the following operators is used for floor division?", ["/", "//", "%", "div"], "//"),
    ("What is a Python lambda function?", ["A simple function", "An anonymous function", "A function with multiple arguments", "None of the above"], "An anonymous function"),
    ("What is the output of `len([1, 2, 3])`?", ["3", "6", "2", "None"], "3"),
    ("How would you remove an item from a set?", ["remove()", "pop()", "delete()", "clear()"], "remove()"),
    ("What will be the result of `x == 10 and x != 10`?", ["True", "False", "Error", "None"], "False"),
    ("What is the default type of a variable in Python?", ["int", "str", "float", "None"], "None"),
    ("Which of the following function is used to get the length of a string?", ["len()", "length()", "size()", "count()"], "len()")
] 

# Select 10 random questions
random.shuffle(questions)
selected_questions = questions[:10]

# Save the selected questions and answers to a file
with open("quiz_questions.txt", "w") as file:
    for i, (question, options, correct_answer) in enumerate(selected_questions):
        file.write(f"Q{i+1}: {question}\n")
        for opt in options:
            file.write(f" - {opt}\n")
        file.write(f"Answer: {correct_answer}\n\n")

# Initialize global variables
current_question = 0
score = 0

# Create the main window
window = tk.Tk()
window.title("Python Quiz")
window.geometry("600x500")
window.config(bg="#f0f0f0")  # Set background color to light gray

def next_question():
    """Load the next question."""
    global current_question
    global score
    
    if current_question >= len(selected_questions):
        messagebox.showinfo("Quiz Over", f"Your final score is {score} out of {len(selected_questions)}")
        window.quit()
        return

    # Get the current question and options
    question, options, correct_answer = selected_questions[current_question]
    
    # Update the question label and radio buttons
    question_label.config(text=question)
    for i, option in enumerate(options):
        option_buttons[i].config(text=option, value=option)

    # Move to the next question
    current_question += 1

def check_answer(selected_answer):
    """Check the selected answer."""
    global score
    
    # Get the correct answer for the current question
    question, options, correct_answer = selected_questions[current_question - 1]
    
    # Update score if the answer is correct
    if selected_answer == correct_answer:
        score += 1
    
    # Move to the next question
    next_question()

# Create UI components
question_frame = tk.Frame(window, bg="#f0f0f0")
question_frame.pack(pady=30, padx=40, fill='both')

question_label = tk.Label(question_frame, text="", font=("Arial", 16, "bold"), wraplength=500, bg="#f0f0f0", justify="center")
question_label.pack(pady=10)

options_frame = tk.Frame(window, bg="#f0f0f0")
options_frame.pack(pady=10, padx=40, fill='both')

option_var = tk.StringVar()

option_buttons = []
for i in range(4):
    rb = tk.Radiobutton(options_frame, text="", font=("Arial", 12), variable=option_var, value="", 
                        command=lambda: check_answer(option_var.get()), 
                        indicatoron=0, width=30, anchor="w", padx=10, pady=5, 
                        relief="flat", selectcolor="#5cb85c", bg="#ffffff", fg="#333333")
    rb.pack(anchor="w", pady=5)
    option_buttons.append(rb)

next_button = tk.Button(window, text="Next", font=("Arial", 14, "bold"), bg="#007bff", fg="white", relief="flat", 
                        width=15, height=2, command=next_question)
next_button.pack(pady=20)

# Start the quiz by loading the first question
next_question()

# Run the Tkinter main loop
window.mainloop()
