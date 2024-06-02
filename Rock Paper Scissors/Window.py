####################################################
#####   
##### Rock, Paper, Scissors 
#####     By Rhyan
#####    
#####
####################################################

import sys
import random
#imported the PyQt6 library for GUI implementation (◣_◢)
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    #setting up the UI ┐( ͡◉ ͜ʖ ͡◉)┌
    def initUI(self):
        #setting windows title and size
        self.setWindowTitle("Rock Paper Scissors")#set window name
        self.setGeometry(125,125,400,350)#x coordinate,y coordinate, width of window, height of window

        #creating labels to display user's choice and computer's choice
        self.user_selection_label = QLabel('Your Choice: ')
        self.computer_selection_label = QLabel("Computer\'s Choice: ")

        #label to display result
        self.result_label = QLabel('Result: ')
        
        #buttons for selection
        self.rock_button = QPushButton("Rock")
        self.paper_button = QPushButton("Paper")
        self.scissors_button = QPushButton("Scissors")

        #connect buttons to functions
        self.rock_button.clicked.connect(lambda: self.play_rps('rock'))
        self.paper_button.clicked.connect(lambda: self.play_rps('paper'))
        self.scissors_button.clicked.connect(lambda: self.play_rps('scissors'))

        #create layout
        layout = QVBoxLayout()

        #add widget to the layout
        layout.addWidget(self.user_selection_label)
        layout.addWidget(self.computer_selection_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.rock_button)
        layout.addWidget(self.paper_button)
        layout.addWidget(self.scissors_button)
        
        #setting layout
        self.setLayout(layout)
        ### function logic for game ᕕ( ͡° ͜ʖ ͡° )ᕗ
    def play_rps(self, user_selection):
        #choices using a dictionary
        choices = {0: 'rock', 1: 'paper', 2: 'scissors'}
        
        #generate choice
        computer_choice = choices[random.randint(0,2)]
       
        #update selection text
        self.user_selection_label.setText(f'Your Choice: {user_selection.capitalize()}')
        self.computer_selection_label.setText(f'Computer\'s Choice: {computer_choice.capitalize()}')
       
        #result of selection
        if user_selection == computer_choice:
            result = 'Draw!'
        elif(user_selection == 'rock' and computer_choice == 'scissors') or \
            (user_selection == 'paper' and computer_choice == 'rock') or \
            (user_selection == 'scissors' and computer_choice == 'paper'):
            result = 'You win!'
        else:
            result = 'Computer win!'
       
        #update result label
        self.result_label.setText(f'Result: {result}')

"""statement is used to check whether the Python script is being run directly by the interpreter, or if it is being imported as a module into another script."""
#RUN (┛◉Д◉)┛彡┻━┻
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
