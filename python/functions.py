"""
1.predefined/built-in:

functions which which were defined already by python itself for certain tasks

2.user defined:

functions which were defined by the user for certain tasks
a.static functions: functions which are defined inside a class but not using self
b.dynamic functions: functions which are defined inside a class and using self



syntax:

def func_name():
    //code


func_name()-->like this we can invoke/call a function 
by default function can return none as a value
to return a value from a function we need to use return keyword 








"""

# def sample():
#     print("hello i am a sample function")
#     return 'thankyou' 
#     print('visit one again')                      
# print(sample()) 

#thankyou is being returned  by sample() (func def)
#and assigning into the function call sample() 

#to say hell for a student using a function as per his name

# def greetings(name):
#     print(f"hello{name}")
#     return '10000-coders'

# print(greetings('kishore'))
# print(greetings('ashok'))  
# print(greetings('kiran'))
# print(greetings('hemanth'))    


# def showtime(name,movie):
#     print(f"{name} is watching {movie}")
#     return 'thankyou for visiting us'
    
# #this function is returning a value thankyou for visiting us

# print(showtime('lucky','OG'))
# print(showtime('kishore','kgf'))


#showtime('john','kgf')

#write a function ton calculate the movie ticket price

# def movie_ticket(price,quantity):
#     total=price*quantity
#     print(f"total amout is {total}")
#     return 'thankyou visit again'


# movie_ticket(3,300)
# print(movie_ticket(int(input('enter the price : ')),int(input('enter the quantity'))))


#write a function which calculate movie ticket price and return
#if amount is greater than 2000 then return coke+popcorn
#if amount id greater than 1500 then return coke
#if amount is less than 1500 then say thankyou

# def movie_ticket_offers(ticketsprice,ticketsquantity):
#     amount=(ticketsprice*ticketsquantity)
#     if(amount>2000):
#         return('YOU GOT A COKE AND POPCORN')
#     elif(amount>1500):
#         return('YOU GOT A COKE')
#     else:
#         return('THANKYOU YOU VISIT AGAIN')


# print(movie_ticket_offers(600,4))
# print(movie_ticket_offers(400,4))
# print(movie_ticket_offers(300,4))

# def movie_ticket_gift():
    
#     price = float(input("Enter ticket price: "))
#     quantity = int(input("Enter number of tickets: "))
    
#     total_amount = price * quantity  
    
#     if total_amount > 2000:
#         return f"Total Bill: {total_amount} | Gift: Coke + Popcorn"
    
#     elif total_amount > 1500:
#         return f"Total Bill: {total_amount} | Gift: Coke"
    
#     else:
#         return f"Total Bill: {total_amount} | Thank You!"


# result = movie_ticket_gift()
# print(result)