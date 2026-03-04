
#list1=[10,23,45,31,24,67,87,45,34]
#x=1
#for num in list1:
 #   print(x)
 #   x+=1

#from numbers 1 to 50 count how many can be divisible by 3 and 5
#count=0
#for num in range(1,51):
 #   if i%3==0 or i%5==0:
  #      count+=1
   #     print(i)
#print(count)

"""from 1 to 30 
add even numbers
and multiply odd numbers using for loop"""  

# sum=0
# product=1
# for x in range(1,31):
#     if x%2==0:
#         sum+=x
#     else:
#         product*=x
# print("sum of even numbers:",sum)
# print("product of odd numbers:",product)  
#  
# plan=30
# current_day=1
# while current_day<=plan:
#     print(f"day- {current_day} watch and njy")
#     current_day+=1

# str1='something'
# x=0
# while x<len(str1):
#     if str1[x] in 'aeiou':
#        print(str1[x])
#     x+=1

# x=len(str1)-1
# while x>0:
#     print(str1[x])
#     x-=1

# num=48962
# str1=str(num)
# x=0
# while x<=len(str1)-1:
#     print(str1[x])
#     x+=1

# 0--->0<=4-->T=str1[0]=4
# 1--->1<=4-->T=str1[1]=8
# 2--->2<=4-->T=str1[2]=9
# 3--->3<=4-->T=str1[3]=6
# 4--->4<=4-->T=str1[4]=2
# 5--->5<=4-->T=str1[5]=???


# num=158
# while num>0:
#     ld=num%10
#     print(ld)
#     num=num//10

# 158-->158>0-->num%10--->8-->//10--->15
# 15-->15>0-->5-->//10--->1
# 1-->1>0-->1-->%10--->1-->//10--->0
# 0-->0>0-->F
 

# num=565
# num1=num
# rev=0
# while num>0:
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# print(rev)
# if rev==num1:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")


# num=158
# count=0
# while num>0:
#     ld=num%10
#     count+=1
#     num=num//10
# print(count)

# num=158
# sum=0
# while num>0:
#     ld=num%10
#     sum+=ld
#     num=num//10
# print(sum)

# num=158
# product=1
# while num>0:
#     ld=num%10
#     product*=ld
#     num=num//10
# print(product)
 
#  write a program to check  given number is armstrong or not
num=565
num1=num
sum=0
while num>0:
    ld=num%10
    sum+=ld**3
    num=num//10
print(sum)
if sum==num1:
    print("it is a armstrong")
else:
    print("it is not a armstrong")
