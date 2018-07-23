vowels:

Vowel=[‘a’,’e’,’i’,’o’,’u’,'A','E','I','O','U']
woruod=input ("enter a word")
count=0
for letter in word:
    if letter in vowel:
    	count=count+1               
print(count)
output:
    LohIth
    count=2

    
Bmi Calculator:
def bmi(height,weight):
    height = float(input("Your height in metres:"))
    weight = int(input("Your weight in kilograms:"))
    bmi = round(weight/ (height * height), 1)

    if bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi, 'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi, 'which means you are overweight.')

    elif bmi > 30:
        print('Your BMI is', bmi, 'which means you are obese.')

    else:
        print('your weight is underweight')

  
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
       	    print("  *  ",end="")
            print("\r")
output:
    *
    * *
    * * *
    * * * *
    * * * * *

 String reverse 

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s = input("enter a word")
print(reverse(s))
output:
enter a word:lohith
    htihol

Special_character:
def special_character(str):
    special_character=['{','}','[',']','$','@','(',')','!']
    word=input ("enter a word")
    count=0
    for letter in word:
        if letter in special_character:
            print(letter)
            count=count+1
    print(count)
special_character()
output:
Enter a word:{abcd{}][$@!efg
7

    
Factorial :
def fact(n):
    n = 5
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        print(fact)
fact()        
output:
5
120

sentence=input("enter a words:")
word=sentence.split()
word.sort()
for i in word:
    print(i)
output:
enter a word : lohith kumar
kumar lohith
