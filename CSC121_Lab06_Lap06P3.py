print("Please enter Jean's scores one by one.")
Jean = []
i = 0
while i < 4:
    Jean.append(float(input("Enter a score: ")))
    i = i + 1
print("Jean's scores: ", Jean)
print()
print("Please enter Kayla's scores one by one.")
Kayla = []
j = 0
while j < 4:
    Kayla.append(float(input("Enter a score: ")))
    j = j + 1
print("Kayla's scores: ", Kayla)
print()
print("Please enter Connie's scores one by one.")
Connie = []
k = 0
while k < 4:
    Connie.append(float(input("Enter a score: ")))
    k = k + 1
print("Connie's scores: ", Connie)
print()
all_scores = [Jean, Kayla, Connie]
print("All scores: ", all_scores)
print()
for i in range(len(all_scores)):
    for j in range(4):
        all_scores[i][j] = all_scores[i][j] + 1
print("All scores after extra point: ", all_scores)
print()
for i in range(len(all_scores)):
    all_scores[i] = (sorted(all_scores[i]))
print("All scores after sorting: ", all_scores)
