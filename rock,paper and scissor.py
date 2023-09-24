# I bulit my first game using python 
import random
#  if two values are equal, declear a tie 
def gamewin(comp,you): 
    if comp == you:
        return None
    #  check for all possiblilities when computer chose r
    elif comp == 'r':
        if you == 's':
            return False 
        elif you == 'p':
            return True
        #  check for all possiblilities when computer chose p
    elif comp == 'p':
        if comp == 'r':
            return False 
        elif you == 's':
            return True 
        #  check for all possiblilities when computer chose s
    elif comp == 's':
        if you == 'p':
            return False  
        elif you == 'r':  
            return True 
        
print("comp Trun: scissor (s) paper(p) or rock(r)?")
randNo =random.randint(1,3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p' 
elif randNo == 3:
    comp = 's' 

you =input('your turn: Scissor(s) paper(p) or rock(r)') 
a = gamewin(comp,you) 
print(f'computer chose {comp}') 
print(f'you chose {you}') 
if a == None:
    print('the game is tie!')
elif a:
    print('you win!') 
else:
    print('sorry!')  