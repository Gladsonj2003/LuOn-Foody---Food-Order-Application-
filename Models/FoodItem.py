from .AbstractItem import *

class FoodItem(AbstractItem):
    def __init__(self,name,rating,price,description):
        super().__init__(name=name,rating=rating)
        self.Price=price
        self.Description=description
        
    def DisplayItem(self,start):
        print(f"{start} => Name : {self.Name} Price : {self.Price} Rating : {self.Rating}")