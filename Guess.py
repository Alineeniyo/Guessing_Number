import random   
def compter_guess(x):
    guess=0
    low=1
    high=x
    feedback= ''
    while feedback != 'c':
        guess =random.randint(low,high)
        feedback = input((f'Is {guess} too high (H) , too low (L) or correctlt (C)')).lower()
        if feedback == 'h':
            high =guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay ! The feedback guessing number , {guess} , correctlty')            
compter_guess(20)

