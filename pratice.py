# from time import time
# def performance(fn):
#     def wrapper(*args,**kawrgs):
#         t1 = time()
#         result = fn(*args,**kawrgs)
#         t2 = time()
#         print(f"took {t2-t1}ms")
#     return wrapper()
#
# @performance
# def long_time():
#     for i in range(100):
#         i*5
#         print(i)
# print(long_time)
#
# while True:
#     try:
#         age = int(input("what's your age?"))
#         print(age)
#     except:
#         print("please enter the number")
#     else:
#         print("Thank you")
#         break

#To prit first 10 nature numbers:
#i=1
# while i<=10:
#     print(i)
#     i+=1

#To add the numbers till the given number:
# n= int(input("enter the number"))
# i=0
# s=0
# while i<=n:
#     s=s+i
#     i+=1
# print(s)

#program for multiplication of given number
# n= int(input('Enter the number for multiplication table'))
# i=0
# Table =0
# for i in range(1,11):
#     Table=i*n
#     print(Table)
#     i+=1

# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# numbers =[12,75,150,180,145,525,50]
# i=0
# for i in numbers:
#     if i%5==0 and i<=150:
#         print(i)
#     elif i > 500:
#         break

# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10
#
#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)

# def fib(num):
#     a=0
#     b=1
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp +b
#
# for i in fib(21):
#     print (i)
#
# import array
#
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
# import pdb
# class Username:
#     def __init__(self,name,age):
#
#         self.name = name
#         self.age = age
#     def run(self):
#         print("run")
#     def speak(self):
#         print(f"My name is {self.name} and i am {self.age} years old")
#
# palyer1 = Username("vamshi", 24)
# pdb.set_trace()
# print(palyer1.speak())

# password = str(input("enter your password"))
# num_str = ""
# for i in password:
#     if i.isdigit()==True:
#         num_str = num_str + i
# if len(password) >=8 and num_str.isdigit()== True and password.capitalize()==password and password.isalnum()==True:
#     print("Valid password")
# else:
#     print("invalid password")


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

# import random
#
# def run_game(guess, answer):
#     if 0 < guess < 11:
#         if guess == answer:
#             print("you are genious")
#             return
#     else:
#         print("enter the correct number")
#
# answer = random.randint(1, 10)
# while True:
#     try:
#         guess = int(input("Guess number from 1~10"))
#         if (run_game(guess, answer)):
#             break
#     except:
#         print("error")



