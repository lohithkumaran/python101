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

Factorial :
def fact(n):
    n = 5
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        print(fact)
fact()        
