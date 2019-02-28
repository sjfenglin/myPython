from functools import reduce


# Q1 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(L):
    return list(map(lambda name: str.title(name), L))


# Q1 方法二
def lower2upper(L):
    return map(lambda s: s[0:1].upper() + s[1:].lower(), L)


# Q2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y, L)


# Q3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    # 字符串转换成数字
    return DIGITS[s]


def fn(x, y):
    # 将序列变换成整数
    return x * 10 + y


def str2float(s):
    f_before = s.split('.')[0]  # 小数点前面的数字
    f_end = s.split('.')[1]  # 小数点后面的数字

    return reduce(fn, map(char2num, f_before)) + reduce(fn, map(char2num, f_end)) / 1000


# 测式
print('测试'* 20)
print(str2float('123.456'))

