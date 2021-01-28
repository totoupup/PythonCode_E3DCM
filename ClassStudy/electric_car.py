class Car():
    """一次模拟骑车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        """制造商、型号、生产年份"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #汽车的里程表
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading)+" miles on it.")
        
    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        """将里程表增加指定的量"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """汽车邮箱"""
        print("This car has a full gas tank!")
        
#针对汽车电瓶的属性和方法
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=70):
        "初始化电瓶的属性"
        self.battery_size = battery_size
    
    def describe_battery(self):
        "打印一条描述电瓶容量的消息"
        print("This car has a "+str(self.battery_size)+"-kwh battery.")
        
    def get_range(self):
        "打印一条消息，指出电瓶的续航里程"
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)
        
#继承
class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        #super()是一个特殊函数，帮助Python将父类和子类联系起来
        #父类也称超类
        super().__init__(make,model,year)
        #子类新属性
        """！重点！"""
        "#创建新的Battery实例存储在ElectricCar属性self.battery中"
        self.battery = Battery()
    #子类新方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery.")
    #重写父类同名方法
    def fill_gas_tank(self):
        """电动汽车没有邮箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla','model s', '2016')
print(my_tesla.get_descriptive_name())

"""！重点！"""
#ElectricCar类.Battery类.Battery类类方法
#Battery类的实例被存储在ElectricCar类的属性
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
        

#my_new_car = Car('toyota','vios','2020')
#print(my_new_car.get_descriptive_name())
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()
#my_new_car.update_odometer(20)

#my_used_car = Car('subaru','outback',2013)
#print(my_used_car.get_descriptive_name())
#my_used_car.update_odometer(23500)
#my_used_car.read_odometer()
#my_used_car.increment_odometer(100)
#my_used_car.read_odometer()