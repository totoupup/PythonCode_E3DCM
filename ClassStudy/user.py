class User():
    
    def __init__(self,first_name,last_name,profile_gender,profile_age):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_gender = profile_gender
        self.profile_age = profile_age
        self.login_attempts = 0
        
    def describe_user(self):#打印信息摘要
        print(self.first_name.title()+" "+self.last_name+"：") 
        print("gender： "+self.profile_gender)
        print("age： "+self.profile_age)
        
        
    def greet_user(self):#中国人first_name 名
        print("Hello! "+self.first_name.title()+" "+self.last_name)
    
    #增加登录次数    
    def increment_login_attempts(self,step=1):
        self.login_attempts += step
    
    #重置登录次数        
    def reset_login_attempts(self,default=0):
        self.login_attempts = default

class Admin(User):
        
user_tu = User("wang","tu","male","30")

user_to = User("zhu","tong","female","30")
user_to.increment_login_attempts()
print(user_to.login_attempts)

user_to.reset_login_attempts()
print(user_to.login_attempts)


#user_tu.describe_user()
#user_tu.greet_user()        
#
#user_to.describe_user()
#user_to.greet_user() 