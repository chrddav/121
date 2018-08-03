sequence = range(5, 24, 4)
list1 = list(sequence)
print("First list:", list1)

sequence = range(5, 24, 4)
print("Elements in the first list:")
for element in sequence:
    print(element)

sequence = range(26, -2, -7)
list2 = list(sequence)
print("Second list:", list2)

total = 0
for element in sequence:
    total = total + element
print("Total of the elements in the second list:", total)
