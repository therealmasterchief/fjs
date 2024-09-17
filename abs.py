import abc
from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("dog can walk and run")
class fish(animal):
    def move(self):
        print("can swim")
d=dog()
d.move()

f=fish()
f.move()