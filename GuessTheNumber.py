print('NAME:basavanagouda.y' ,'USN:1AY24AI017')
import random
number=random.randint(1,100)
guess=int(input("guess the number between 1 and 100:"))
if guess==number:
    print("you guessed it!!")
else:
    print(f"wrong! the number was {number}")
