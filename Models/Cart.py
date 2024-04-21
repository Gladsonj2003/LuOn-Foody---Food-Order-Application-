class Cart:
    def __init__(self, items, choices):
        self.Choices = choices
        self.FoodItems = self.__AddtoCart(items)
        
    def __AddtoCart(self, items):
        foodDic = {}
        for choice in self.Choices:
            if choice > len(items) or choice < 1:
                raise KeyError
            if choice in foodDic:
                foodDic[choice] += 1
            else:
                foodDic[choice] = 1
        return foodDic
    
    def ProcessOrder(self, foodItems):
        Total = 0
        for item, quantity in self.FoodItems.items():
            price = quantity * foodItems[item - 1].Price
            Total += price
            print(f"{foodItems[item - 1].Name} x {quantity} = {price}")
        print(f"Total : {Total}")
        
        self.ProcessPayment(Total)
        
    def ProcessPayment(self,amount):
        pass