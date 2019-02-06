"""
Q1 Program to find max from 5 numbers
"""

'''
#way1
max = 0
list = [100,20,15,500,5]
for i in range (0,5):
 if max < list[i]:
     max =list[i]
print('Max no out of list is',max)
'''
#while list[0] == list[-1]:  # list[-1] helps you get the last element of the list
'''
#Way 2
max = 0
list = [100, 20, 15, 500, 5]
i = 0
while i < len(list):
    if max < list[i]:
      max = list[i]
    i=i+1
print('Max no out of list is', max)
'''
"""
Q2write a code to find minimum number from 5 values
"""
"""
list_min = [20, 45, 15, 10, 90, 200, 56, 5]
length = len(list_min)
minimum = list_min[1]
for i in range(0, length):
    if minimum > list_min[i]:
        minimum = list_min[i]
        print(i,minimum)
print("Min no in the list is",minimum)
"""

"""
creating pattern no 4
"""
"""
for i in range(0, 6):
    print(" ")
    symbol = i % 2
    print(symbol, end=" ")
    for j in range(0, i):
        if symbol == 1:
           symbol = 0
           print(symbol, end=" ")
        else:
            symbol = 1
            print(symbol, end=" ")
"""
"""
Q5 pattern
"""
"""
for i in range(0, 6):
    print(" ")
    symbol = 1
    print(symbol, end=" ")
    for j in range(0, i):
        if symbol==1:
         symbol=0
         print(symbol, end=" " )
        else:
         symbol=1
         print(symbol, end=" " )
"""
"""
Q6 pattern
"""
for i in range(0,5):
    print(" ")
    for j in range(1,6):
        print(j, end=" ")
        