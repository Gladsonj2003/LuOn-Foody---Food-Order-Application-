# FoodApp.py
from Models.User import *
from Models.Usermanager import *
from Controllers.MainMenu import *

class LoginSystem:
    def Login(self):
        mailid=input("Enter your mail ID: ")
        password=input("Password: ")

        user=UserManager.FindUser(mailid=mailid, pwd=password)
        
        if user is not None:
            print("Login Successfully..")
        else:
            print("Invalid MailId/Password.... Please Retry")
            
    def Register(self):
        name=input("Name: ")
        mobile=int(input("Enter your mobile number: "))
        mailid=input("Enter your mail ID: ")
        password=input("Password: ")
        
        user= User (name=name,phn=mobile,mail=mailid,pwd=password)
        UserManager.AddUser(user)
        
    def GuestLogin(self):
        pass
    
    @staticmethod
    def Exit():
        print("Thank you for using our Food App..")
        exit()
        
    def validateOption(self,option):
        try:
            getattr(self, option)()
        except AttributeError:
            print("Invalid choice.. Please Retry")
    
class FoodApp:
    LoginOptions={1:"Login",2:"Register", 3:"GuestLogin",4:"Exit"}
    @staticmethod
    def Init():
        print("<< Welcome to LuOn Foody >>")
        
        menu=MainMenu()
        menu.Start()
        
        loginSystem=LoginSystem()
        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}",end="  ")
            print()
            
            try:
                choice=int(input("Please Enter your choices: "))
                loginSystem.validateOption(FoodApp.LoginOptions[choice])
            except (ValueError,KeyError):
                print("Invalid input.. Please Enter the Valid Choice")