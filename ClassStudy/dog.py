class Dog():#Python中首字母大写的名称指的是类
    
#    类中的函数称为方法
    """一次模拟小狗的简单尝试"""
    #__init__()特殊方法
    #Dog类创建实例时，Python会自动运行它
    #双下划线__约定，避免Python默认方法与普通方法冲突
    #形参self必不可少，必须位于其他形参前面
    
    #self形参是代表类的实例的变量名
    def __init__(self,name,age):
        """初始化属性name和age"""
        #以self为前缀的变量可供类中的所有方法使用
        self.name = name
        self.age = age
        
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over！")

#小写名称指根据类创建的实例
my_dog = Dog("BigYellow",4)
my_dog.sit()

your_dog = Dog("LittleBlack",1)
your_dog.sit()