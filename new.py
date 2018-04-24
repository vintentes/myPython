#!/usr/bin/env python
#print ("你好，世界")
#猜年龄1
'''
age_of_one = 88
guess_age = int(input(">>:"))
if guess_age == age_of_one:
    print("Yes,You got it ...")
else:
    print("No,it's wrong.")
'''
#猜年龄2 break 跳出整个循环 continue 跳出本次循环
'''
age = 88
while True:
    user_input_age = int(input("Age is :"))
    if user_input_age == age:
        print("Yes,You got it ...")
        break
    elif user_input_age>age:
        print("Is bigger")
    else:
        print("Is smaller")
print("end！")
'''
