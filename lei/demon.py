class Person():
    name = "小明"
    age = 18
    sex = "男"
    
    # def eat(self,a1):
    #     print("rennengchi{}".format(a1))
    #     return"xxx"
    
    def run(self):
        self.aihao = "打篮球"  #初始化变量
        self.name = "小张"    #替换成员变量值
        print("这个类的名字是{}".format(self.name))


p = Person()  #调用方法
p.run()
print(p.aihao) 
print(p.name)


#不可行
# print(Person().aihao) 
# print(Person().name)

