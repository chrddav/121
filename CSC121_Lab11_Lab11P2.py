import random
set1 = {random.randint(1,10) for x in range(5)}
print('set1:', set1)
set2 = {random.randint(1,10) for x in range(5)}
print('set2:', set2)

union = (set1 | set2)
print('Union of set1 and set2:', union)

odd_set = {x for x in union if x % 2 == 1}
print('Odd numbers in union of set1 and set2:', odd_set)

intersected_set = (set1 & set2)
print('Intersection of set1 and set2:', intersected_set)

symmetric_difference = (set1 ^ set2)
print('Symmetric difference of set1 and set2:', symmetric_difference)


