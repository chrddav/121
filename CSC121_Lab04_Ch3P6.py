i = 1
per_row = 10
while i <=100:
    while(per_row > 0):
        print(i, end=' ')
        i = i + 1
        per_row = per_row - 1
    print()
    per_row = 10


idea = list(range(1, 101))
i = 0
while i < 100:
    print("{:>3d}".format(idea[i]), end=" ")
#{:>3d} is format style to right align integers 3 spaces
    i = i+1
    if i % 10 == 0:
        print("")
