# 1 Write a python script to take your name as input from the user and then print it.
"""Solution 
userInput = input("Enter Your Name : ")
print("Hi ",userInput)"""

# 2 Write a python script to take input from the user. Input must be a number.
"""Solution
userInput =  int(input("Enter Number Only : "))
print("You have Enterd {0}".format(userInput),"and it's ",type(userInput))"""

# 3 Write a python script which takes two numbers from the user, then calculate their sum and display the result.
"""Solution 
num_One = int(input("Enter First Number : "))
num_Two = int(input("Enter Second Number : "))

print("The Sum of Two Numbers is %d"%(num_One+num_Two))"""

# 4 Write a python script which takes the radius from the user and display area of a circle.
"""Solution
from math import pi
input_Radius = float(input("Enter the Radius of the Circle : "))
area_Of_Circle = pi*input_Radius*input_Radius

print("The Area of Circle is ",area_Of_Circle)"""

# 5 Write a python script to calculate the square of a number. Number is entered by the user.
"""Solution 
from math import sqrt

user_Square_Num = int(input("Enter Number to calculate Square : "))
print(sqrt(user_Square_Num))"""

# 6 Write a python script to calculate the area of Triangle. Number is entered by the user.
"""Solution 
formula to calculate  Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2

tri_1 =  float(input("Enter First value : "))
tri_2 = float(input("Enter Second Value : "))
tri_3 = float(input("Enter Third Value : "))

semi_Para = (tri_1 + tri_2 + tri_3)/2

area = (semi_Para*(semi_Para-tri_1)*(semi_Para-tri_2)*(semi_Para-tri_3))**0.5

print("The Area of Triangle is ",area)"""

# 7 Write a python script to calculate average of three numbers, entered by the user
""""Solution 
adding a group of numbers and then dividing by the count of those numbers

avrg_1 =  float(input("Enter First value : "))
avrg_2 = float(input("Enter Second Value : "))
avrg_3 = float(input("Enter Third Value : "))

print("The Average Value is {0}".format(avrg_1+avrg_2+avrg_3/3))"""

# 8 Write a python script to calculate simple interest
""""simple interest formula Si = (P * R * T)/100

principal_Amount = eval(input("Enter Principal Amount : "))
rate_Of_Intrest = eval(input("Enter Rate of Intrest charaged : "))
time_Period = eval(input("Enter Time Period :"))

simple_Interest = (principal_Amount* rate_Of_Intrest* time_Period)/100

print("The Simple Intrest is ",simple_Interest)"""

# 9 Write a python script to calculate the volume of a cuboid.
"""l = eval(input("Enter Length : "))
w = eval(input("Enter Width : "))
h = eval(input("Ener Hight :"))

print("The Total Volume is ",l*w*h)"""

# 10 Write a python script to calculate area of a rectangle
"""Solution 
Area of rectangle = Length x Breadth
length = float(input("Enter Length :"))
breath = float(input("Enter Breath : "))
area_Of_Rectangle = (length*breath)

print("Area of Rectangle is",area_Of_Rectangle )"""
