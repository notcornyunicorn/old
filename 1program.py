print('hello! I am a program that you give three integer numbers to and I decide whether the third number is a product or a quotient of the first and the second numbers')
a = input('give me a number\n')
b = input('give me another\n')
c = input('one more\n')
a = int(a)
b = int(b)
c = int(c)
d = a*b
e = a/b
if d == c:
    print('this is a product')
elif e == c:
    print('this is a quotient')
else:
    print('this is neither a product nor a quotient')
