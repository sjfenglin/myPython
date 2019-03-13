###from OOPCourse import p01    #引用包OOPCourse 和模块 p01
import OOPCourse.pkg01.p01
class mysun(object):
    __mysunName='类属性名称'
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
        print(mysun.__mysunName)
        return None

    def getName(self,name1):
        mysun.__mysunName=name1
        self.name1=name1
        print(name1,mysun.__mysunName)
        return None



aa=mysun('sunjian','male',18)
aa.getName("haha")
aa.temp='temple'

print(aa.name,aa.gender,aa.age,aa.temp,'\n','*' * 50)


def stu_key(name="No name", age=0, addr="No addr"):
    print("I am a student")
    print("我叫 {0}， 我今年 {1}岁了， 我住{2}".format(name, age, addr))


stu_key("sunjian",18,"Shanghai")

stu_key(name="name update", age=38, addr="update addr")