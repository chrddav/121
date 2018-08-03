import random
list1 = []
for i in range(6):
    m = random.randint(10,20)
    list1.append(m)
print("List 1: ", list1)
list2 = []
for i in range(6):
    n = random.randint(15,25)
    list2.append(n)
print("List 2: ", list2)
list3 = list1[:3] + list2[3:]
print("List 3: ", list3)
list4 = list1[3:] + list2[:3]
print("List 4: ", list4)
list3 = sorted(list3)
print("List 3 sorted in ascending order: ", list3)
list4 = sorted(list4)
list4 = list(reversed(list4))
print("List 4 sorted in descending order: ", list4)
biglist = [list3, list4]
print("Big List: ", biglist)
for i in range(2):
    for j in range(6):
        print(biglist[i][j])
odds = []
for odd in list3:
    if odd % 2:
        odds.append(odd)
print("Odd numbers in List 3: ", odds)
evens = []
for even in list4:
    if not even % 2:
        evens.append(even)
print("Even numbers in List 4: ", evens)
