#Luan Mangels, 12 Feb 21

from tkinter import *
from tkinter import ttk

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

        #Difficulty level label and radio buttons
        self.DifficultyLabel = Label(self.Welcome, text = "Choose Your Difficulty Level", anchor = W,
                                    fg = "black", width = 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.DifficultyLabel.grid(row = 4, column = 0)

        self.difficulty = ["Easy", "Medium", "Hard", 'Super Hard']
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0) #.set is used so that when the radio buttons appear it is automatically set to the easy difficulty.
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i],
                            anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+5, column = 0, sticky = W)

        self.NextButton = Button(self.Welcome, text = 'Next', command = self.show_Questions) #ttk prefit gives modern Button
        self.NextButton.grid(row = 8, column = 1)

        '''Widgets for Questions Frame'''

        self.Questions = Frame(parent)
        #self.Questions.grid(row = 0, column = 1)

        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                bg = "black", fg = "white", width = 20, padx =30, pady = 10,
                                font = ("Time", '14', "bold italic"))
        self.QuestionsLabel.grid(columnspan = 2)

        self.HomeButton = Button(self.Questions, text = 'Home', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 0)   

        '''A method that removes Questions Frame'''
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()
        
    def show_Questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()


#Main routine
if __name__ == "__main__": #checks if condition - name of Parent class is main module
    root =Tk()
    frames = MathsQuiz(root)
    root.title("Quiz")
    root.mainloop() #binds the above commands together


