import abc
from abc import ABC, abstractmethod
class abstract(ABC):
    def display(self,number):
        print("the number is ", number)
    @abstractmethod
    def task(self):
        print("It is an abstract function")
class testclass(abstract):
    def task(self):
        print("this is test class")
y= testclass()
y.task()
y.display(8)
