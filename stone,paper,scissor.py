# if it is possible try to built a application uses this backend like make 
# #  website application of this stone paper scissor game.
# like try a theme as three options like rock paper scissor then add button to webpage and then add backend and functionality then 
# then link this python file to that
# if u want to go a little bit advanced then try to use camera and find out the signs of rock paper scissor then add the above steps
# import random

def swg(comp,mine):
    if(comp == 'stone' and mine == 'papers'):
        return True
    elif(comp == 'scissor' and mine == 'stone'):
        return True
    elif(comp == 'paper' and mine == 'scissor'):
        return True
    else:
        return False
    
choice = ('stone', 'paper', 'scissor')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input('choose either stone, paper or scissor : ')

win = swg(comp, mine)
if win:
    print("you won")
else:
    print(f"you choose {mine} and computer choose {comp}")
    print("you lose")