# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


# task 1


three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5
max_num = 100

for i in range(1, max_num):
    # % or modulo division gives you the remainder 
    if i%num1 == 0 and i%num2 == 0:
       print(i, three_mul+five_mul)

    elif i%num2 == 0:
        print(i, five_mul)
    elif i%num1 == 0:
     print(i, three_mul)


# task 2 
# sum: 1 to 5 # I changed the variable name from Sum to Total
n = 5
number = 1
total = 0
while number < n + 1 :
    total += number
    number += + 1
print('Total =', total)


# task 3
n = 5
sum = 0

for num in range(n+1): 
    sum += num
print("Sum=", sum)

# task 4
 # 4.1
for x in range(3):
        print(x)

# 4.2
for j in range(5):
     print("This is loop number", j)
# 4.3
x = 10    
while x > 0:
    print(x)
    x -= 1
# 4.4
countdown = 5
while countdown >= 0 :
    if countdown !=0 :
      print(countdown)
    countdown -= 1
else: 
    print("Start!")

# task 5

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z or z== x:
   result = 0 
else:
    sum = x + y + z
print("Calculated sum is ", result)

# task 6

x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result > 15 and result < 20:
    result = 20
print("Calculated sum is ", result)


# task 7

a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " , b=", b)

print("After swapping: a =", a, " , b=", b)

#b, a = a, b

temp = b
b = a
a = temp

# task 8

x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y, z))
print("The minimum value is ", min(x, y, z))


# task 9


x = input("Type your value:") # 1st bug string not recognized 

if x == "0": # 2nd bug here, not integer; equality
    x = False # 3nd bug false 
elif x == "1": # 4th bug, not integer, equality 
    x = True
else:
  pass # indentation issue 

print("Your entered value is now ", x) 



# 10
x = int(input("First number:"))
y = int(input("Second number:"))

if x % y == 0:
    print("First number is divisible by second number, result =", x /y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y / x)
else:
    print("Numbers are non-divisible!")