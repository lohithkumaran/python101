num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number between",num1,",",num2,"and",num3,"is",largest)
output
The largest number between 10 , 14 and 12 is 14

LCD

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)
Output: False

print(x2 is y2)
Output: True


print(x3 is y3)
Output: False


Membership operator
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
Output: True


print('hello' not in x)
Output: True

print(1 in y)
Output: True

print('a' in y)
Output: False
