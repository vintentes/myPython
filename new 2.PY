# 使用#号输出一个长方形，用户可以指定宽和高，while实现
'''
height=int(input("height:"))  #用户输入高度
width=int(input("width:"))    #用户输入宽度
num_height=1
while num_height<=height:
    num_width=1
    while num_width<=width:
        print("#",end="")
        num_width+=1
    num_height+=1
    print()
'''

'''
height=int(input("height:"))  #用户输入高度
width=int(input("width:"))    #用户输入宽度
num2=height
while num2>0:
    num1=width
    while num1>0:
        print("#",end="")
        num1-=1
    num2-=1
'''