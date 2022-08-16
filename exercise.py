# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


# task 1


'''three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 4 
max_num = 100

for i in range(1, max_num):
    # % or modulo division gives you the remainder 
 
    if i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)
    elif i%num1 == 0 and i%num2 == 0:
       print(i, three_mul+five_mul)'''


# task 2
# sum: 1 to 5

'''number = 1
total = 0
while number <= 5 :
    total += number
    number += + 1
print(total)'''

# task 3

'''for x in range(3): 
    print(x)'''

# task 4

'''for j in range(5):
     print("This is loop number", j)'''

'''countdown = 5
while countdown >= 0 :
    if countdown !=0 :
      print(countdown)
    countdown -= 1
else: 
    print("Start!")'''

# task 5

'''x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or z== x:
   sum = 0 
else:
    sum = x + y + z
print("Calculated sum is ", sum)'''

# task 6

'''x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result > 15 and result < 20:
    result = 20
print("Calculated sum is ", result)'''


# task 7

'''a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " , b=", b)

print("After swapping: a =", b, " , b=", a)'''

# task 8

'''x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y, z))
print("The minimum value is ", min(x, y, z))'''


# task 9


'''x = input("Type your value:")

if x == "0":
    x = False
elif x == "1":
    x = True
else:
  pass

print("Your entered value is now ", x)'''

# 10
x = int(input("First number:"))
y = int(input("Second number:"))

if x % y == 0:
    print("First number is divisible by second number, result =", x /y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y / x)
else:
    print("Numbers are non-divisible!")