# #Ex1
# x= str(input("Enter your language code:"))
#
# if x=="A"or x=="a":
#     print("Ada language is seleted to installation")
# elif x=="B" or x=="b":
#     print("Basic language is seleted to installation")
# elif x=="C" or x=="c":
#     print("Cobol language is seleted to installation")
# elif x=="D" or x=="d":
#     print("Dbase language is seleted to installation")
# elif x=="F" or x=="f":
#     print("Fortran language is seleted to installation")
# elif x=="D" or x=="d":
#     print("Dbase language is seleted to installation")
# elif x=="P" or x=="p":
#     print("Pascal language is seleted to installation")
# elif x=="V" or x=="v":
#     print("Visual C++ language is seleted to installation")
# else :
#   print ("Error! Operation is not correct")
#
# #Exp2
# n = int(input("enter a number"))
#
# if n%2!=0:
#   print ("Weird")
# elif n%2==0 and n>=2 and n<=5:
#    print ("Not Weird")
# elif n%2==0 and n>=6 and n<=20:
#    print ("Weird")
# elif n%2==0 and n>=20:
#   print ("Not Weird")
#
# #Ex3: To find the leap year
#
# year= int(input("Enter a year"))
#
# if year%4==0 and (year%400==0 or year%100!=0):
#   print("Year is leap year")
# else:
#   print("Year is not a leap year")
#
# Ex4- Jun22
#
# password = str(input('Enter your password:'))
# length = len(password)
# if length >=8:
#     print("Valid password")
# else:
#     print("invalid password")
# Ex5
# l = x
# i=0
# for i in l:
#     if i%2==0:
#         print(f"{i} is even")
#     else:
#         print(f'{i} is odd')

# Ex6: To print the output as below
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5:
#             print("*",end=" ")
#         elif j ==1 or j==5:
#             print ("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# Ex- class :To print the output as below
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
# * * * * * *
# k=1
# for i in range(6,0,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for p in range(k):
#         print("*",end=" " )
#     k+=1
#     print()

# # Ex7: To print the output as below
#        *
#       * *
#      * * *
#     * * * *
#      * * *
#       * *
#        *
# k=1
# for i in range(4,0,-1):
#     for j in range(i):
#         print(" ",end="")
#     for p in range(k):
#         print("* ",end="" )
#     k+=1
#     print()
# X=3
# for i in range(2,5):
#     for j in range(i):
#         print(" ",end="")
#     for p in range(X):
#         print("* ",end="" )
#     X-=1
#     print()

# Ex8: To print the output as below
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
# for i in range(5,0,-1):
#     k=5
#     for j in range(i):
#         print(f"{k}",end=" ")
#         k-=1
#     print()
# for h in range(2,6):
#     k=5
#     for l in range(h):
#         print(f"{k}", end=" ")
#         k-=1
#     print()

# EX9: To find max and min numbers from array without using predefined functions
# import array
# ar = array.array("i", [1,2,3,4,5,6,7,8,12,10,9])
# max=1
# min=1
# for i in ar:
#     if i<=min:
#         min = i
#     elif i>=max:
#         max =i
# print(f'maximum number in the array is {max}')
# print(f'minimum number in the array is {min}')

# EX10:To find 2nd lagest number from array without using predefined functions
# import array
# ar = array.array("i", [1,2,3,4,5,6,7,8,12,10,9,15,16,22,17])
# max=1
# sec_max =1
# for i in ar:
#     if i>=max:
#         max=i
# for i in ar:
#     if i>=sec_max and i<max:
#         sec_max= i
# print(f'largest number in the array is {max}')
# print(f'second largest number in the array is {sec_max}')

# Ex11: Password check: 8 characters, First letter captial, Any one numaric value
# password = str(input("enter your password"))
# num_str = ""
# for i in password:
#     if i.isdigit()==True:
#         num_str = num_str + i
# if len(password) >=8 and num_str.isdigit()== True and password.capitalize()==password and password.isalnum()==True:
#     print("Valid password")
# else:
#     print("invalid password")

# Ex12: Input numbers in words output numbers in digits
# give_str =(input("enter your number in words").split())
# for i in give_str:
#     if i=="one":
#         print('1',end="")
#     elif i=="two":
#         print('2',end="")
#     elif i == "three":
#         print('3',end="")
#     elif i == "four":
#         print('4',end="")
#     elif i == "five":
#         print('5',end="")
#     elif i == "six":
#         print('6',end="")
#     elif i == "seven":
#         print('7',end="")
#     elif i == "eigth":
#         print('8',end="")
#     elif i == "nine":
#         print('9',end="")
#     elif i == "ten":
#         print('10',end="")
#     elif i == "zero":
#         print('0',end="")

# Ex13: enter sentence to find lagest word
# given_str = input("enter sentence to find lagest word").split()
# len_of_lagest_word = 0
# lagest_word =""
# for i in given_str:
#     if len(i) >= len_of_lagest_word:
#         len_of_lagest_word = len(i)
#         lagest_word = i
# print(f"lagest word is {lagest_word} with length {len_of_lagest_word} characters")

Data = str(input(Enter the roman number))
Lt = Data.split()

for i in Lt:
    if i == I:
        print("1",end="")
    elif i == V:
        print("1",end="")
    if i == I:
        print("1", end="")
    if i == I:
        print("1", end="")


