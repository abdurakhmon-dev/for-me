import math
class Myfunctions:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
        self.printSum()
        self.printMinus()

    def printSum(self):
        print(self.number1 + self.number2)
    
    def printMinus(self):
        print(self.number1 - self.number2)

    def printKvadrat(self):
        print(math.pow(self.number1,self.number2))
    
obj = Myfunctions(3,2)
obj.printKvadrat()


#print(dir(obj))  -->  classning hamma funksiyasini ekranga chiqaradi