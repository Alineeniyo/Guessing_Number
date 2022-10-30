import random 

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:

        guess =int(input(f'Guess a number btn 1 and {x} = '))

        if guess > random_number:

            print('you are wrong too low')

        elif guess < random_number:

            print("Sorry You are wrong again too high")  

    print(f'yay you gussed riht number of digits{random_number} correctly')         
guess(10)

    
