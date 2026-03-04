""""

simple--if
if--else
if--elif--else
nested--if
"""

# print("statment1")
# if 2==3:
#     print("statment2")
#     print("statment3")  


"""
1. take a number and check whether it is  
a positive or negative 

"""

# num=int(input("enter the number : "))

# if num<0:
#     print("it is negative")
# else :
#     print("it is positive")

# if num==0:
#     print('number is zero')
# elif num<0:
#     print('number is negative')
# elif num>0:
#     print('number is positive') 
# else:
#     print('invalid number')    


# a=23
# d=20
# if a>d:
#     print("a is largest")
# else:
#     print("d is largest")


# a=120
# b=123
# c=43
# if a>b and a>c:
#     print("a is largest",a)
# elif b>a and b>c:
#     print("b is largest",b)
# else:
#     print("c is largest",c)

# if a<b and a<c:
#     print("a is smallest",a)
# elif b<a and b<c:
#     print("b is smallest",b)
# else:
#     print("c is smallest",c)

#print the second largest num
# if a<b and a>c or a>b and a<c:
#     print("a is second largest",a)
# elif b<a and b>c or b>a and b<c:
#     print("b is second largest",b)
# else:
#     print("c is second largest",c)


# check whether given num is 2-digit or not

# 789-->its not a 2-digit number
# 78-->its a 2-digit number
# >9 and <100   

# num=int(input('enter the number: '))
# if num>9 and num<100:
#     print(num,'is a 2-digit number')
# elif num>99 and num<1000:
#     print(num,'is a 3-digit number')
# else:
#     print(num,'is not a 2-digit number')

#check whether num is leap year or not
#generate electricity bill as per the units

"""
for first 100 units--->2rs/unit
next 100 units--->3rs/unit
above 200 units--->5rs/unit
"""
# unit=int(input("enter the number of units consumed:"))
# bill=0
# if unit<=100:
#     bill=unit*2
#     print(f"total electricity bill={bill}")
# elif unit<=200:
#     bill=(100*2)+(unit-100)*3
#     print(f"total electricity bill={bill}")
# else:
#     bill=(100*2)+(unit-200)*5
#     print(f"total electricity bill={bill}")
    

# year=int(input("enter the year:"))
# if year%4==0:
#     print("it is a leap year")
# else:
#     print("it is not a leap year")


# take 3 inputs-->
# triangle or not

# equilateral
# isosceles
# scalene

# not able to form a triangle

# a, b, c
# a+b+c=180-->yes we can form a triangle

# a=b=c
# equilateral

# a=b or b=c or c=a
# isosceles

# scalene
# a+b+c!=180-->not able to form a triangle

# def triangle():
#     a=int(input("enter the first side:"))
#     b=int(input("enter the second side:"))
#     c=int(input("enter the third side:"))
#     if a+b+c==180:
#         print("it is a triangle")
#         if a==b==c:
#             print("it is an equilateral triangle")
#         elif a==b or b==c or c==a:
#             print("it is an isosceles triangle")
#         else:
#             print("it is a scalene triangle")
#     else:
#         print("it is not a triangle")

# triangle()


#using nested if 

# temp is less then zero-->freezing

# temp is greater then zero-->
#      --->temp less then 30--->moderate
#      --->temp greater then 30--->its so hot

# temp=int(input("enter the temperature:"))
# if temp>0:
#     if temp<30:
#         print("it is moderate")
#     else:
#         print("it is so hot")
# else:
#     print("it is freezing")

"""
if we watch devare-1  then only  we can watch devara-2
otherwise go and watch devara-1 """

# is_devara1_watched=True
# is_devara2_watched=True

# if is_devara1_watched:
#     if is_devara2_watched:
#         print('u can watch devra'
