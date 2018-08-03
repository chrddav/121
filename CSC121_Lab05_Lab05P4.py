import random
num1 = []
for i in range(5):
    m = random.randint(1,9)
    num1.append(m)
print("First list:", num1)

num2 = []
for j in range(5):
    n = random.randint(2,8)
    num2.append(n)
print("Second list:", num2)

print("Larger number in each comparison:")
i = 0
while i < 5:
    if num1[i] > num2[i]:
        print(num1[i])
    else:
        print(num2[i])
    i = i + 1
