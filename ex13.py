import sys

print('Arguments:', len(sys.argv))
print('List:', str(sys.argv))

if sys.argv < 2:
    print('To few arguments, please specify a filename')

filename = sys.argv[1]
print('Filename:', filename)

output
$ python 1.py
Arguments: 1
List: ['1.py']

 output
$ python 1.py lohith
Arguments: 2
List: ['1.py', 'lohith']
