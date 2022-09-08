from email import header
from turtle import window_height
import weakref


class car:
    def __init__(self, model, color, price, horsepower):
        self.model = model
        self.color = color
        self.price = price
        self.horsepower = horsepower

    def showinfocar(self):
        return{
        "model": self.model,
        "color": self.color,
        "price": self.price,
        "horsepower": self.horsepower
        }

class Truck(car):
    def __init__(self, model, color, price, horsepower,capacity,weight):
        self.capacity = capacity
        self.weight = weight
        super().__init__(model, color, price, horsepower)

    def returninfocar(self):
        new_dct = super().returninfocar()
        new_dct.update({"capacity":self.capacity, "weight":self.weight})

    def showtruckinfo(self):
        print(tabulate(self.returninfocar(),headers="keys"))

class Lightcar(car):
    def __init__(self,model,color,price,horsepower,weight,max_score,typecar):
        self.weight = weight
        self.max_score = max_score  
        self.typecar = typecar

        super().__init__(model, color, price, horsepower)

    def returninfocar(self):
        new_dct = super().returninfocar()
        new_dct.update({"typecar":self.typecar, "weight":self.weight,"max_score":self.max_score})
        return [new_dct]
objTruck1 = Truck("man","white","120.000$",220,4300,8)
objTruck2 = Truck("Mercedes","Black")


#class LightCar(car):
 #   def __init__(self, model, color, price, horsepower):
  #      super().__init__(model, color, price, horsepower)






