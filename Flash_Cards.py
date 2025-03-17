class flashcards:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
    def __str__(self):
        #Will return a string
        return self.word+': '+self.definition

flash = []
print("Welcome to Ark's Flashcard Program")

#The following loop will run the the user decides to stop. 
while(True):
    word = input(str('Enter the name you want you want to add to the flashcard: '))
    definition = input(str('Enter the definition of the word: '))

    #This will append the word and definition to the flash list
    flash.append(flashcards(word, definition))

    #This will ask the user if they want to add more words to the flashcard
    more = input(str('Do you want to add more words to the flashcard? (yes/no): '))
    if more == 'no':
        break
    else:
        continue

#This will print the flashcard
for i in flash:
    print(i)
    