from .FoodManager import *
from Models.Cart import *

class MainMenu:
    
    __Options = {1: "ShowRestaurents", 2: "ShowFoodItems", 3: "SearchRestaurant", 4: "SearchFoodItems", 5: "Logout"}
    
    def __init__(self):
        self.__FoodManager = FoodManager()
        
    def ShowRestaurents(self):
        for i, res in enumerate(self.__FoodManager.Restaurants, 1):
            res.DisplayItem(i)
    
        choice = int(input("Please select the Restaurant : "))
        
        if 0 < choice <= len(self.__FoodManager.Restaurants):
            res = self.__FoodManager.Restaurants[choice - 1]
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print("Invalid restaurant selection.")
        

    def ShowFoodItems(self, foodItems=None):
        if foodItems is not None:
            for i, foodItem in enumerate(foodItems, 1):
                foodItem.DisplayItem(i)
            choices = list(map(int, input("Please Choose your Food Items (eg. 1,2) : ").split(',')))
            
            try:
                cart = Cart(foodItems, choices)
                cart.ProcessOrder(foodItems)  # Pass foodItems here
            except KeyError:
                print("Invalid choice. Please retry.")
        else:
            pass

    
    def SearchRestaurant(self):
        resName = input("Enter the Restaurant Name: ")
        res = self.__FoodManager.FindRestaurant(resName)
        
        if res is not None:
            print("Restaurant Found...")
            print(f"Name : {res.Name}, Rating : {res.Rating}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"No Restaurant Found in the Name {resName}")
    
    def SearchFoodItem(self):
        pass
    
    def ShowFoodMenus(self, menus):
        print("\n\nList of Menus Available :")
        for i, menu in enumerate(menus, 1):
            menu.DisplayItem(i)
        choice = int(input("Please Choose Menu : "))
        
        if 0 < choice <= len(menus):
            fooditems = menus[choice - 1].FoodItems
            self.ShowFoodItems(fooditems)
        else:
            print("Invalid menu selection.")
        
    def Start(self):
        while True:
            for option in MainMenu.__Options:
                print(f"{option}.{MainMenu.__Options[option]}", end="  ")
            print()
            
            try:
                choice = int(input("Please Enter your choices: "))
                value = MainMenu.__Options.get(choice)
                if value:
                    getattr(self, value)()
                else:
                    print("Invalid input.. Please Enter the Valid Choice")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
