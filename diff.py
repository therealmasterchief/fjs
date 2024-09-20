class diff :
    def __init__(self,number):
        self.number=number
    def __lt__(self,number2):
        if (self.number<number2.number):
            return "ob1 is less than 2"
        else:
            return "ob1 is more than ob2"
    def __eq__(self,number2):
        if(self.number==number2.number):
            return "both are equal"
        else:
            return "both are not equal"

ob1= diff(4)
ob2= diff(13)
print(ob1<ob2)

ob3=diff(11)
ob4=diff(11)
print(ob3==ob4)