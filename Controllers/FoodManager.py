from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurants=self.__PrepareRestaurants()
        
    def __PrepareFoodItems(self):
        item1=FoodItem(name="VegBiriyani",rating=4,price=100,description="****")
        item2=FoodItem(name="chickenBiriyani",rating=4.2,price=150,description="****")
        item3=FoodItem(name="Parotta",rating=4.4,price=10,description="****")
        item4=FoodItem(name="Dosa",rating=4.6,price=60,description="****")
        item5=FoodItem(name="ChickenNoodles",rating=3.2,price=80,description="****")
        return[item1,item2,item3,item4,item5]
    
    def __PrepareFoodMenus(self):
        FoodItems=self.__PrepareFoodItems()
        menu1=FoodMenu("Veg")
        menu1.FoodItems=[FoodItems[0],FoodItems[3]]
        menu2=FoodMenu("Non-Veg")
        menu2.FoodItems=[FoodItems[1],FoodItems[2]]
        menu3=FoodMenu("Chinese")
        menu3.FoodItems=[FoodItems[4]]
        return[menu1,menu2,menu3]
        
    def __PrepareRestaurants(self):
        FoodMenus=self.__PrepareFoodMenus()
        res1=Restaurant(name="A1",rating=4.7,location="Perumalpuram",offer=10)
        res1.FoodMenus=[FoodMenus[1],FoodMenus[2]]
        res2=Restaurant(name="NewRuchi",rating=4.5,location="Junction",offer=15)
        res2.FoodMenus=[FoodMenus[0],FoodMenus[1],FoodMenus[2]]
        res3=Restaurant(name="ArabianHotGrill",rating=4.8,location="Palayamkottai",offer=20)
        res3.FoodMenus=[FoodMenus[1],FoodMenus[2]]
        return[res1,res2,res3]
    
    def FindRestaurant(self,name):
        for res in self.Restaurants:
            if res.Name==name:
                return res