import cmath
a= float(input('enter a: '))
b= float(input('enter b: '))
c= float(input('enter c: '))
d= (b**2)-(4*a*c)
res1 =(-b-cmath.sqrt(d))/(2*a)
res2 =(-b+cmath.sqrt(d))/(2*a)
print('the solution are {0} and {1}'.format(res1,res2))

output
1.
enter a: 5
enter b: 2
enter c: 6
the solution are (-0.2-1.0770329614269007j) and (-0.2+1.0770329614269007j)
2.
enter a: 10
enter b: 20
enter c: 30
the solution are (-1-1.4142135623730951j) and (-1+1.4142135623730951j)
