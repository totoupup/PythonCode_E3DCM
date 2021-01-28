class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  #就餐人数
    
    def describe_restaurant(self):
        print("The restuarant name is "+self.restaurant_name+".")
        print("The cuisine type is "+self.cuisine_type+".")
        
    def open_restaurant(self):
        print(self.restaurant_name.title()+" is open.")
    
    #设置就餐人数    
    def set_number_served(self,total_number_served):
        self.number_served = total_number_served
    
    #将就餐人数递增    
    def increment_number_served(self,day_number_served):
        self.number_served += day_number_served
        
class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name,cuisine_type,flavors):
        
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
#        flavors = ['salt','sweety']
        
    def describe_restaurant(self):
        print("The IceCreamStand name is "+self.restaurant_name+".")
        print("The cuisine type is "+self.cuisine_type+".")
        
    def show_flavors(self):
        print("flavors:")
        print(str(self.flavors))


tug_icecream = IceCreamStand("Tug's IceCreamStand","private", ['salt','sweety'])
tug_icecream.describe_restaurant()
tug_icecream.show_flavors()     


#restaurant = Restaurant("Tug's Kitchen","private dishes")
#print(restaurant.restaurant_name)
#print(restaurant.cuisine_type)
#
##创建一个实例
#restaurant.describe_restaurant()
#restaurant.open_restaurant()
#print("There are "+str(restaurant.number_served)+" peoples had dinner here!")

#创建三个实例       
#pig_resta =  Restaurant("Pig's Kitchen","private dishes")
#dog_resta =  Restaurant("Dog's Kitchen","meat and bones")        
#cat_resta =  Restaurant("Cat's Kitchen","meat and fishes")            
#
#pig_resta.describe_restaurant()
#dog_resta.describe_restaurant()
#cat_resta.describe_restaurant()