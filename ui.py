from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=40, bg=THEME_COLOR)
        self.window.title("Trivia Game")
        self.canvas = Canvas(width=400, height=526)
        self.text_bg = self.canvas.create_rectangle(0, 100, 400, 400, fill="white")
        false_image = PhotoImage(file="./images/false.png")
        false_button = Button(image=false_image,highlightthickness=0)
        false_button.grid(row=1, column=0, columnspan=1)
        true_image = PhotoImage(file="./images/true.png")
        true_button = Button(image=true_image, highlightthickness=0, command=self.its_true)
        true_button.grid(row=1, column=1, columnspan=1)
        self.canvas.config(bg=THEME_COLOR, highlightthickness=0)
        self.question_title = self.canvas.create_text(175, 250, text="Some Question Text", font=("Ariel", 20, "italic"), fill=THEME_COLOR, width=300)
        self.score_text = self.canvas.create_text(200, 50, text="Score: 0", font=("Ariel", 20, "bold"), fill="white")
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.itemconfig(self.text_bg, fill="white")
        self.canvas.itemconfig(self.question_title, fill=THEME_COLOR)
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_title, text=question)
    def its_true(self):
        if self.quiz.check_answer("True"):
            self.correct_ui()
        else:
            self.wrong_ui()
        self.update_score()
    def its_false(self):
        if self.quiz.check_answer("False"):
            self.correct_ui()
        else:
            self.wrong_ui()
        self.update_score()
    def correct_ui(self):
        self.canvas.itemconfig(self.text_bg, fill="Green")
        self.canvas.itemconfig(self.question_title, fill="white")
        self.window.after(1000, self.get_next_question)
    def wrong_ui(self):
        self.canvas.itemconfig(self.text_bg, fill="Red")
        self.canvas.itemconfig(self.question_title, fill="white")
        self.window.after(1000, self.get_next_question)
    def update_score(self):
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.quiz.score}")