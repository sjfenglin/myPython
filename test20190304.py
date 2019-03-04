def stu_key(name="No name", age=0, addr="No addr"):
    print("I am a student")
    print("我叫 {0}， 我今年 {1}岁了， 我住{2}".format(name, age, addr))


stu_key("sunjian",18,"Shanghai")

stu_key(name="name update", age=38, addr="update addr")