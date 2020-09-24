class baba():
    money = "1E"
    def make_money(self):
        print("xioamud")
#子类可以继承父类的属性和方法
#子类可以重写父类的属性和方法
class son(baba):
    name = "wsc"
    money = "-1e"
    def make_moneky(self):
        print("22")
s = son()
print(s.money)
s.make_moneky()
