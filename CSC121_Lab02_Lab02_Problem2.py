Lab1 = float(input('Enter the score for Lab 1: '))
Lab2 = float(input('Enter the score for Lab 2: '))
Lab3 = float(input('Enter the score for Lab 3: '))
Test1= float(input('Enter the score for Test 1: '))
Test2= float(input('Enter the score for Test 2: '))
LabAverage = (Lab1 + Lab2 + Lab3) / 3
TestAverage = (Test1 + Test2) /2
Course_Grade = (LabAverage*0.55) + (TestAverage*0.45)
print('Lab Average:', format(LabAverage, '.2f'))
print('Test Average:', format(TestAverage, '.2f'))
print('Course Grade:', format(Course_Grade, '.2f'))
