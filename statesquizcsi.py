MIN = 0
MAX = 49

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
from random import shuffle
from tkinter import *


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the self window
    self.title('States and Capitals Quiz')
    self.geometry('500x500')
        
    fillerdict = {
            
            
        }
    
    statecapDict = {'Alabama': 'Montgomery',
                'Alaska': 'Juneau',
                'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock',
                'California': 'Sacramento',
                'Colorado': 'Denver',
                'Connecticut': 'Hartford',
                'Delaware': 'Dover',
                'Florida': 'Tallahassee',
                'Georgia': 'Atlanta',
                'Hawaii': 'Honolulu',
                'Idaho': 'Boise',
                'Illinois': 'Springfield',
                'Indiana': 'Indianapolis',
                'Iowa': 'Des Moines',
                'Kansas': 'Topeka',
                'Kentucky': 'Frankfort',
                'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta',
                'Maryland': 'Annapolis',
                'Massachusetts': 'Boston',
                'Michigan': 'Lansing',
                'Minnesota': 'Saint Paul',
                'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City',
                'Montana': 'Helena',
                'Nebraska': 'Lincoln',
                'Nevada': 'Carson City',
                'New Hampshire': 'Concord',
                'New Jersey': 'Trenton',
                'New Mexico': 'Santa Fe',
                'New York': 'Albany',
                'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck',
                'Ohio': 'Columbus',
                'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem',
                'Pennsylvania': 'Harrisburg',
                'Rhode Island': 'Providence',
                'South Carolina': 'Columbia',
                'South Dakota': 'Pierre',
                'Tennessee': 'Nashville',
                'Texas': 'Austin',
                'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier',
                'Virginia': 'Richmond',
                'Washington': 'Olympia',
                'West Virginia': 'Charleston',
                'Wisconsin': 'Madison',
                'Wyoming': 'Cheyenne'}
                        
                
    stateDictincorrect = {'Alabama': 'Birginham',
                'Alaska': 'Wasilla',
                'Arizona': 'Tucson',
                'Arkansas': 'Fayetteville',
                'California': 'Los Angeles',
                'Colorado': 'Colorodo Springs',
                'Connecticut': 'Bridgeport',
                'Delaware': 'Wilmington',
                'Florida': 'Miami',
                'Georgia': 'Colombus',
                'Hawaii': 'East Honolulu',
                'Idaho': 'Meridian',
                'Illinois': 'Aurora',
                'Indiana': 'Fort Wayne',
                'Iowa': 'Cedar Rapids',
                'Kansas': 'Wichita',
                'Kentucky': 'Lexington',
                'Louisiana': 'New Orleans',
                'Maine': 'Portland',
                'Maryland': 'Baltimore',
                'Massachusetts': 'Worcester',
                'Michigan': 'Detroit',
                'Minnesota': 'Minneapolis',
                'Mississippi': 'Gulfport',
                'Missouri': 'Kansas City',
                'Montana': 'Billings',
                'Nebraska': 'Omaha',
                'Nevada': 'Las Vegas',
                'New Hampshire': 'Manchester',
                'New Jersey': 'Newark',
                'New Mexico': 'Albuquerque',
                'New York': 'New York City',
                'North Carolina': 'Charlotte',
                'North Dakota': 'Fargo',
                'Ohio': 'Cleveland',
                'Oklahoma': 'Tulsa',
                'Oregon': 'Portland',
                'Pennsylvania': 'Pittsburg',
                'Rhode Island': 'Cranston',
                'South Carolina': 'Charleston',
                'South Dakota': 'Sioux Falls',
                'Tennessee': 'Memphis',
                'Texas': 'Houston',
                'Utah': 'West Valley City',
                'Vermont': 'Burlington',
                'Virginia': 'Sion Farm',
                'Washington': 'Seattle',
                'West Virginia': 'Huntington',
                'Wisconsin': 'Milwaukee',
                'Wyoming': 'Casper'}
                
                
                
                
                
    statescapList = list(statecapDict.values())
    state = list(statecapDict)
    statesListinc = list(stateDictincorrect.values())

    correct = 0
    incorrect = 0


    again = 'y'    
    while (again == 'y'):

        num = random.randint(MIN,MAX)
        statecap = statescapList[num]
        incstate = statesListinc[num]
        states = state[num]
            
        listcity=[statecap,incstate]
        shuffle(listcity)    
        
        questionstates = ttk.Label(self, text=("What is the state captial of "+ states), font=("Helvetica", 20))
        questionstates.pack(pady=20)
        
        def reset_board(self):
                self._game.reset_game()
                self._update_display(msg="Ready?")
                for button in self._cells.keys():
                    button.config(highlightbackground="lightblue")
                button.config(text="")
                button.config(fg="black")

            
            
        
        def submit1():
            if listcity[0] == statecap:
                Correct = ttk.Label(self, text=('Correct!'), font=("Helvetica", 20))
                Correct.pack(pady=20)
                
                exit_button = ttk.Button(self, text="Exit", command=self.destroy)
                exit_button.pack(pady=20)
                
                again_button = ttk.Button(self, text="Play Again", command=reset_board)
                again_button.pack(pady=20)

            elif listcity[0] == incstate:
                inCorrect = ttk.Label(self, text=('Incorrect'), font=("Helvetica", 20))
                inCorrect.pack(pady=20)
                
                exit_button = ttk.Button(self, text="Exit", command=self.destroy)
                exit_button.pack(pady=20)

                again_button = ttk.Button(self, text="Play Again", command=reset_board)
                again_button.pack(pady=20)
                
                
        def submit2():
            if listcity[1] == statecap:
                Correct = ttk.Label(self, text=('Correct!'), font=("Helvetica", 20))
                Correct.pack(pady=20)
                
                exit_button = ttk.Button(self, text="Exit", command=self.destroy)
                exit_button.pack(pady=20)
                
                again_button = ttk.Button(self, text="Play Again", command=reset_board)
                again_button.pack(pady=20)
                
            elif listcity[1] == incstate:
                inCorrect = ttk.Label(self, text=('Incorrect'), font=("Helvetica", 20))
                inCorrect.pack(pady=20)
                
                exit_button = ttk.Button(self, text="Exit", command=self.destroy)
                exit_button.pack(pady=20)
                
                again_button = ttk.Button(self, text="Play Again", command=reset_board)
                again_button.pack(pady=20)
                
                
        button1 = ttk.Button(self, text=listcity[0], command=submit1)
        button1.pack(pady=20)
        button2 = ttk.Button(self, text=listcity[1], command=submit2)
        button2.pack(pady=20)
            
        print('\n' "What is the capital of "+ states)
        ans = int(input("\n1." + listcity[0] +"\n2." + listcity[1] + "\nType the name of the capital here:"))
            
        print(ans)
            

        if (ans == 1):
            if (statecap == listcity[0]):
                print (listcity[0] + ' is the capital of ' + states) 
                correct += 1
                print ('Score is - ',correct)
                print ('Incorrect attempts is - ',incorrect)
                again = input('If you want to play again type "y" and if you do not want to play type anything else. : ')  

            else:
                print (listcity[0] + ' is not the capital of ' + states)
                incorrect += 1
                print ('Score is - ',correct)
                print ('Incorrect attempts is - ',incorrect)
                again = input('If you want to play again type "y" and if you do not want to play type anything else. : ')  
    
        elif (ans == 2):
            if (statecap == listcity[1]):
                print (listcity[1] + ' is the capital of ' + states) 
                correct += 1
                print ('Score is - ',correct)
                print ('Incorrect attempts is - ',incorrect )
                again = input('If you want to play again type "y" and if you do not want to play type anything else. : ')  
    
            else:
                print (listcity[1] + ' is not the capital of ' + states)
                incorrect += 1
                print ('Score is - ',correct)
                print ('Incorrect attempts is - ',incorrect )
                again = input('If you want to play again type "y" and if you do not want to play type anything else. : ')  
    
        else:
            print ("Incorrect Input")   
                

                    

if __name__ == "__main__":
      app = App()
      app.mainloop()
