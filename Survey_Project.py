#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):

        #   Make it look pretty
        

        self.frame_top = ttk.Frame(master)
        self.frame_top.pack()
        
        #   Add in image and title
        self.fig1 = PhotoImage(file = r'C:\Users\meert\OneDrive\Desktop\Final Project\tour_logo.gif')
        label = ttk.Label(self.frame_top, image = self.fig1).grid(row = 0, column = 0, rowspan = 2, sticky = 'sw')

        self.frame_middle = ttk.Frame(master)
        self.frame_middle.pack()
        
        #   Add questions and options for input
        nameQuestion = ttk.Label(self.frame_middle, text = 'Enter your name here:').grid(row = 2, column = 0, sticky = 'w')
        self.nameInput = ttk.Entry(self.frame_middle, width = 20)
        emailQuestion = ttk.Label(self.frame_middle, text = 'Enter your email here:').grid(row = 3, column = 0, sticky = 'w')
        self.emailInput = ttk.Entry(self.frame_middle, width = 20)
        commentsQuestion = ttk.Label(self.frame_middle, text = 'Enter your comments here:').grid(row = 4, column = 0, padx = 0, columnspan = 2, sticky = 'sw')
        self.commentsInput = Text(self.frame_middle, width = 50, height = 10)

        #   Display Entry Boxes
        self.nameInput.grid(row = 2, column = 1, sticky = 'sw')
        self.emailInput.grid(row = 3, column = 1, sticky = 'sw')
        self.commentsInput.grid(row = 5, column = 0, columnspan = 2)

        
        ## maybe input a few 1-5 ratings
        
        submitButton = ttk.Button(self.frame_middle, text = 'Submit', command = self.submitSurvey).grid(row = 6, column = 0)
        clearButton = ttk.Button(self.frame_middle, text = 'Clear', command = self.clearSurvey).grid(row = 6, column = 1)

    def submitSurvey(self):
        # Print contents to console
        print('Name: {}'.format(self.nameInput.get()))
        print('Email: {}'.format(self.emailInput.get()))
        print('Comments: {}'.format(self.commentsInput.get(1.0,'end')))
        # Pop-up notifing that comments were submitted
        messagebox.showinfo(title = 'Survey Submission Sucessful!', message = 'Thanks for completing this survey, we appreciate you taking the time to share your opinion!',wraplength = 50)
        # Empty contents of the input fields
        self.clearSurvey(trigger = 0)
            
    def clearSurvey(self,trigger = 1):
        # Empty contents of the input fields
        self.nameInput.delete(0,'end')
        self.emailInput.delete(0,'end')
        self.commentsInput.delete(1.0,'end')
        # Print cleared message to console if this is a user generated clear
        if (trigger == 1):
            print('All input fields cleared!')
            messagebox.showinfo(title = 'Survey Cleared!', message = 'Survey inputs cleared!')

        

            
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

    
if __name__ == "__main__":
    main()



###   Capabilities:
### a. Pressing submit will:
###   1.    Print contents of input fields to the console
###   2.    Empty content of input field
###   3.    Notify user that the comments were submitted
### b. Pressing clear will:
###   1.    Empty the input fields
### c.
