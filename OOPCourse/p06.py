import sys

print( '打印sys.path 的类型',type(sys.path ))
print( '打印sys.path 的值',sys.path )

for p in sys.path:
    print(p,end='  ')
