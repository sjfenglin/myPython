print('hello world Sunjian!!')

age = 33

if age >= 18:
    if age>50:
        print('老年人')
    print ('adult')
elif age >6 and age<= 12 :
    print ('少年')
else:
    print ('baby')



L = ['老大', '老二', '老三', '老四']
for name in L:
    print (name)

# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum1 = 0
x = 2
n = 0
while True:

    sum1 = sum1 + pow(x,n)
    n = n + 1
    print(n,x)
    if n > 19:
        break
print("任务1",sum1)


# 计算100以内的奇数的和
sum = 0
x = 0
while True:

    x = x + 1
    if x%2 ==0:
        continue

    if x > 100:
        break
    sum=sum+x
    print(x,sum)
print ("任务2",sum)

# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）
for x in [0,1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
        if x<y:
            print (x,y)
print("任务3")



#在生成的表格中，对于没有及格的同学，请把分数标记为红色。
#提示：红色可以用 <td style="color:red"> 实现。

dd = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%sun</td><td style="color:red">%sun</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in dd.items()]
print(u"\n任务4")
print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>')

print('\n')
print( [m + n for m in 'ABC' for n in '123'])


##
print('\n 任务四')
##from functools import map  ## 从functools模块中 引入高阶函数 reduce
def format_name(s):
    return s[0].upper() + s[1:].lower()
print (list(map(format_name, ['adam', 'LISA', 'barT'])))


##
print('\n 任务五')
from functools import reduce  ## 从functools模块中 引入高阶函数 reduce
def prod(x, y):
    return x * y
print (reduce(prod, [2, 4, 5, 7, 12]))


class sunjian(object):
    name = '初始姓名'
    age = 18

    def say(self):
        self.name = 'say name'
        self.age = 188
        ##print(self.name, '  *****  ',self.age)
        return None


yueyue = sunjian()
print('\n 1 ',yueyue.name, yueyue.age)

yueyue.say()
print('\n 2 ',yueyue.name, yueyue.age)
print('\n 3 ',sunjian.name, sunjian.age)


