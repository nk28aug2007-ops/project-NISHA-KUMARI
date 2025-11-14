# #list


# my_list=["apple","banana","cherry"]
# #print(my_list)


# #format string


# Name="bob"
# age=20
# print(x+y) 

# x="bob"
# y=20
# print("my name is {x} and my age is{y}")

# x=5
# x+=3
# print(x)

# x-=3
# print(x)
# x*=3
# print(x)
# x/=3
# print(x)




























# # x=5
# # y=10
# # print(x==y)
# # print(x!=y)
# # print(x>=y)
# # print(x<=y)
# # print(x>y)
# # print(x<y)



# # x=8
# # y=x
# # z=1 
# # print(y)
# # print(x is y)
# # print(x is not y)


# # colors={"red","green","blue",}
# # print(colors)

# # colors.add("yellow")
# # print(colors)

# # colors.remove("green")
# # print(colors)

# # for color in colors:
# #      print(color)


# students={
# "name":"nisha",
# "age":30,
# "grades":"A"
# }
# print(students)
# students ["age"]=21
# students["city"]="Delhi"
#  print(students)

# students.pop("grade")
#  del students["city"]
#  print(students)
 




# if else 




 
# age=20
 # if ageage>=18:
 #     print("you are adult")
 # else:
 #     print("you are not adult")

 # if age<=18:
# print("you are adult")
# # else:
# print("you are not adult")

# age=18
# if age>18:
#     print("you are teen")
# elif age==17:
#  print("you are 17")
# elif age==16:
#    print("you are 16")
# else:
#    print("you are not adult")

# x=5
# if x>10:
#     print("x is greater than 10")

#     if x>20:
#       print("x is greater then 20") 
# else:
#       print("x is not greater then 20")

# x=7
# if x%2==0:
#     print(f"even")
# else:
#    print(f"odd")


# fruits=["apple","banana","cherry"]
# print(fruits)

# loops

# word="python"
# for letter in word:
#    print(letter)

# for i in range(5):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(1,4):
#     print(i)

# for i in range(1,4):
#    for j in range(1,3):
#      print(f"i={i},j={j}")

# for i in range(1,6):
#   if i==4:
#     break 
#   print(i)

#   for i in range(1,6):
#     if i==3:
#       continue
#     print(i)

# # question1
# for i in range(1,20):
#         print(i)

#     # question2 
# x=30
# if x%2==0:
#   print(f"even")
# else: 
#   print(f"odd")

# def greet():
#    print("Hello,Python!")

#    greet() #calling the function



# #function



# def greet(name):
#       print(f"Hello,{name}!")

# greet("Alice")
# greet("Bob")


# def add(a,b):
#     return a + b
# result=add(5,3)
# print(result)


# def sub(a,b):
#     return a - b
# result=sub(5,3)
# print(result)


# def mull(a,b):
#     return a * b
# result=mull(5,3)
# print(result)


# def div(a,b):
#     return a / b
# result=div(5,3)
# print(result)


# x=10 #global
# def my_func():
#     y=5 #local
#     print("inside:",x)


# def my_func()
#     print("outside:",x)
#     print(y) ,y is locals


# def my_func():
#     print(x,y)
#  #   class
#     my_func()
#     print(x)
#     print(y)


# def greet():
#     print(f"hello")
# greet()#calling the function


# 
# def greet(name):
#     print(f"Hello{"name"}!)
# greet("Alice")
# greet("Bob")


# def add(a,b):
#     return a+b
# result=add(121,233)
# print(result)


#class car:
# def__into__(self,brand,color):
# self.brand = brand
# self.color = color
# def drive(self):
#     print(f"{self.color} {self.brand} is driving")
# car1 = car("BMW","Black")
# car2 = car("Tesla","White")

# car1.drive()     
# car2.drive()



# import array



# number=array.array[1,2,3,4,5]
# print(number)

#python # pip install numpy
 
# from numpy import random 

# x=random.randint(100)
# print(x)

# x=random.rand()
# print(x)
# print(type(x))

# from numpy import random

# x=random.randint(100,size=(5))
# print(x)

# x=random.randint(100,size=(3,5,))
# print(x)


# x=random.randint(100,size=(3,5,7))
# print(x)

# x=random.randint(100,size=(2,2,2,5))
# print(x)


# x=random.choice([4,5,6] , size=(5))
# print(x)





# pandas


# import pandas as pd

# data=[10,20,30,40]
# s=pd.Series(data)

# print(s)



# import pandas as pd

# data={
#     "Name":["Alice","Bob","Charlie","David"],
#     "Age":[24,27,22,32],
#     "city":["Delhi","Mumbai","chennai","kolkata"]
# }

# df=pd.DataFrame(data)

# print(df)

#from the numpy array

# import numpy as np

# arr=np.array([1,2,3,4,5])
# s=pd.Series(arr)

# print(s)


#from a Dictionary



# data={"Math":90,"Science":85,"English":78}

# s=pd.Series(data)

# print(s)


import pandas as pd
df = pd.read_csv()
print(df.head())
print(df.tail())






