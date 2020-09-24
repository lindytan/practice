class person():
    name = "zhansan"
    sex = "nnv"
    age = "22"
    yz = "1"
    
    def fly(self):
        print("jintian")

    def eat(self,food):   #在类里面相互调用方法，一定要用self
        self.aihao = "nv"
        self.yz = "2"  #在class下面不能有yz这个变量，不然就是修改yz的量
        print("{}能吃{}".format(self.name,food))

print(person.age)
print(person().fly())  #不调用参数类要加括号，方法也要加返回值，没有默认位none
p = person()
p.eat("海鲜")    #调用方法要加括号；self能引用自己类里面额属性和方法
print(p.aihao)  #前面要调用p.eat()的方法才能是实现打印预期结果
print(p.yz)  #需要class下面也有yz变量才能打印出来，没有就无法打印