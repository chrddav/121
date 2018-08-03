values = []
i = 'y'
while i == 'y':
    new_values = int(input("Enter an integer from 1-10: "))
    if new_values not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        print("Error: Must be an integer from 1-10: ")
    else: values.append(new_values)
    i = input("Enter another integer? [y/n] ")
    while i not in ('y', 'n'):
        print("Error: Must be y or n: ")
        i = input("Enter another integer? [y/n] ")
total = 0
value_length = len(values)
for value in values:
    total = total + value
avg_value = total / value_length
print("Number list: ", values)
print("Average: ", avg_value)
j = 0
if avg_value > 7:
    while j < value_length:
        values[j] = values[j] - 1
        j = j + 1
    print("Modified number list: ", values)
