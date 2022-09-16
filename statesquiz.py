from tkinter import *
import random
from random import shuffle


root = ()
root.title('States Quiz')
root.geometry("500x500")
        
    
print ("test")
MIN = 0
MAX = 49
    
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

num = random.randint(MIN,MAX)
statecap = statescapList[num]
incstate = statesListinc[num]
states = state[num]
            
listcity=[statecap,incstate]
shuffle(listcity)
print('test') 
       
questionstates = Label(root, text=("What is the state captial of "+ states), font=("Helvetica", 20))
questionstates.pack(pady=20)
        

print("test")            
        
def submit1():
        if listcity[0] == statecap:
                Correct = Label(root, text=('Correct!'), font=("Helvetica", 20))
                Correct.pack(pady=20)
                
                exit_button = Button(root, text="Exit", command=root.destroy)
                exit_button.pack(pady=20)
                
                again_button = Button(root, text="Play Again")
                again_button.pack(pady=20)

        elif listcity[0] == incstate:
                inCorrect = Label(root, text=('Incorrect'), font=("Helvetica", 20))
                inCorrect.pack(pady=20)
                
                exit_button = Button(root, text="Exit", command=root.destroy)
                exit_button.pack(pady=20)

                again_button = Button(root, text="Play Again")
                again_button.pack(pady=20)
                
                
def submit2():
            if listcity[1] == statecap:
                Correct = Label(root, text=('Correct!'), font=("Helvetica", 20))
                Correct.pack(pady=20)
                
                exit_button = Button(root, text="Exit", command=root.destroy)
                exit_button.pack(pady=20)
                
                again_button = Button(root, text="Play Again")
                again_button.pack(pady=20)
                
            elif listcity[1] == incstate:
                inCorrect = Label(root, text=('Incorrect'), font=("Helvetica", 20))
                inCorrect.pack(pady=20)
                
                exit_button = Button(root, text="Exit", command=root.destroy)
                exit_button.pack(pady=20)
                
                again_button = Button(root, text="Play Again")
                again_button.pack(pady=20)
                
                
button1 = Button(root, text=listcity[0], command=submit1)
button1.pack(pady=20)
button2 = Button(root, text=listcity[1], command=submit2)
button2.pack(pady=20)

