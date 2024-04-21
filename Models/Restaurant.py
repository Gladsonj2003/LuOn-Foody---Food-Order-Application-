from .AbstractItem import *
from .FoodMenu import *

class Restaurant(AbstractItem):
    def __init__(self, name,rating,location,offer):
        super().__init__(name=name,rating=rating)
        self.Location=location
        self.Offer=offer
        self.FoodMenu=None
        
    @property    
    def FoodMenus(self):
        return self.__FoodItems
    
    @FoodMenus.setter
    def FoodMenus(self,items):
        for item in items:
            if not isinstance(item,FoodMenu):
                print("Invalid FoodItem..")
                return
            
        self.__FoodItems=items
        
    def DisplayItem(self,start):
        print(f"{start} => {self.Name} => Rating: {self.Rating}")