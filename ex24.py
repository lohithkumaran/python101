Creating a tuple 
	empty_tuple = ()
	print (empty_tuple)
output
()

	tup = 'python', 'geeks'
	print(tup)
	output
	('python', 'geeks')

	

	
	tup = ('python', 'geeks')
	print(tup)
	
	Length of a Tuple
	tuple2 = ('python', 'geek')
	print(len(tuple2))
	
	2

	Concatenation of Tuples

	tuple1 = (0, 1, 2, 3)
	tuple2 = ('python', 'geek')
	print(tuple1 + tuple2)
	output
        (0,1,2,3,'python','geek')


	Nesting of Tuples

	tuple1 = (0, 1, 2, 3)
	tuple2 = ('python', 'geek')
	tuple3 = (tuple1, tuple2)
	print(tuple3)
	output
	((0, 1, 2, 3), ('python', 'geek'))

	
	Repetition in Tuples

	# Code to create a tuple with repetition

	tuple3 = ('python',)*3
	print(tuple3)

	tuple4 = ('python')*3
	print(tuple4)
	
	Immutable Tuples
	tuple1 = (0, 1, 2, 3)
	tuple1[0] = 4
	print(tuple1)
	
	Slicing in Tuples
	tuple1 = (0 ,1, 2, 3)
	print(tuple1[1:])
	print(tuple1[::-1])
	print(tuple1[2:4])
        output
	(1, 2, 3)
        (3, 2, 1, 0)
        (2, 3)

	Deleting a Tuple
	tuple3 = ( 0, 1)
	del tuple3
	print(tuple3)

	#Lets see how to delete a tuple
	myTup = tuples = [('a', 9), ('b', 8), ('c', 7), ('d', 6), ('e', 5), ('f
  	 ', 4), ('g', 3), ('h', 2), ('i', 1), ('j', 0)]
     

	Converting list to a Tuple

	# Code for converting a list and a string into a tuple

	list1 = [0, 1, 2]
	print(tuple(list1))
	print(tuple('python')) 
	output								     
(0, 1, 2)
('p', 'y', 't', 'h', 'o', 'n')
