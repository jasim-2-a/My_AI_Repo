import random

def play():
    user = input("What is your choice?  'R' for rock 'P' for paper 'S' for scissor:")
    computer = random.choice(['R','P','S'])
    if user == computer:
        return 'tie'
    if is_win(user,computer):
        return 'You won'
    
    return 'You Lost'
def is_win(player,opponent):
    if(player == 'R' and opponent == 'S')or(player =='S' and opponent == 'P')or(player=='P' and opponent=='R'):
        return True
    
print(play())