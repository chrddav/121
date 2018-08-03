X = float(input('Enter first number: '))
Y = float(input('Enter second number: '))
Z = float(input('Enter third number: '))
if X > Y and X > Z:
    print ('The largest number is: ', X)
else:
    if Y > X and Y > Z:
        print ('The largest number is: ', Y)
    else:
        if Z > X and Z > Y:
            print ('The largest number is: ', Z)
        else:
            print ('The largest number is: ', X)
