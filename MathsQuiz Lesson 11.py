#Luan Mangels, 3 Mar 21

from tkinter import*
from tkinter import ttk
from random import*

#Parent class
class MathsQuiz:
    def __init__(self,parent):

        '''Widgets for Welcome Frame'''

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.TitleLabel = Label(self.Welcome, text ="Welcome to Maths Quiz",
                                bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.TitleLabel.grid(columnspan = 2) #Label spans over two columns

        #Name and Age Labels
        self.NameLabel = Label(self.Welcome, text = "Name", anchor = W,
                                fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)

        self.AgeLabel = Label(self.Welcome, text = "Age", anchor = W,
                                fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.AgeLabel.grid(row = 3, column = 0)

        #Name and Age Entry
        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row = 2, column = 1)

        self.AgeEntry = ttk.Entry(self.Welcome, width =20)
        self.AgeEntry.grid(row = 3, column = 1)

        #Warning, Difficulty level label and radio buttons

        self.WarningLabel = Label(self.Welcome, text = "", anchor = W,
                                fg = "red", width = 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row = 4, columnspan = 2)

        self.DifficultyLabel = Label(self.Welcome, text = "Choose Difficulty Level", anchor = W,
                                    fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.DifficultyLabel.grid(row = 5, column = 0)

        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar() #Use StringVar() for text in list and IntVar() for numbers in list
        self.diff_lvl.set(0) #.set is used so that when the radio buttons appear it is automatically set to the easy difficulty.
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            self.rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i],
                            anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(self.rb)
            self.rb.grid(row = i+6, column = 0, sticky = W)

        self.NextButton = Button(self.Welcome, text = 'Next', command = self.show_Questions) #ttk prefit gives modern Button
        self.NextButton.grid(row = 8, column = 1)


        '''Widgets for Questions Frame'''

        self.index = 0
        self.score = 0

        self.Questions = Frame(parent)
        #self.Questions.grid(row = 0, column = 1)
        '''update QuestionsLabel configure method to print question number'''
        self.QuestionsLabel = Label(self.Questions, text = "",
                                bg = "black", fg = "white", width = 20, padx =30, pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.QuestionsLabel.grid(columnspan = 3)

        self.Problems = Label(self.Questions, text = "")
        self.Problems.grid(row = 1, column = 0)

        self.AnswerEntry = ttk.Entry(self.Questions, width = 20)
        self.AnswerEntry.grid(row = 1, column = 1)
        #Create ScoreLabel to display Score 
        self.ScoreLabel = Label(self.Questions, text = "")
        self.ScoreLabel.grid(row = 1, column = 2)

        self.feedback = Label(self.Questions, text = "")
        self.feedback.grid(row = 2, column = 0)

        self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 0)

        self.check_button = ttk.Button(self.Questions, text = 'Check Answer', command = self.check_answer)
        self.check_button.grid(row = 8, column = 1)

        self.next_button = ttk.Button(self.Questions, text = 'Next Question', command = self.next_question)   
        self.next_button.grid(row = 8,column = 2)

        '''A method that removes Questions Frame'''
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()
        
    def show_Questions(self):

        try:
#Error checking for empty or non-text user entries for name
            if self.NameEntry.get() == "":
                self.WarningLabel.configure(text = "Please enter a name")
                self.NameEntry.focus()

            elif self.NameEntry.get().isalpha() == False:
                self.WarningLabel.configure(text = "Please enter a name and age")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()
#Error checking for empty and age limit cases
            elif self.AgeEntry.get() =="":
                self.WarningLabel.configure(text = "Please enter your age")
                self.AgeEntry.focus()

            elif int (self.AgeEntry.get()) > 12:
                self.WarningLabel.configure(text = "You are to old!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int (self.AgeEntry.get()) < 0:
                self.WarningLabel.configure(text = "You are to old?")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            elif int (self.AgeEntry.get()) < 7:
                self.WarningLabel.configure(text = "You are to young!")
                self.AgeEntry.delete(0, END)
                self.AgeEntry.focus()

            else: #if all conditions are met, then show Questions frame
                self.Welcome.grid_remove()
                self.Questions.grid()

        except ValueError:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()


    def next_question(self):
        '''Creates questions, Stores answer'''
        x = randrange(10)
        y = randrange(10)
        self.answer = x + y
        self.index += 1 #keeps adding to index number

        question_text = str(x) + " + " + str(y) + " = "
        self.Problems.configure(text = question_text)
        #update QuestionsLabel with question number
        self.QuestionsLabel.configure(text = "Quiz Question" + str(self.index)+ "/5")
        #limit number questions to 5, then remove Questions frame and show Welcome frame
        if self.index >= 6:
            self.Questions.grid_remove()
            self.Welcome.grid()

    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct")
                self.score += 1 #add 
                score_text = "Score =" + str(self.score)
                self.ScoreLabel.configure(text = score_text)
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()
            
            else:
                self.feedback.configure(text = "Incorrect")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()

        except ValueError:
            self.feedback.configure(text = "Enter a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()


#Main routine
if __name__ == "__main__": #checks if condition - name of Parent class is main module
    root =Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop() #binds the above commands together

