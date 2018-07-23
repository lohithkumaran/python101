

my_list_1 = []


my_list_2 = [1, 2, 3]
Print (my_list_2)
[1,2,3]

my_list_3 = [1, "Hello", 3.4]
Print (my_list_3)
[1,'Hello', 3.4]
my_list_4 = ["mouse", [8, 4, 6], ['a']]
my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[4])

Output
p
o
e


n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1])    
print(n_list[1][3])
 Output
  a 
  5

my_list = ['p','r','o','b','e']
print(my_list[-1])
print(my_list[-5])

 Output
  e 
  p
  

my_list = ['p','r','o','g','r','a','m','i','z']

print(my_list[2:5])

print(my_list[:-5])

print(my_list[5:])

print(my_list[:])
output
['o', 'g', 'r']
['p', 'r', 'o', 'g']
['a', 'm', 'i', 'z']
['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']



odd = [2, 4, 6, 8]
odd[0] = 1            
print(odd)

output
[1, 4, 6, 8]


odd[1:4] = [3, 5, 7]  
print(odd)   

output
[1, 3, 5, 7]




odd.append(7)
print(odd)

output
[1, 3, 5, 7, 7]

odd.extend([9, 11, 13])
print(odd)
print(my_list.pop(1))

Output: ['r', 'b', 'l', 'e', 'm']

print(my_list)
 Output: 'm'
print(my_list.pop())
 Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()



odd = [1, 3, 5]
Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
Output: ["re", "re", "re"]
print(["re"] * 3)


my_list = ['p','r','o','b','l','e','m']


del my_list[2]

Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)


del my_list[1:5]  
Output: ['p', 'm']
print(my_list)
# delete entire list
del my_list       
print(my_list) # see whats the output
