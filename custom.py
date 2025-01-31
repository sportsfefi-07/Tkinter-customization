import tkinter as tk
from tkinter import Toplevel, messagebox

######window settings######
window1 = tk.Tk()
window1.title("Window 1")
window1.geometry("400x400")
window1.configure(bg= "#C41E3A")
window1.iconbitmap("images/St._Louis_Cardinals_logo.ico")



######Sample Questions######

questions =  [
    {"question": "What is 2+2", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "What is the capital of Japan", "options": ["Beijing", "Seoul","Tokyo"], "answer": "4"},
    {"question": "What is Biggest city in the United States", "options": ["Chicago", "New York" "Los Angeles"], "answer": "New York"},
]


#Global Varibles

score = 0 #initalize player's score
question_index = 0 #initializing the question index

# function to open the window
def start_quiz():
    global question_index, score
    question_index=0 #resetting the question index
    score=0 #resetting the score
    open_quiz_window()
#tk.button.Top 
# function to open quiz window
def open_quiz_window():
    quiz_window = Toplevel(window1)
    quiz_window.title("Quiz")

    #fuction display the question and options
    def show_question():
        if question_index < len(questions): #if there are more still more quetions
            q = questions[question_index] #get the current question from the list
            question_label.config(text=q["question"]) #set the question label text
            for i, option in enumerate(q["question"]):
                buttons[i].config(text=option, command=lambda opt=option: check_answer(opt, quiz_window))# set the options text and command
            else:
                messagebox.showinfo("Quiz finished!", f"Your score is {score} / {len(questions)}")
                quiz_window.destroy() #close window when the quiz is finished
                update_scoreboard()

    def check_answer(selected_option, quiz_window):
        global question_index, score
        if selected_option == questions[question_index]["answer"]:
            score+=1 #increase the question index as we move forward
            show_question()

    question_label = tk.Label(quiz_window, text="", font=("Arial",14))
    question_label.pack(pady=10)
    buttons =  [tk.Button(quiz_window, text="", font=("Arial" , 12)) for i in range(3)]
    for btn in buttons:
        btn.pack(pady=5)
    show_question()

# Function to update scoreboard
def update_scoreboard():
    with open("scores.txt", "a") as f:
        f.write(f"Score: {score}/{len(questions)}\n")
# Function to view scoreboard
def view_scoreboard():
    scoreboard_window = tk.Toplevel(window1)
    scoreboard_window.title("Scoreboard")
    tk.Label(scoreboard_window, text="Score History", font=("Arial", 14)).pack()


# Main menu
windo1 = tk.Tk()
window1.title("Quiz App")

tk.Label(window1, text="Welcome to the Quiz!", font=("Arial", 16)).pack(pady=10)
tk.Button(window1, text="Start Quiz", command=start_quiz).pack(pady=5)
tk.Button(window1, text="View Scoreboard", command=view_scoreboard).pack(pady=5)


window1.mainloop()