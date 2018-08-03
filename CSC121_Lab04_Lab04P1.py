FPG = float(input("Enter patient's fasting plasma glucose (FPG) level: "))
if FPG > 125:
    print('This patient has diabetes')
elif FPG > 100:
    print('This patient has pre-diabetes')
else:
    print('This patient has healthy fpg level')
again= input("Enter another patients FPG level?[y/n]: ")
while again == 'y':
    FPG = float(input("Enter patient's fasting plasma glucose (FPG) level: "))
    if FPG > 125:
        print('This patient has diabetes')
    elif FPG > 100:
        print('This patient has pre-diabetes')
    else: print('This patient has healthy fpg level')
    again = input("Calculate commission for another house?[y/n] ")
