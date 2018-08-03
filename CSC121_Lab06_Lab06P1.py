test_list1 = []
i = 0
while i < 5:
    test_list1.append(int(input("Enter a test score: ")))
    i = i + 1
print("All scores: ", test_list1)
test_list2 = test_list1 + []
print("Students who scored below 60 get 10 extra points")
j = 0
while j < 5:
    if test_list2[j] < 60:
        new_score = test_list2[j] + 10
        test_list2[j] = new_score
        j = j + 1
    else:
        j = j + 1
print("All scores: ", test_list2)
print("Students whose scores have changed:")
h = 0
while h < 5:
    if test_list1[h] != test_list2[h]:
        print("Old Score: ", test_list1[h], "New Score: ", test_list2[h])
        h = h + 1
    else:
        h = h + 1

