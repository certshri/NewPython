# #################################
#1)Conditional Statements
#if
#If


#if
# #################################
'''number1 = 10
number2 = 40
number3 = 30
if number2 < number1:
    print("number1 is greater")
elif number3 > number2:
    print("number3 is greater")
elif number2>number1:
    print("NUMBER2 is greater")
else:
    print("number0 is greater")
'''

number_01 = 10
number_02 = 20
number_03 = 30

'''
# if number_01 < number_02:
#     if number_01 < number_03:
#         print('number_01 is max')
#     else:
#         print('number_03 is max')
# else:
#     if number_02> number_03:
#         print('number_02 is max')
#     else:
#         print('number_03 is max')
# '''
# for i in range(0, 5, 1):
#     print(i, end = " ") # by default after printing it goes to new line, so to continue on same line use end = " "
#     print('')  #  it takes to new line
#
#
#
# number = 0
# while number < 5:
#     print('number')
#     number += 1


# do while loop (by defaults enters in loop)
#number = 0
# while True:
#       if number > 5:
#        break
#        print(number)
#       number += 1

# for i in range (0,5):
#     print(" ")
#     for j in range (0,5):
#         print("*", end = " ")
#
# for i in range(0,5):
#     print(" ")
#     for j in range(0, 5):
#         print("1", end=" ")
# k = 0
# for i in range(0,5):
#
#     print(" ")
#     for j in range(0, 5):
#
#         print(k, end=" ")
#         if j == 4:
#          if k == 0:
#                k=1
#          else:
#              k = 0

# for i in range(0,5):
#     for j in range(0,5):
#         print('1', end="")
#     print('')
for i in range (0,5):
    print(" ")
    for j in range (0,5):
     print(i%2,end = " ")