for i in range(1, 21):
    if (i % 3 == 0 and i % 5 == 0):
        print(f"{i}--FizzBuzz")
    elif (i % 3 == 0):
        print(f"{i}--Fizz")
    elif (i % 5 == 0):
        print(f"{i}--Buzz")
    elif (i % 7 == 0):
        print(f"{i}--Bazz")
    elif (i % 11 == 0):
        print(f"{i}--Bizz")
    elif (i % 13 == 0):
        print(f"{i}--Bozz")
    elif (i % 17 == 0):
        print(f"{i}--Bizzz")
    elif (i % 19 == 0):
        print(f"{i}--Bizzzz")    
