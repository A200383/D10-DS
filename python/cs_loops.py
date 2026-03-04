"""
1.for loop
2.while loop

for varible ib seq:
    //statements

    for varible in range(start, end, step):
        //statements
"""

# str1="SOMETHINg IS FISHY"
# x=1
# for char in str1:
#     print(char, x)
def count_vowels(str1):
    count=0
    for char in str1:
        if char in "aeiouAEIOU":
            count+=1
    return count