class flash:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + '-' + self.meaning
    
light=[]
print("welcome to the flashcard system")

while True:
    word= input("enter word")
    meaning=input("enter meaning")
    light.append(flash(word,meaning))
    option=int(input("enter 0 to continue and 1 to stop"))
    if(option):
        break
print("your flashcards are listed below")
for list in light:
    print("*",list)