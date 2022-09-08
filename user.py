class First:

    def madenewname(self,name):
        return name.title()
    
class second(First):
    def printname(self,name):
        return self.madenewname(name)


second1 = second()
print(second1.printname("aziz"))