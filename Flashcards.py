class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+"( '+self.meaning') "
    
flash = []
print("Welcome ot flashcard application")

while(True):
    word = input("Enter the name you want to add flashcard : ")
    meaning = input("Entee the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0 , if you want to add another flashcard otherwise enter 1 : "))

    if(option):
        break

    print(" Your flashcard ")
    for i in flash:
        print(">", i)