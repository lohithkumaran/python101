vowels:

Vowel=[‘a’,’e’,’i’,’o’,’u’,'A','E','I','O','U']
woruod=input ("enter a word")
count=0
for letter in word:
    if letter in vowel:
    	count=count+1               
print(count)

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
bmi()
  
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
       	    print("  *  ",end="")
            print("\r")
 pattern()

