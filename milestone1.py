import sys
vowels(str)
bmi(height,weight)
pattern(n)
reverse(s)
special_character(str)
fact(n)
sort(str)
def vowels(str):
    Vowel=[‘a’,’e’,’i’,’o’,’u’,'A','E','I','O','U']
    word=input ("enter a word")
    count=0
    for letter in word:
        if letter in vowel:
    	    count=count+1               
    print(count)
    return
    
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
    return
  
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
       	    print("  *  ",end="")
            print("\r")
    return        

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

    s = input("enter a word")
    print(reverse(s))
    
def special_character(str):
    special_character=['{','}','[',']','$','@','(',')','!']
    word=input ("enter a word")
    count=0
    for letter in word:
        if letter in special_character:
            print(letter)
            count=count+1
    print(count)
    return
   
def fact(n):
    n = 5
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        print(fact)
    return   
def sort(str):
    sentence=input("enter a words:")
    word=sentence.split()
    word.sort()
    for i in word:
        print(i)
    return    
if __name__ == "__main__":
    arg_len = len(sys.argv [1:])
    print(arg_len)
    if (arg_len <1):
        print("ERROR\t:exitting......arguments passed")
        sys.exit()

    print("calling main function")
    main(sys.argv[1])
