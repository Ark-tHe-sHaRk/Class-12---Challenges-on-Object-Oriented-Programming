import random

class fruitquiz:

    #Create a constructor
    def __init__(self):
        self.fruits = {
            'apple': 'red',
            'banana': 'yellow',
            'grapes': 'purple',
            'mango': 'orange',
            'orange': 'orange',
            'pineapple': 'brown',
            'strawberry': 'red',
            'watermelon': 'green'
        }

    #Function for the quiz
    def quiz(self):
        while(True):
            fruit, colour = random.choice(list(self.fruits.items()))
            print('What is the colour of', fruit, '?')
            user_answer = input('Enter your answer: ')

            if(user_answer.lower() == colour):
                print('Correct Answer!')

            else:
                print('Incorrect Answer! The correct answer is', colour)

            option = input('Do you want to continue? (yes/no): ')
            if(option.lower() == 'no'):
                break
            else:
                print('Thank you for playing the Fruit Quiz!')

print('Welcome to the Fruit Quiz!')
fq = fruitquiz()
fq.quiz()
print('Thank you for playing the Fruit Quiz!')