from Models.User import *

class UserManager:
    __Users=[]
    
    @classmethod
    def AddUser(cls,userObj):
        if isinstance(userObj,User):
            cls.__Users.append(userObj)
            print("You have been Successfully registered")
        else:
            print("Invalid User")
    
    @classmethod        
    def FindUser(cls, mailid,pwd):
        for user in cls.__Users:
            if user.MailId==mailid and user.Password==pwd:
                return user