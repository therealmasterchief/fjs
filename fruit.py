import random
class fruitquiz:
    def __init__(self):
        self.fruits={
            'apple':'red',
            'watermelon':'green',
            'banana':'yellow',
            'orange':'orange'
        }
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("what is the color of:", fruit,"?")
            answer=input("enter answer")
            if (answer.lower())==color:
                print("correct")
            else:
                print("wrong")
            option=int(input("enter 0 to continue and press 1 to stop"))
            if(option):
                break
print("welcome to t the quiz")
x=fruitquiz()
x.quiz()