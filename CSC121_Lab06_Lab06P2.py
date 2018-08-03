import random
num1 = []
for i in range(10):
    m = random.randint(1,15)
    num1.append(m)
tuple1 = tuple(num1)
print("Tuple of 10 random numbers:", tuple1)
tuple2 = tuple1[:3]
print("Tuple of the first 3 numbers: ", tuple2)
tuple3 = tuple1[7:]
print("Tuple of the last 3 numbers: ", tuple3)
tuple4 = tuple2 + tuple3
print("Two tuples concatenated: ", tuple4)
print("Two tuples concatenated and sorted: ", sorted(tuple4))
