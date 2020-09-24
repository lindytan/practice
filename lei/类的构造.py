class Cat():
    #构造方法：固定方法，类实例化的时候运行
    def __init__(self,mx): #只能写一次init
        self.name = mx

    def aa(self):
        a = 1 # 只针对aa有效
        self.b = 2 #整个类都有效,使用时要先调用c.aa
#一定要取加参数
c = Cat("tomcat")
print(c.name)

